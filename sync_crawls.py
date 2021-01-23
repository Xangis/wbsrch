# time python sync_crawls.py "dbname=zetaweb_addendum user=zetaweb password=password" "dbname=zetaweb user=zetaweb password=password"
# "dbname=urls_addendum user=urls password=password" "dbname=urls user=urls password=password" -p -d|tee sync_crawls_domains_2021-01-22.txt
import psycopg2
from psycopg2.extensions import AsIs
import argparse
#from dateutil.parser import parse

parser = argparse.ArgumentParser(description="Sync data between databases")
parser.add_argument('input', action='store', type=str, help='Input db, example: "dbname=suppliers user=postgres password=postgres"')
parser.add_argument('output', action='store', type=str, help='Output db, example: "dbname=zetaweb user=postgres password=postgres"')
parser.add_argument('inputurls', action='store', type=str, help='Input db, example: "dbname=suppliers user=postgres password=postgres"')
parser.add_argument('outputurls', action='store', type=str, help='Output db, example: "dbname=zetaweb user=postgres password=postgres"')
parser.add_argument('-p', '--nopages', default=False, action='store_true', dest='nopages', help='Do not update pages.')
parser.add_argument('-d', '--nodomains', default=False, action='store_true', dest='nodomains', help='Do not update domains.')
parser.add_argument('-u', '--nourls', default=False, action='store_true', dest='nourls', help='Do not update pending urls.')
options = parser.parse_args()

#
# SET UP DB CONNECTIONS
#
print('Input: ' + options.input)
print('Output: ' + options.output)
print('Inputurls: ' + options.inputurls)
print('Outputurls: ' + options.outputurls)

indb = psycopg2.connect(options.input)
outdb = psycopg2.connect(options.output)
inurldb = psycopg2.connect(options.inputurls)
outurldb = psycopg2.connect(options.outputurls)

incur = indb.cursor()
outcur = outdb.cursor()
inurlcur = inurldb.cursor()
outurlcur = outurldb.cursor()

incur.execute("SELECT version()")
outcur.execute("SELECT version()")

in_version = incur.fetchone()[0]
print('In Database Version: {0}'.format(in_version))

out_version = outcur.fetchone()[0]
print('Out Database Version: {0}'.format(out_version))


def SaveDomain(domain, update=False):
    columns = domain.keys()
    values = [domain[column] for column in columns]

    if not update:
        statement = 'INSERT INTO dir_domaininfo (%s) values %s'
        # print(outcur.mogrify(statement, (AsIs(','.join(columns)), tuple(values))))
        outcur.execute(statement, (AsIs(','.join(columns)), tuple(values)))
        outdb.commit()
    else:
        statement = 'UPDATE dir_domaininfo SET (%s) = (%s) WHERE id = %s'
        # print(outcur.mogrify(statement, (AsIs(','.join(columns)), tuple(values), domain['id'])))
        outcur.execute(statement, (AsIs(','.join(columns)), tuple(values)))
        outdb.commit()


def SavePage(page, update=False):
    columns = page.keys()
    values = [page[column] for column in columns]

    if not update:
        statement = 'INSERT INTO site_info (%s) values %s'
        print(outcur.mogrify(statement, (AsIs(','.join(columns)), tuple(values))))
    else:
        statement = 'UPDATE site_info SET (%s) = (%s) WHERE id = %s'
        # print(outcur.mogrify(statement, (AsIs(','.join(columns)), tuple(values), page['id'])))
        outcur.execute(statement, (AsIs(','.join(columns)), tuple(values)))
        outdb.commit()


def ProcessUnmatchedDomainFields(fields, existing_record):
    # existing_record contains the record as it is in the database.
    # fields contains source fields that differ.
    # Replace values in fields as necessary.
    # Update record in DB when needs_save = True.
    needs_save = False
    for item in fields.items():
        field = item[0]
        inval = item[1][0]
        outval = item[1][1]
        print('Field: {0}, Inval: {1}, Outval: {2}'.format(field, inval, outval))
        if field == 'robots_ip':
            # Don't bother comparing now, only compare if robots date is wrong.
            pass
        elif field == 'robots_last_updated':
            if 'robots_ip' in fields:
                if inval < outval:
                    print('Existing value is newer, not copying')
                else:
                    print('Input value is newer, copying over')
                    existing_record['robots_last_updated'] = inval
                    existing_record['robots_ip'] = fields['robots_ip'][0]
                    needs_save = True
            else:
                print('No robots_ip in mismatched fields, ignoring difference in robots_last_updated.')
        elif field == 'whois_last_updated':
            # If our data is newer, copy in all whois fields:
            # whois_address
            # whois_city
            # whois_country
            # whois_name
            # whois_registrar
            # whois_state
            # whois_zipcode
            # whois_emails
            # whois_nameservers
            # whois_org
            #
            # If a domain goes private or expires, we don't wan to delete previous data.
            # However, since None values are discarded before they ever reach this function,
            # this won't be a problem.
            if inval > outval:
                existing_record['whois_last_updated'] = fields['whois_last_udated'][0]
                if 'whois_address' in fields:
                    existing_record['whois_address'] = fields['whois_address'][0]
                if 'whois_city' in fields:
                    existing_record['whois_city'] = fields['whois_city'][0]
                if 'whois_country' in fields:
                    existing_record['whois_country'] = fields['whois_country'][0]
                if 'whois_name' in fields:
                    existing_record['whois_name'] = fields['whois_name'][0]
                if 'whois_registrar' in fields:
                    existing_record['whois_registrar'] = fields['whois_registrar'][0]
                if 'whois_state' in fields:
                    existing_record['whois_state'] = fields['whois_state'][0]
                if 'whois_zipcode' in fields:
                    existing_record['whois_zipcode'] = fields['whois_zipcode'][0]
                if 'whois_emails' in fields:
                    existing_record['whois_emails'] = fields['whois_emails'][0]
                if 'whois_nameservers' in fields:
                    existing_record['whois_nameservers'] = fields['whois_nameservers'][0]
                if 'whois_org' in fields:
                    existing_record['whois_org'] = fields['whois_org'][0]
                needs_save = True
            pass
        elif field == 'domain_created':
            if outval is None:
                existing_record['domain_ceated'] = inval
                needs_save = True
            else:
                raise ValueError('Input domain_created is {0} and output domain_created is {1} and we do not know what to do.'.format(inval, outval))
        elif field == 'domain_expires':
            if outval is None:
                existing_record['domain_expires'] = inval
                needs_save = True
            else:
                raise ValueError('Input domain_expires is {0} and output domain_expires is {1} and we do not know what to do.'.format(inval, outval))
        elif field == 'domain_updated':
            if outval is None:
                existing_record['domain_updated'] = inval
                needs_save = True
            else:
                raise ValueError('Input domain_updated is {0} and output domain_updated is {1} and we do not know what to do.'.format(inval, outval))
        elif field == 'whois_address':
            # Handled by whois_last_updated.
            pass
        elif field == 'whois_city':
            # Handled by whois_last_updated.
            pass
        elif field == 'whois_country':
            # Handled by whois_last_updated.
            pass
        elif field == 'whois_name':
            # Handled by whois_last_updated.
            pass
        elif field == 'whois_registrar':
            # Handled by whois_last_updated.
            pass
        elif field == 'whois_state':
            # Handled by whois_last_updated.
            pass
        elif field == 'whois_zipcode':
            # Handled by whois_last_updated.
            pass
        elif field == 'whois_emails':
            # Handled by whois_last_updated.
            pass
        elif field == 'whois_nameservers':
            # Handled by whois_last_updated.
            pass
        elif field == 'whois_org':
            # Handled by whois_last_updated.
            pass
        else:
            raise ValueError(field)
    print('ProcessUnmatchedDomainFields: Save = {0}'.format(needs_save))
    if needs_save:
        SaveDomain(existing_record, update=True)
        return True
    else:
        return False


def ProcessUnmatchedPageFields(fields, existing_record):
    # existing_record contains the record as it is in the database.
    # fields contains source fields that differ.
    needs_save = False
    for item in fields.items():
        field = item[0]
        inval = item[1][0]
        outval = item[1][1]
        print('Field: {0}, Inval: {1}, Outval: {2}'.format(field, inval, outval))
        if field == 'firstcrawled':
            if inval < outval:
                print('Input value was crawled earlier, copying over.')
                existing_record['firstcrawled'] = inval
                needs_save = True
            else:
                print('Existing value was crawled earlier, not copying.')
        elif field == 'lastcrawled':
            if inval > outval:
                print('Input value was crawled more recently, copying over.')
                if 'pagetext' in fields:
                    existing_record['lastcrawled'] = inval
                    existing_record['pagetext'] = fields['pagetext'][0]
                    # If it didn't change, we don't care. If it went from something to
                    # nothing there will be a delta.
                    if 'pagetitle' in fields:
                        existing_record['pagetitle'] = fields['pagetitle'][0]
                    if 'pagecontents' in fields:
                        existing_record['pagecontents'] = fields['pagecontents'][0]
                    if 'pagesize' in fields:
                        existing_record['pagesize'] = fields['pagesize'][0]
                    if 'server_header' in fields:
                        existing_record['server_header'] = fields['server_header'][0]
                    if 'num_javascripts' in fields:
                        existing_record['num_javascripts'] = fields['num_javascripts'][0]
                        print('TODO: Copy javascript entries from urls table')
                    needs_save = True
                else:
                    print('No pagetext in fields, cannot copy it over.')
            else:
                print('Existing value was crawled more recently, not copying.')
        elif field == 'pagetext':
            # Don't bother comparing now, only if lastcrawled is newer.
            pass
        elif field == 'pagetitle':
            # Don't bother comparing now, only if lastcrawled is newer.
            pass
        elif field == 'pagecontents':
            # Don't bother comparing now, only if lastcrawled is newer.
            pass
        elif field == 'pagesize':
            # Don't bother comparing now, only if lastcrawled is newer.
            pass
        elif field == 'num_javascripts':
            # Don't bother comparing now, only if lastcrawled is newer.
            pass
        elif field == 'server_header':
            # Don't bother comparing now, only if lastcrawled is newer.
            pass
        else:
            raise ValueError(field)
    print('ProcessUnmatchedPageFields: Save = {0}'.format(needs_save))
    if needs_save:
        SavePage(existing_record, update=True)


if not options.nodomains:
    #
    # Here we do domains.
    #
    print('--- PROCESSING DOMAINS ---')

    incur.execute("SELECT * FROM dir_domaininfo")
    print('Number of dir_domaininfo: {0}'.format(incur.rowcount))

    colnames = [desc[0] for desc in incur.description]
    # print(colnames)

    existing_query = 'SELECT * FROM dir_domaininfo WHERE URL = %s'

    # We ignore calculated columns and columsn imported by other means.
    ignored_columns = ['id', 'majestic_rank', 'majestic_outdated', 'majestic_refsubnets',
    'majestic_rank_date', 'alexa_rank', 'alexa_outdated', 'domains_linking_in', 'domains_linking_in_last_updated',
    'alexa_rank_date', 'quantcast_rank', 'quantcast_rank_date', 'quantcast_outdated',
    'domcop_rank', 'domcop_pagerank', 'domcop_pagerank_outdated', 'domcop_pagerank_date']

    new = 0
    updated = 0
    notupdated = 0
    row = incur.fetchone()
    while row is not None:
        unmatched_fields = {}
        # print(row)
        url = row[1]
        outcur.execute(existing_query, (url,))
        num_existing = outcur.rowcount
        if num_existing > 0:
            existing_record = {}
            print('The domain {0} already exists in the output database.'.format(url))
            existing_row = outcur.fetchone()
            existing_colnames = [desc[0] for desc in outcur.description]
            # print(existing_colnames)
            colpos = {}
            for index in range(len(colnames)):
                colpos[colnames[index]] = index
            for index in range(len(existing_row)):
                # print('Existing column {0} ({1}) is {2} in source'.format(index, existing_colnames[index], colpos[existing_colnames[index]]))
                inval = row[colpos[existing_colnames[index]]]
                outval = existing_row[index]
                existing_record[existing_colnames[index]] = existing_row[index]
                if existing_colnames[index] in ignored_columns:
                    # print('Ignoring column {0}'.format(existing_colnames[index]))
                    pass
                elif inval is None:
                    # print('Empty input value for {0}, skipping'.format(existing_colnames[index]))
                    pass
                elif inval != outval:
                    # print('Field {0} ({1}) does not match. Input: {2}, Output: {3}'.format(existing_colnames[index], index, inval, outval))
                    unmatched_fields[existing_colnames[index]] = (inval, outval)
            if ProcessUnmatchedDomainFields(unmatched_fields, existing_record):
                updated += 1
            else:
                notupdated += 1
        else:
            print('The domain {0} is new.'.format(url))
            record = {}
            for index in range(len(row)):
                if colnames[index] != 'id':
                    record[colnames[index]] = row[index]
            SaveDomain(record)
            new += 1
        row = incur.fetchone()

    print('--- END PROCESSING DOMAINS ---\n')
    print('{0} existed and were updated, {1} existed and were not updated, {2} were newly added'.format(updated, notupdated, new))
    print('------------------------------\n')


if not options.nopages:
    #
    # Here we do pages.
    #
    print('--- PROCESSING PAGES ---')

    incur.execute("SELECT * FROM site_info")
    print('Number of site_info: {0}'.format(incur.rowcount))

    # 31 columns:
    # ['id', 'rooturl', 'url', 'pagetitle', 'pagedescription', 'pagefirstheadtag', 'pagefirsth2tag', 'pagefirsth3tag', 'pagekeywords', 'pagecontents',
    #  'pagetext', 'pagesize', 'lastcrawled', 'firstcrawled', 'ip', 'num_errors', 'error_info', 'server_header', 'content_type_header', 'num_css_files',
    #  'num_images', 'num_javascripts', 'num_iframes', 'num_audio_tags', 'num_video_tags', 'num_svg_tags', 'num_canvas_tags', 'image_alt_tags', 'image_title_tags', 'image_filenames',
    #  'simhash_value']
    colnames = [desc[0] for desc in incur.description]
    # print(colnames)

    existing_query = 'SELECT * FROM site_info WHERE URL = %s'

    ignored_columns = ['id', 'simhash_value']

    updated = 0
    notupdated = 0
    new = 0
    row = incur.fetchone()
    while row is not None:
        unmatched_fields = {}
        # print(row)
        url = row[2]
        outcur.execute(existing_query, (url,))
        num_existing = outcur.rowcount
        if num_existing > 0:
            existing_record = {}
            print('The url {0} already exists in the output database.'.format(url))
            existing_row = outcur.fetchone()
            existing_colnames = [desc[0] for desc in outcur.description]
            # print(existing_colnames)
            colpos = {}
            for index in range(len(colnames)):
                colpos[colnames[index]] = index
            for index in range(len(existing_row)):
                # print('Existing column {0} ({1}) is {2} in source'.format(index, existing_colnames[index], colpos[existing_colnames[index]]))
                inval = row[colpos[existing_colnames[index]]]
                outval = existing_row[index]
                existing_record[existing_colnames[index]] = existing_row[index]
                if existing_colnames[index] in ignored_columns:
                    # print('Ignoring column {0}'.format(existing_colnames[index]))
                    pass
                elif inval is None:
                    # print('Empty input value for {0}, skipping'.format(existing_colnames[index]))
                    pass
                elif inval != outval:
                    # print('Field {0} ({1}) does not match. Input: {2}, Output: {3}'.format(existing_colnames[index], index, inval, outval))
                    unmatched_fields[existing_colnames[index]] = (inval, outval)
            ProcessUnmatchedPageFields(unmatched_fields, existing_record)
        else:
            print('The url {0} is new.'.format(url))
            record = {}
            for index in range(len(row)):
                if colnames[index] != 'id':
                    record[colnames[index]] = row[index]
            SavePage(record)
        row = incur.fetchone()

        print('--- END PROCESSING DOMAINS ---\n')
        print('{0} existed and were updated, {1} existed and were not updated, {2} were newly added'.format(updated, notupdated, new))
        print('------------------------------\n')


if not options.nourls:
    #
    # Here we do pending urls.
    #
    print('--- PROCESSING PENDING URLS ---')

    inurlcur.execute("SELECT * FROM dir_crawlableurl")
    print('Number of dir_crawlableurl: {0}'.format(inurlcur.rowcount))

    updated = 0
    alreadycrawled = 0
    alreadypending = 0
    new = 0
    row = inurlcur.fetchone()
    while row is not None:
        print(row)
        url = row[2]
        existing_url_query = 'SELECT * FROM site_info WHERE URL = %s'
        outcur.execute(existing_url_query, (url,))
        num_existing = outcur.rowcount
        if num_existing > 0:
            alreadycrawled += 1
            row = inurlcur.fetchone()
            continue
        existing_crawlableurl_query = 'SELECT * FROM dir_crawlableurl WHERE URL = %s'
        outurlcur.execute(existing_crawlableurl_query, (url,))
        num_existing = outcur.rowcount
        if num_existing > 0:
            alreadypending += 1
            row = inurlcur.fetchone()
            continue

        print('The url {0} is new.'.format(url))
        new += 1
        insert_query = "INSERT INTO dir_crawlableurl (rooturl, url, randval) VALUES (%s, %s, %s)"
        print(outurlcur.mogrify(insert_query, (row[1], row[2], row[3])))
        #outcur.execute(insert_query, (row[0], row[1], row[2]))
        #outdb.commit()
        row = inurlcur.fetchone()

    print('--- END PROCESSING PENDING URLS ---\n')
    print('{0} were already crawled, {1} were already pending, {2} were newly added'.format(alreadycrawled, alreadypending, new))
    print('-----------------------------------\n')


incur.close()
outcur.close()
inurlcur.close()
outurlcur.close()
