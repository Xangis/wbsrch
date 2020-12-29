// Requires package libpqxx-dev.
//
// Build: g++ -std=c++11 -o index index.cpp -l pqxx
//
#include <iostream>
#include <sstream>
#include <string>
#include <pqxx/pqxx>

using namespace std;
using namespace pqxx;

int main(int argc, char* argv[]) {
   if( argc < 2 ) {
     cout << "This program requires 1 argument: number of items to process. Try 10. If any third argument is supplied, it will reindex old rather than new." << endl;
     exit(1);
   }
   stringstream sql;
   int numitems = atoi(argv[1]);
   bool redo = false;
   if( argc > 2 ) {
       redo = true;
   }

   try {
      connection C("dbname = zetaweb user = zetaweb password = password \
      hostaddr = 127.0.0.1 port = 5432");
      if (C.is_open()) {
         cout << "Opened database successfully: " << C.dbname() << endl;
      } else {
         cout << "Can't open database" << endl;
         return 1;
      }
      connection D("dbname = indexes user = indexes password = password \
      hostaddr = 127.0.0.1 port = 5432");
      if (D.is_open()) {
         cout << "Opened database successfully: " << D.dbname() << endl;
      } else {
         cout << "Can't open database" << endl;
         return 1;
      }

      /* Create SQL statement */
      if (!redo ) {
          sql << "SELECT id, keywords FROM dir_pendingindex ORDER BY date_added ASC LIMIT " << numitems << endl;
      } else {
          sql << "SELECT id, keywords FROM dir_indexterm ORDER BY date_indexed ASC LIMIT " << numitems << endl;
      }

      /* Create a non-transactional object. */
      nontransaction N(D);
      nontransaction O(C);

      cout << "Executing: " << sql.str() << endl;
      /* Execute SQL query */
      result R( N.exec( sql.str() ));

      /* Print all records */
      int count = 0;
      for (result::const_iterator c = R.begin(); c != R.end(); ++c) {
         int id = c[0].as<int>();
         std::string keywords = c[1].as<string>();
         cout << "ID = " << id << ", Keywords = " << keywords << endl;

         // Python: BuildIndexForTerm(keywords)
         /* Python Code
    start = timezone.now()
    multiword = False
    if ' ' in keywords:
        multiword = True
    # We have to keep track of the number of previous queries and add from there because
    # when we index multiple terms, queries are additive.
    if verbose:
        prevqueries = len(connection.queries)
    keywords = keywords.strip()
    if len(keywords) < 1:
        if verbose:
            print('BuildIndexForTerm: Search term is empty. Refusing to index.')
        return False
    keywords = keywords.lower()
    term = None
    new = False
    term_model = GetIndexModelFromLanguage(lang)
    site_model = GetSiteInfoModelFromLanguage(lang)
    try:
        term = term_model.objects.get(keywords=keywords)
        if term.num_pages is None:
            term.num_pages = 0
    except ObjectDoesNotExist:
        term = term_model()
        term.keywords = keywords
        term.num_results = 0
        term.num_pages = 0
        new = True
    if verbose:
        print('{0} Indexing term ({1}): {2}'.format(timezone.now().isoformat(), lang, keywords))
        if term.num_results > 0:
            print('(Reindex) Term had {0} results and {1} pages last index on {2}'.format(term.num_results, term.num_pages, term.date_indexed))
    # We do not need pagecontents, lastcrawled, or firstcrawled. This may or may not save some effort.
    # However, leaving out pagetext saves a *lot* of effort and computation time.
    kp = '%' + keywords + '%' # Allow us to do raw ILIKE queries without formatting problems.
    spacelesskeywords = keywords.replace(' ', '%')
    asciikeywords = unidecode(spacelesskeywords)
    if spacelesskeywords != asciikeywords:
        print('Checking URL as {0}'.format(asciikeywords))
    akp = '%' + asciikeywords + '%'
    # Don't even bother selecting on page text, keywords, or description ILIKE for massive queries.
    # Since title, first head tag, and URL are most important. About 1.2% of queries fit this and
    # indexing them can be a multi-hour process on a slow server.
    #
    # On 2015-03-18 added a limit of 1 million rows to every query. Results for anything with a million rows will be crappy
    # and a popularity contest anyway, at least that gives us a chance of succeeding in our indexing.
    querystart = timezone.now()
    if term.num_pages > 100000:
        sql_query = ("SELECT id, rooturl, url, pagetitle, pagedescription, pagefirstheadtag, pagekeywords, pagetext, pagesize FROM " +
                     site_model._meta.db_table +
                     " WHERE (pagetitle ILIKE %s OR url ILIKE " +
                     "%s OR pagefirstheadtag ILIKE %s) LIMIT 1000000")
        index_items = site_model.objects.raw(sql_query, [kp, akp, kp])
    elif term.num_pages > 40000:
        sql_query = ("SELECT id, rooturl, url, pagetitle, pagedescription, pagefirstheadtag, pagekeywords, pagetext, pagesize FROM " +
                     site_model._meta.db_table +
                     " WHERE (pagetitle ILIKE %s OR url ILIKE " +
                     "%s OR pagefirstheadtag ILIKE %s OR pagefirsth2tag ILIKE %s) LIMIT 1000000")
        index_items = site_model.objects.raw(sql_query, [kp, akp, kp, kp])
    elif term.num_pages > 10000:
        sql_query = ("SELECT id, rooturl, url, pagetitle, pagedescription, pagefirstheadtag, pagekeywords, pagetext, pagesize FROM " +
                     site_model._meta.db_table +
                     " WHERE (pagetitle ILIKE %s OR url ILIKE " +
                     "%s OR pagefirstheadtag ILIKE %s OR pagefirsth2tag ILIKE %s OR pagefirsth3tag ILIKE %s) LIMIT 1000000")
        index_items = site_model.objects.raw(sql_query, [kp, akp, kp, kp, kp])
    # If we have more than 3000 results, ignore the specific page text because we can get what we
    # need from the head tag, url, keywords, description, and title (mostly).
    elif abbreviated or term.num_pages > 3000:
        sql_query = ("SELECT id, rooturl, url, pagetitle, pagedescription, pagefirstheadtag, pagekeywords, pagetext, pagesize FROM " +
                     site_model._meta.db_table +
                     " WHERE (pagetitle ILIKE %s OR pagekeywords LIKE %s OR pagedescription ILIKE %s OR url ILIKE " +
                     "%s OR pagefirstheadtag ILIKE %s OR pagefirsth2tag ILIKE %s OR pagefirsth3tag ILIKE %s) LIMIT 1000000")
        index_items = site_model.objects.raw(sql_query, [kp, kp, kp, akp, kp, kp, kp])
    else:
        sql_query = ("SELECT id, rooturl, url, pagetitle, pagedescription, pagefirstheadtag, pagekeywords, pagetext, pagesize FROM " +
                     site_model._meta.db_table +
                     " WHERE (pagetitle ILIKE %s OR pagekeywords LIKE %s OR pagedescription ILIKE %s OR pagetext ILIKE " +
                     "%s OR url ILIKE %s OR pagefirstheadtag ILIKE %s OR pagefirsth2tag ILIKE %s OR pagefirsth3tag ILIKE %s) LIMIT 1000000")
        index_items = site_model.objects.raw(sql_query, [kp, kp, kp, kp, akp, kp, kp, kp])
    if verbose:
        print(sql_query.replace("%s", ("'" + kp + "'")))
    ratings = []
    if verbose:
        querydelta = timezone.now() - querystart
        print('Query took: {0} seconds'.format(querydelta.total_seconds()))
        print('{0} Calculating values.'.format(timezone.now().isoformat()))
    # Calculate the score for each page we've found.
    termcalcstart = timezone.now()
    for item in index_items:
        try:
            weight = CalculateTermValue(item, keywords, abbreviated, lang)
        # Any problem calculating the term's value and it gets a zero.
        except Exception:
            weight = 0
        ratings.append([item.id, weight])
    term.num_pages = len(ratings)
    # Sort by score
    if verbose:
        termcalcdelta = timezone.now() - termcalcstart
        print('Calculating term values took: {0} seconds'.format(termcalcdelta.total_seconds()))
        print('{0} Sorting index by score.'.format(timezone.now().isoformat()))
    ratings.sort(key=lambda tup: tup[1], reverse=True)
    ratings = ratings[0:5000]
    # Load existing terms for multi-word phrases.
    if multiword and type:
        ratings = AddIndividualWords(ratings, keywords, type, lang)
        # Re-trim the ratings so we're still at 5000 max.
        ratings = ratings[0:5000]
    term.keywords = keywords
    term.page_rankings = str(ratings)
    term.num_results = len(ratings)
    end_delta = timezone.now() - start
    term.index_time = end_delta.total_seconds()

    if verbose:
        print('{0} Saving index term.'.format(timezone.now().isoformat()))
    jsonify_start = timezone.now()
    # Don't save new index terms unless it has at least one result.
    saved = True
    if not new or term.num_pages > 0:
        if new and multiword:
            individualwords = term.keywords.split(' ')
            blocked = term_model.objects.filter(keywords__in=individualwords, actively_blocked=True).count()
            if blocked > 0:
                print('Marking this term as blocked because at least one of the words in it is blocked.')
                term.actively_blocked = True
        term.save()
        JsonifyIndexTerm(term, lang, verbose=verbose)
    else:
        if verbose:
            print('Not saving index term because it does not have at least one result.')
        saved = False
    jsonify_delta = timezone.now() - jsonify_start
    if verbose:
        print('{0} Done indexing: {1}, {2} results from {3} pages.'.format(timezone.now().isoformat(), keywords, term.num_results, term.num_pages))
        LogQueries(connection.queries[prevqueries:])
    try:
        print("Index Time for '{0}': {1} seconds, Jsonify Time: {2} seconds (includes ranking update), {3} pages, {4} results.".format(
            term.keywords, term.index_time, jsonify_delta.total_seconds(), term.num_pages, term.num_results))
    except Exception:
        pass
    return saved
         */

         // Python: RemoveFromPending(keywords)
         std::string sqlthree("DELETE FROM dir_pendingindex WHERE KEYWORDS = %s");
         count += 1;
         // cout << "Executing: " << sqlthree << endl;
         cout << "Indexed term " << keywords << endl;
         nontransaction P(D);
         result T( P.exec( sqlthree.c_str(), keywords ));
         P.commit();
      }
      cout << "Operation done successfully. " << count << " terms indexed." << endl;
      C.disconnect ();
      D.disconnect ();
   } catch (const std::exception &e) {
      cerr << e.what() << std::endl;
      return 1;
   }

   return 0;
}
