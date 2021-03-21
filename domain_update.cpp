// Requires package libpqxx-dev.
//
// Build: g++ -std=c++11 -o domain_update domain_update.cpp -l pqxx
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
     cout << "This program requires 2 arguments: number of items to process and offset. Try 10000 and 0. If any third argument is supplied, it will recalculate old rather than new." << endl;
     exit(1);
   }
   stringstream sql;
   int numitems = atoi(argv[1]);
   int offset = atoi(argv[2]);
   bool redo = false;
   if( argc > 3 ) {
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
      connection D("dbname = urls user = urls password = 'fd=dgsm=fe~td4=3' \
      hostaddr = 216.151.2.52 port = 5432");
      if (D.is_open()) {
         cout << "Opened database successfully: " << D.dbname() << endl;
      } else {
         cout << "Can't open database" << endl;
         return 1;
      }
      connection E("dbname = indexes user = indexes password = 'jsanvsiuyeh8u8m3' \
      hostaddr = 216.151.2.50 port = 5432");
      if (E.is_open()) {
         cout << "Opened database successfully: " << E.dbname() << endl;
      } else {
         cout << "Can't open database" << endl;
         return 1;
      }

      // We don't actually need any fields other than ID and URL since we're not doing anything with the old values.
      if (!redo ) {
          sql << "SELECT id, url, alexa_rank, domains_linking_in, domains_linking_in_last_updated, num_urls, num_urls_last_updated FROM dir_domaininfo WHERE domains_linking_in_last_updated IS NULL LIMIT ";
      } else {
          sql << "SELECT id, url, alexa_rank, domains_linking_in, domains_linking_in_last_updated, num_urls, num_urls_last_updated FROM dir_domaininfo WHERE domains_linking_in_last_updated IS NOT NULL ORDER BY domains_linking_in_last_updated LIMIT ";
      }
      sql << numitems << " OFFSET " << offset;

      /* Create a non-transactional object. */
      nontransaction N(C);
      nontransaction O(D);
      nontransaction P(E);

      cout << "Executing: " << sql.str() << endl;
      /* Execute SQL query */
      result R( N.exec( sql.str() ));

      /* Print all records */
      int count = 0;
      for (result::const_iterator c = R.begin(); c != R.end(); ++c) {
         int id = c[0].as<int>();
         std::string url = c[1].as<string>();

         // Update number of domains linking in.
         std::string sqltwo("SELECT COUNT(DISTINCT rooturl_source) FROM dir_pagelink WHERE rooturl_destination = '");
         sqltwo = sqltwo + url + std::string("'");
         result S( O.exec( sqltwo.c_str() ));
         for (result::const_iterator d = S.begin(); d != S.end(); ++d) {
             int value = d[0].as<int>();
             cout << value << " domains linking in for " << url << endl;
             std::string sqlthree("UPDATE dir_domaininfo SET domains_linking_in = ");
             sqlthree = sqlthree + std::to_string(value) + ", domains_linking_in_last_updated = current_timestamp WHERE ID = " + std::to_string(id);
             count += 1;
             result T( N.exec( sqlthree.c_str() ));
         }

         // Update num pages in index.
         std::string sqlfour("SELECT COUNT(rooturl) FROM site_info WHERE rooturl = '");
         sqlfour = sqlfour + url + std::string("'");
         result U( N.exec( sqlfour.c_str() ));
         for (result::const_iterator e = U.begin(); e != U.end(); ++e) {
             int value = e[0].as<int>();
             cout << value << " pages in index for " << url  << endl;
             std::string sqlfive("UPDATE dir_domaininfo SET num_urls = ");
             sqlfive = sqlfive + std::to_string(value) + ", num_urls_last_updated = current_timestamp WHERE ID = " + std::to_string(id);
             result T( N.exec( sqlfive.c_str() ));
         }

         // Update number of keywords ranked.
         std::string sqlsix("SELECT COUNT(rooturl) FROM dir_keywordranking WHERE rooturl = '");
         sqlsix = sqlsix + url + std::string("'");
         result V( P.exec( sqlsix.c_str() ));
         for (result::const_iterator f = V.begin(); f != V.end(); ++f) {
             int value = f[0].as<int>();
             cout << value << " keywords ranked for " << url  << endl;
             std::string sqlseven("UPDATE dir_domaininfo SET num_keywords_ranked = ");
             sqlseven = sqlseven + std::to_string(value) + ", num_keywords_last_updated = current_timestamp, last_updated = current_timestamp WHERE ID = " + std::to_string(id);
             result T( N.exec( sqlseven.c_str() ));
         }
      }
      cout << "Operation done successfully. " << count << " domains updated." << endl;
      C.disconnect ();
      D.disconnect();
   } catch (const std::exception &e) {
      cerr << e.what() << std::endl;
      return 1;
   }

   return 0;
}
