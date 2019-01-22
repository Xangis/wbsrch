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
     cout << "This program requires 2 arguments: number of items to process and offset. Try 10000 and 0." << endl;
     exit(1);
   }
   stringstream sql;
   int numitems = atoi(argv[1]);
   int offset = atoi(argv[2]);

   try {
      connection C("dbname = zetaweb user = zetaweb password = d9irk0kfnv,er9kd2 \
      hostaddr = 127.0.0.1 port = 5432");
      if (C.is_open()) {
         cout << "Opened database successfully: " << C.dbname() << endl;
      } else {
         cout << "Can't open database" << endl;
         return 1;
      }
      connection D("dbname = urls user = zetaweb password = d9irk0kfnv,er9kd2 \
      hostaddr = 45.33.19.243 port = 5432");
      if (D.is_open()) {
         cout << "Opened database successfully: " << D.dbname() << endl;
      } else {
         cout << "Can't open database" << endl;
         return 1;
      }

      /* Create SQL statement */
      //sql = "SELECT id, url, alexa_rank, domains_linking_in, domains_linking_in_last_updated, num_keywords_ranked, num_keywords_last_updated, num_urls, num_urls_last_updated FROM dir_domaininfo WHERE domains_linking_in_last_updated IS NULL ORDER BY alexa_rank LIMIT 100000";
      //sql = "SELECT id, url, alexa_rank, domains_linking_in, domains_linking_in_last_updated FROM dir_domaininfo WHERE domains_linking_in_last_updated IS NULL ORDER BY alexa_rank LIMIT 100000";
      sql << "SELECT id, url, alexa_rank, domains_linking_in, domains_linking_in_last_updated FROM dir_domaininfo WHERE domains_linking_in_last_updated IS NULL LIMIT ";
      sql << numitems << " OFFSET " << offset;

      /* Create a non-transactional object. */
      nontransaction N(C);
      nontransaction O(D);

      cout << "Executing: " << sql.str() << endl;
      /* Execute SQL query */
      result R( N.exec( sql.str() ));

      /*
 id                              | integer                  | not null default nextval('dir_domaininfo_id_seq'::regclass)
 url                             | character varying(255)   | not null
 language_association            | character varying(8)     | 
 notes                           | text                     | 
 rank_adjustment                 | integer                  | not null
 rank_reason                     | integer                  | 
 alexa_rank                      | integer                  | 
 alexa_rank_date                 | date                     | 
 alexa_outdated                  | boolean                  | not null
 uses_language_subdirs           | boolean                  | not null
 uses_language_query_parameter   | boolean                  | not null
 uses_langid                     | boolean                  | not null
 max_urls                        | integer                  | 
 is_unblockable                  | boolean                  | not null
 domain_created                  | timestamp with time zone | 
 domain_expires                  | timestamp with time zone | 
 whois_last_updated              | timestamp with time zone | 
 robots_ip                       | character varying(16)    | 
 robots_txt                      | text                     | 
 robots_last_updated             | timestamp with time zone | 
 domains_linking_in              | integer                  | 
 domains_linking_in_last_updated | timestamp with time zone | 
 verified_notporn                | boolean                  | not null
 only_crawl_rooturl              | boolean                  | not null
 num_keywords_last_updated       | date                     | 
 num_keywords_ranked             | integer                  | 
 num_urls                        | integer                  | 
 num_urls_last_updated           | date                     | 
 whois_address                   | character varying(80)    | 
 whois_city                      | character varying(40)    | 
 whois_country                   | character varying(16)    | 
 whois_name                      | character varying(60)    | 
 whois_org                       | character varying(60)    | 
 whois_registrar                 | character varying(60)    | 
 whois_state                     | character varying(10)    | 
 whois_zipcode                   | character varying(8)     | 
 domain_updated                  | timestamp with time zone | 
 whois_emails                    | text                     | 
 whois_nameservers               | text                     | 
      */


/*
            if urlcounts:
                num_urls = PageLink.objects.filter(rooturl_destination=domain.url).values('rooturl_source').distinct().count()
                print u'{0} urls crawled for {1}'.format(num_urls, domain.url)
                domain.num_urls = num_urls
                domain.num_urls_last_updated = timezone.now()
            elif keywordcounts:
                num_keywords_ranked = PageLink.objects.filter(rooturl_destination=domain.url).values('rooturl_source').distinct().count()
                print u'{0} keywords ranked for {1}'.format(num_keywords_ranked, domain.url)
                domain.nuM_keywords_ranked = num_keywords_ranked
                domain.num_keywords_ranked_last_updated = timezone.now()
            else:
                num_domains_linking_in = PageLink.objects.filter(rooturl_destination=domain.url).values('rooturl_source').distinct().count()
                print u'{0} incoming links for {1}'.format(num_domains_linking_in, domain.url)
                domain.domains_linking_in = num_domains_linking_in
                domain.domains_linking_in_last_updated = timezone.now()
            domain.save()
            if sleeptime:
                time.sleep(sleeptime)
        updated = domains.count()
        elapsed = timezone.now() - start
        if total:
            nototal = DomainInfo.objects.filter(domains_linking_in_last_updated__isnull=True).count()
            print u'{0} domains still do not have link count information.'.format(nototal)
        print u'{0} domains updated in {1} seconds.'.format(updated, elapsed.total_seconds())
*/

      /* Print all records */
      for (result::const_iterator c = R.begin(); c != R.end(); ++c) {
         int id = c[0].as<int>();
         //cout << "ID = " << id << endl;
         std::string url = c[1].as<string>();
         //cout << "Url = " << url << endl;
         //if( !c[2].is_null() )
         //cout << "alexa_rank = " << c[2].as<string>() << endl;
         //if( !c[3].is_null() )
         //cout << "domains_linking_in = " << c[3].as<int>() << endl;
         //if( !c[4].is_null() )
         //cout << "domains_linking_in_last_updated = " << c[4].as<string>() << endl;
         //if( !c[5].is_null() )
         //cout << "num_keywords = " << c[3].as<int>() << endl;
         //if( !c[6].is_null() )
         //cout << "num_keywords_last_updated = " << c[4].as<string>() << endl;
         //if( !c[7].is_null() )
         //cout << "num_urls = " << c[3].as<int>() << endl;
         //if( !c[8].is_null() )
         //cout << "num_urls_last_updated = " << c[4].as<string>() << endl;

         // SELECT COUNT(DISTINCT rooturl_source) FROM dir_pagelink WHERE rooturl_destination = <URL>
         std::string sqltwo("SELECT COUNT(DISTINCT rooturl_source) FROM dir_pagelink WHERE rooturl_destination = '");
         sqltwo = sqltwo + url + std::string("'");
         //cout << sqltwo << endl;
         //nontransaction U(C);
         //result S( U.exec( sqltwo.c_str() ));
         result S( O.exec( sqltwo.c_str() ));
         for (result::const_iterator d = S.begin(); d != S.end(); ++d) {
             int value = d[0].as<int>();
             cout << value << " domains linking in for " << url << endl;
             // UPDATE dir_domaininfo SET domains_linking_in = value, domains_linking_in_last_updated = current_timestamp WHERE ID = id;
             std::string sqlthree("UPDATE dir_domaininfo SET domains_linking_in = ");
             sqlthree = sqlthree + std::to_string(value) + ", domains_linking_in_last_updated = current_timestamp WHERE ID = " + std::to_string(id);
             //cout << sqlthree << endl;
             result T( N.exec( sqlthree.c_str() ));
             //for (result::const_iterator e = T.begin(); e != T.end(); ++e) {
             //    cout << "Update result = " << e[0].as<string>() << endl;
             //}
         }
         // SELECT COUNT(DISTINCT rooturl_source) FROM dir_pagelink WHERE rooturl_destination = <URL>
         // SELECT COUNT(DISTINCT rooturl_source) FROM dir_pagelink WHERE rooturl_destination = <URL>
      }
      cout << "Operation done successfully" << endl;
      C.disconnect ();
   } catch (const std::exception &e) {
      cerr << e.what() << std::endl;
      return 1;
   }

   return 0;
}
