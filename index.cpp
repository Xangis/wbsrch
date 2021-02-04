// Requires package libpqxx-dev.
//
// Build: g++ -std=c++11 -o index index.cpp -l pqxx
//
#include <iostream>
#include <sstream>
#include <string>
#include <chrono>
#include <algorithm>
#include <cctype>
#include <list>
#include <pqxx/pqxx>

using namespace std;
using namespace std::chrono;
using namespace pqxx;

struct IndexTerm {
    std::string keywords;
    int num_results;
    int num_pages;
    bool saved;
    std::string page_rankings;
    float index_time;
    bool new_term;
    bool actively_blocked;
};

template <std::ctype_base::mask mask>
class IsNot
{
    std::locale myLocale;       // To ensure lifetime of facet...
    std::ctype<char> const* myCType;
public:
    IsNot( std::locale const& l = std::locale() )
        : myLocale( l )
        , myCType( &std::use_facet<std::ctype<char> >( l ) )
    {
    }
    bool operator()( char ch ) const
    {
        return ! myCType->is( mask, ch );
    }
};

typedef IsNot<std::ctype_base::space> IsNotSpace;

std::string strip( std::string const& original )
{
    std::string::const_iterator right = std::find_if( original.rbegin(), original.rend(), IsNotSpace() ).base();
    std::string::const_iterator left = std::find_if(original.begin(), right, IsNotSpace() );
    return std::string( left, right );
}

std::string lower(std::string original)
{
    std::transform(original.begin(), original.end(), original.begin(), [](unsigned char c){ return std::tolower(c); });
    return original;
}

std::string GetPageTermQuery(IndexTerm term)
{
    std::string spacelesskeywords = term.keywords.replace(' ', '%');
    std::string asciikeywords = unidecode(spacelesskeywords);
    if( spacelesskeywords != asciikeywords )
        printf("Checking URL as %s", asciikeywords);
    std::string akp = '%' + asciikeywords + '%';
    std::string sql_query;
    if( term.num_pages > 100000 )
        sql_query = ("SELECT id, rooturl, url, pagetitle, pagedescription, pagefirstheadtag, pagekeywords, pagetext, pagesize FROM site_info" +
                     " WHERE (pagetitle ILIKE %s OR url ILIKE " +
                     "%s OR pagefirstheadtag ILIKE %s) LIMIT 1000000");
    else if( term.num_pages > 40000 )
        sql_query = ("SELECT id, rooturl, url, pagetitle, pagedescription, pagefirstheadtag, pagekeywords, pagetext, pagesize FROM site_info" +
                     " WHERE (pagetitle ILIKE %s OR url ILIKE " +
                     "%s OR pagefirstheadtag ILIKE %s OR pagefirsth2tag ILIKE %s) LIMIT 1000000");
    else if( term.num_pages > 10000 )
        sql_query = ("SELECT id, rooturl, url, pagetitle, pagedescription, pagefirstheadtag, pagekeywords, pagetext, pagesize FROM site_info" +
                     " WHERE (pagetitle ILIKE %s OR url ILIKE " +
                     "%s OR pagefirstheadtag ILIKE %s OR pagefirsth2tag ILIKE %s OR pagefirsth3tag ILIKE %s) LIMIT 1000000");
    else if( term.num_pages > 3000 )
        sql_query = ("SELECT id, rooturl, url, pagetitle, pagedescription, pagefirstheadtag, pagekeywords, pagetext, pagesize FROM site_info" +
                     " WHERE (pagetitle ILIKE %s OR pagekeywords LIKE %s OR pagedescription ILIKE %s OR url ILIKE " +
                     "%s OR pagefirstheadtag ILIKE %s OR pagefirsth2tag ILIKE %s OR pagefirsth3tag ILIKE %s) LIMIT 1000000");
    else
        sql_query = ("SELECT id, rooturl, url, pagetitle, pagedescription, pagefirstheadtag, pagekeywords, pagetext, pagesize FROM site_info" +
                     " WHERE (pagetitle ILIKE %s OR pagekeywords LIKE %s OR pagedescription ILIKE %s OR pagetext ILIKE " +
                     "%s OR url ILIKE %s OR pagefirstheadtag ILIKE %s OR pagefirsth2tag ILIKE %s OR pagefirsth3tag ILIKE %s) LIMIT 1000000");
    return sql_query;
}

void BuildIndexForTerm(std::string keywords)
{
    if( keywords.empty() )
    {
        return;
    }
    cout << "Indexing " << keywords << endl;
    auto start = high_resolution_clock::now();

    bool multiword = false;
    if(keywords.find(" ") != string::npos)
        multiword = true;

     keywords = strip(keywords);

    if( keywords.length() < 1)
        printf("Keyword is empty after calling strip(). Refusing to index.");
        return;

    keywords = lower(keywords);
    term.new_term = false;
    IndexTerm term;
    term.keywords = keywords;
    term.num_results = 0;
    term.num_pages = 0;

    query = "SELECT id, num_results, num_pages, date_indexed FROM dir_indexterm where keywords = " + keywords;
    nontransaction N(C);
    result R (N.exec(query.str()));
    N.commit();

    auto data = R[0];

    if( !data )
    {
        term.new_term = true;
    }

    // Store the num_pages if the previous index is found because it determines how many fields we will query.

    // printf("(Reindex) Term had {0} results and {1} pages last index on {2}".format(term.num_results, term.num_pages, term.date_indexed))

    query = GetPageTermQuery();

    nontransaction O(C);
    result S( O.exec( query.c_str() ));
    O.commit();
    std::list<std::pair<int, float>> ratings;
    for (result::const_iterator item = S.begin(); item != S.end(); ++item )
    {
        int weight = CalculateTermValue(item, keywords, "en");
        ratings.insert(weight, item.id);
    }
    term.num_pages = ratings.size();
    sort(ratings.begin(), ratings.end());
    if(ratings.size() > 5000)
    {
        ratings = std::list<std::pair<int, float>>(ratings.begin() + 1, ratings.end)
    }

    if( multiword )
    {
        ratings = AddIndividualWords(ratings, keywords, "en");
        if(ratings.size() > 5000)
        {
            ratings = std::list<std::pair<int, float>>(ratings.begin() + 1, ratings.end)
        }
    }

    term.page_rankings = ratings.toString();
    term.num_results = len(ratings);
    auto end = high_resolution_clock::now();
    auto elapsed = duration_cast<milliseconds>(end-start);
    term.index_time = elapsed / 1000.0;
    cout << "Indexing " << term << " took " << term.index_time << " seconds." << endl;
    auto jsonifystart = high_resolution_clock::now();
    term.saved = false;

    if( !new_term || term.num_pages > 0)
    {
        std::string individualwords = term.keywords.split(' ');
        int blocked = term_model.objects.filter(keywords__in=individualwords, actively_blocked=True).count()
        if(blocked > 0)
        {
            printf("Marking this term as blocked because at least one of the words in it is blocked.");
            term.actively_blocked = true;
        }
        // JsonifyIndexTerm needs to update rankings.
        term.JsonifyIndexTerm(term, "en");
        SaveTerm(term);
        term.saved = true;
    }
    else
    {
        printf("Not saving term because it does not have at least one result.");
    }

    auto jsonifyend = high_resolution_clock::now();
    auto jsonifyelapsed = duration_cast<milliseconds>(jsonifyend-jsonifystart);
    term.index_time = jsonifyelapsed / 1000.0;
    count << "Jsonify " << term << " took " << jsonifyelapsed / 1000.0 << " seconds." << endl;

    printf("Index Time for '%s': %f seconds, Jsonify Time: %f seconds (includes ranking update), %d pages, %d results.",
        term.keywords, term.index_time, jsonify_delta.total_seconds(), term.num_pages, term.num_results);

    return term.saved;
}

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

         BuildIndexForTerm(keywords);

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
