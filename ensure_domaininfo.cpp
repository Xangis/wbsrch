// Requires package libpqxx-dev.
//
// Build: g++ -std=c++11 -o ensure_domaininfo ensure_domaininfo.cpp -l pqxx
//
// Compared to the Python version, this uses 8MB for 10,000 domains updated in a batch vs.
// Python's 130MB.
#include <iostream>
#include <sstream>
#include <string>
#include <pqxx/pqxx>

using namespace std;
using namespace pqxx;

int main(int argc, char* argv[]) {
   if( argc < 3 ) {
     cout << "This program requires 2 arguments: number of items to process and offset. Try 10000 and 0. If any third argument is supplied it will log results." << endl;
     exit(1);
   }
   stringstream sql;
   int numitems = atoi(argv[1]);
   int offset = atoi(argv[2]);
   bool log = false;
   if( argc > 3 ) {
       log = true;
   }

   try {
      connection C("dbname = zetaweb user = zetaweb password = password \
      hostaddr = 127.0.0.1 port = 5432");
      if (C.is_open()) {
         cout << "Opened database zetaweb successfully: " << C.dbname() << endl;
      } else {
         cout << "Can't open database" << endl;
         return 1;
      }
      connection D("dbname = indexes user = indexes password = password \
      hostaddr = 127.0.0.1 port = 5432");
      if (D.is_open()) {
         cout << "Opened database indexes successfully: " << D.dbname() << endl;
      } else {
         cout << "Can't open database" << endl;
         return 1;
      }

      /* Create SQL statement */
      sql << "SELECT id, rooturl FROM site_info WHERE rooturl ILIKE '%.%' ORDER BY rooturl LIMIT ";
      sql << numitems << " OFFSET " << offset;

      /* Create a non-transactional object. */
      nontransaction N(C);

      // cout << "Executing: " << sql.str() << endl;
      /* Execute SQL query */
      result R( N.exec( sql.str() ));
      N.commit();

      /* Print all records */
      int count = 0;
      int processed = 0;
      cout << "Pages retrieved. Checking for DomainInfo entries." << endl;
      for (result::const_iterator c = R.begin(); c != R.end(); ++c)
      {
         int id = c[0].as<int>();

         std::string url = c[1].as<string>();

         std::string sqltwo("SELECT COUNT(url) FROM dir_domaininfo WHERE url = '");
         sqltwo = sqltwo + url + std::string("'");

         // cout << "Executing: " << sqltwo << endl;

         nontransaction O(D);
         result S( O.exec( sqltwo.c_str() ));
         O.commit();
         for (result::const_iterator d = S.begin(); d != S.end(); ++d) {
             int value = d[0].as<int>();
             // cout << "Domains Found: " << value << endl;
             if(value < 1)
             {
                 // cout << "Adding " << url << " to database " << endl;
                 // insert into dir_domaininfo (url, rank_adjustment, alexa_outdated, uses_language_subdirs, uses_language_query_parameter,
                 // uses_langid, is_unblockable, verified_notporn, majestic_outdated, only_crawl_rooturl, domcop_pagerank_outdated, quantcast_outdated) values
                 // ('pants.pants', 0, true, false, false, false, false, false, false, false, false, false);
                 std::string sqlthree("INSERT INTO dir_domaininfo (url, rank_adjustment, alexa_outdated, uses_language_subdirs, uses_language_query_parameter, uses_langid, is_unblockable, verified_notporn, majestic_outdated, only_crawl_rooturl, domcop_pagerank_outdated, quantcast_outdated) values('");
                 sqlthree = sqlthree + url + "', 0, true, false, false, false, false, false, false, false, false, false)";
                 count += 1;
                 // cout << "Executing: " << sqlthree << endl;
                 if( log ) {
                     cout << "Added domain " << url << endl;
                 }
                 nontransaction P(D);
                 result T( P.exec( sqlthree.c_str() ));
                 P.commit();
             }
             processed += 1;
             if( processed % 10000 == 0)
             {
                 cout << processed << " domains processed." << endl;
             }
         }
      }
      cout << "Operation done successfully. " << count << " domains added." << endl;
      C.disconnect ();
      D.disconnect ();
   } catch (const std::exception &e) {
      cerr << e.what() << std::endl;
      return 1;
   }

   return 0;
}
