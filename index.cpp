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
#include <regex>
#include <vector>
//#include <tuple>
//#include <format.h>
#include <pqxx/pqxx>
//#include <pqxx/result.hxx>

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

string replace( string const & in, string const & from, string const & to )
{
  return std::regex_replace( in, std::regex(from), to );
}

vector<string> split(string const &in, char splitchar)
{
    vector<string> strings;
    istringstream f(in);
    string s;    
    while (getline(f, s, splitchar)) {
        cout << s << endl;
        strings.push_back(s);
    }
    return strings;
}

std::string removeAccented( const char* str ) {
    const char*
    //   "ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ"
    tr = "AAAAAAECEEEEIIIIDNOOOOOx0UUUUYPsaaaaaaeceeeeiiiiOnooooo/0uuuuypy";
    std::string out;
    int slen = strlen(str);
    for( int i = 0; i < slen; i++ )
    {
        unsigned char ch = (unsigned char)str[i];
        if ( ch >=192 ) {
            ch = tr[ ch-192 ];
        }
        out += (char)ch;
    }
    return str;
}

std::string GetPageTermQuery(IndexTerm term)
{
    std::string spacelesskeywords = replace(term.keywords, std::string(" "), std::string("%"));
    std::string asciikeywords = std::string(removeAccented(spacelesskeywords.c_str()));
    if( spacelesskeywords != asciikeywords )
        cout << "Checking URL as " << asciikeywords << endl;
    std::string akp = '%' + asciikeywords + '%';
    std::string sql_query;
    if( term.num_pages > 100000 )
        sql_query = std::string("SELECT id, rooturl, url, pagetitle, pagedescription, pagefirstheadtag, pagekeywords, pagetext, pagesize FROM site_info WHERE (pagetitle ILIKE {} OR url ILIKE {} OR pagefirstheadtag ILIKE {}) LIMIT 1000000");
    else if( term.num_pages > 40000 )
        sql_query = std::string("SELECT id, rooturl, url, pagetitle, pagedescription, pagefirstheadtag, pagekeywords, pagetext, pagesize FROM site_info WHERE (pagetitle ILIKE %s OR url ILIKE %s OR pagefirstheadtag ILIKE %s OR pagefirsth2tag ILIKE %s) LIMIT 1000000");
    else if( term.num_pages > 10000 )
        sql_query = std::string("SELECT id, rooturl, url, pagetitle, pagedescription, pagefirstheadtag, pagekeywords, pagetext, pagesize FROM site_info WHERE (pagetitle ILIKE %s OR url ILIKE %s OR pagefirstheadtag ILIKE %s OR pagefirsth2tag ILIKE %s OR pagefirsth3tag ILIKE %s) LIMIT 1000000");
    else if( term.num_pages > 3000 )
        sql_query = std::string("SELECT id, rooturl, url, pagetitle, pagedescription, pagefirstheadtag, pagekeywords, pagetext, pagesize FROM site_info WHERE (pagetitle ILIKE %s OR pagekeywords LIKE %s OR pagedescription ILIKE %s OR url ILIKE %s OR pagefirstheadtag ILIKE %s OR pagefirsth2tag ILIKE %s OR pagefirsth3tag ILIKE %s) LIMIT 1000000");
    else
        sql_query = std::string("SELECT id, rooturl, url, pagetitle, pagedescription, pagefirstheadtag, pagekeywords, pagetext, pagesize FROM site_info WHERE (pagetitle ILIKE %s OR pagekeywords LIKE %s OR pagedescription ILIKE %s OR pagetext ILIKE %s OR url ILIKE %s OR pagefirstheadtag ILIKE %s OR pagefirsth2tag ILIKE %s OR pagefirsth3tag ILIKE %s) LIMIT 1000000");
    return sql_query;
}

list<std::pair<float, int>> AddIndividualWords(list<std::pair<float, int>> ratings, std::string keywords, std::string language)
{
    return ratings;
}

float CalculateTermValue(std::vector<std::string> rowdata, std::string keywords, std::string language)
{
    return 0.0;
}

std::string GetPageTermQuery(std::string query)
{
    return query;
}

bool JsonifyIndexTerm(IndexTerm term, std::string language)
{
    return true;
}

bool SaveTerm(IndexTerm term)
{
    return true;
}

bool BuildIndexForTerm(std::string keywords, connection* C)
{
    if( keywords.empty() )
    {
        return false;
    }
    cout << "Indexing " << keywords << endl;
    auto start = high_resolution_clock::now();

    bool multiword = false;
    if(keywords.find(" ") != string::npos)
        multiword = true;

     keywords = strip(keywords);

    if( keywords.length() < 1)
        printf("Keyword is empty after calling strip(). Refusing to index.");
        return false;

    keywords = lower(keywords);
    IndexTerm term;
    term.new_term = false;
    term.keywords = keywords;
    term.num_results = 0;
    term.num_pages = 0;

    std::string query = "SELECT id, num_results, num_pages, date_indexed FROM dir_indexterm where keywords = " + keywords;
    nontransaction N(*C);
    result R (N.exec(query.c_str()));
    N.commit();

    if( R.size() < 1 )
    {
        term.new_term = true;
    }

    // Store the num_pages if the previous index is found because it determines how many fields we will query.

    // printf("(Reindex) Term had {0} results and {1} pages last index on {2}".format(term.num_results, term.num_pages, term.date_indexed))

    query = GetPageTermQuery(term);

    nontransaction O(*C);
    result S( O.exec( query.c_str() ));
    O.commit();
    std::list<std::pair<float, int>> ratings;
    for (result::const_iterator row = S.begin(); row != S.end(); ++row )
    {
        int id = row[0].as<int>();
        std::vector<std::string> rowdata;
        for(pqxx::row::iterator field = row.begin(); field != row.end(); ++field)
        {
            rowdata.push_back(field.c_str());
        }
        float weight = CalculateTermValue(rowdata, keywords, "en");
        ratings.push_back(std::pair<float, int>(weight, id));
    }
    term.num_pages = ratings.size();
    ratings.sort();
    if(ratings.size() > 5000)
    {
        cout << "TODO: Write a slice function to trim ratings down to 5000" << endl;
        //ratings = std::list<std::pair<int, float>>(ratings.begin() + 1, ratings.end)
    }

    if( multiword )
    {
        ratings = AddIndividualWords(ratings, keywords, "en");
        if(ratings.size() > 5000)
        {
            cout << "TODO: Write a slice function to trim ratings down to 5000" << endl;
            //ratings = std::list<std::pair<int, float>>(ratings.begin() + 1, ratings.end)
        }
    }

    std::string encoded_rankings = std::string("[");
    bool first = true;
    for( std::list<std::pair<float, int>>::iterator i = ratings.begin(); i != ratings.end(); i++)
    {
        if( !first )
        {
            encoded_rankings += ", ";
        }
        encoded_rankings += std::string("[") + std::to_string((*i).first) + ", " + std::to_string((*i).second) + std::string("]");
        first = false;
    }
    encoded_rankings += "]";

    term.page_rankings = encoded_rankings;
    // [[775416, 12.0], [752310, 12.0], [1073551, 10.0], [1068168, 7.5], [556956, 4.0]]
    term.num_results = ratings.size();
    auto end = high_resolution_clock::now();
    auto elapsed = duration_cast<milliseconds>(end-start);
    term.index_time = elapsed.count() / 1000.0;
    cout << "Indexing " << term.keywords << " took " << term.index_time << " seconds." << endl;
    auto jsonifystart = high_resolution_clock::now();
    term.saved = false;

    if( !term.new_term || term.num_pages > 0)
    {
        std::vector<std::string> individualwords = split(term.keywords, ' ');
        std::string blockedquery = "SELECT COUNT(*) FROM dir_indexterm WHERE actively_blocked = true AND keywords in (%s)";
        result S( O.exec( blockedquery.c_str() ));
        O.commit();
        // TODO: Get count from result.
        if(term.actively_blocked > 0)
        {
            printf("Marking this term as blocked because at least one of the words in it is blocked.");
            term.actively_blocked = true;
        }
        // JsonifyIndexTerm needs to update rankings.
        JsonifyIndexTerm(term, "en");
        SaveTerm(term);
        term.saved = true;
    }
    else
    {
        printf("Not saving term because it does not have at least one result.");
    }

    auto jsonifyend = high_resolution_clock::now();
    auto jsonifyelapsed = duration_cast<milliseconds>(jsonifyend-jsonifystart);
    float jsonifyseconds = jsonifyelapsed.count() / 1000.0;
    cout << "Jsonify " << term.keywords << " took " << jsonifyseconds << " seconds." << endl;

    cout << "Index Time for '" << term.keywords << "': " << term.index_time << " seconds, Jsonify Time: " <<
            jsonifyseconds << " seconds (includes ranking update), " << term.num_pages << " pages, " <<
            term.num_results << " results." << endl;

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
      connection C("dbname = zetaweb user = zetaweb password = '.vasd,f.ef,,.dii.' \
      hostaddr = 216.151.2.54 port = 5432");
      if (C.is_open()) {
         cout << "Opened database successfully: " << C.dbname() << endl;
      } else {
         cout << "Can't open database" << endl;
         return 1;
      }

      connection D("dbname = indexes user = indexes password = 'jsanvsiuyeh8u8m3' \
      hostaddr = 216.151.2.50 port = 5432");
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

         BuildIndexForTerm(keywords, &C);

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
