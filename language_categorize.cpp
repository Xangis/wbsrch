// Requires package libpqxx-dev.
//
// Build: g++ -std=c++11 -o language_categorize language_categorize.cpp -l pqxx
//
// Builds a list of all of the domains that have URLs ni the database and
// no language set for them.
#include <iostream>
#include <sstream>
#include <string>
#include <list>
#include <pqxx/pqxx>

using namespace std;
using namespace pqxx;

int main(int argc, char* argv[]) {
   try {
      connection C("dbname = zetaweb user = zetaweb password = d9irk0kfnv,er9kd2 \
      hostaddr = 45.56.74.154 port = 5432");
      if (C.is_open()) {
         cout << "Opened database successfully: " << C.dbname() << endl;
      } else {
         cout << "Can't open database" << endl;
         return 1;
      }
      connection D("dbname = zetaweb user = zetaweb password = d9irk0kfnv,er9kd2 \
      hostaddr = 45.56.74.154 port = 5432");
      //connection D("dbname = urls user = zetaweb password = d9irk0kfnv,er9kd2 \
      //hostaddr = 45.56.74.154 port = 5432");
      if (D.is_open()) {
         cout << "Opened database successfully: " << D.dbname() << endl;
      } else {
         cout << "Can't open database" << endl;
         return 1;
      }

      /* Create SQL statement */
      std::string sql("SELECT DISTINCT rooturl FROM site_info");

      /* Create a non-transactional object. */
      nontransaction N(C);
      nontransaction O(D);

      cout << "Executing: " << sql << endl;
      /* Execute SQL query */
      result R( N.exec( sql ));

      cout << R.size() << " rows selected from site_info." << endl;

      std::list<std::string> domains_to_check;

      /* Print all records */
      for (result::const_iterator c = R.begin(); c != R.end(); ++c) {
          std::string url = c[0].as<string>();

          // SELECT COUNT(DISTINCT rooturl_source) FROM dir_pagelink WHERE rooturl_destination = <URL>
          std::string sqltwo = std::string("SELECT url FROM dir_domaininfo WHERE url = '") + url + ("' AND (language_association IS NULL OR language_association = '')");
          //cout << "Executing: " << sqltwo << endl;
          result S( O.exec( sqltwo.c_str() ));
          const int num_rows = S.size();
          //cout << num_rows << " rows in dir_domaininfo for " << url << endl;
          if( num_rows == 0 ) {
              domains_to_check.push_back(url);
          } else {
              //cout << "Not adding already tagged site to check list." << endl;
          }
      }

      std::list<std::string>::iterator it;
      for( it = domains_to_check.begin(); it != domains_to_check.end(); it++ ) {
          cout << *it << endl;
      }
      C.disconnect ();
      D.disconnect ();
   } catch (const std::exception &e) {
      cerr << e.what() << std::endl;
      return 1;
   }

   return 0;
}
