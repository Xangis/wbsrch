import psycopg2
from psycopg2.extensions import AsIs
import argparse
#from dateutil.parser import parse

parser = argparse.ArgumentParser(description="Sync data between databases")
parser.add_argument('input', action='store', type=str, help='Input db, example: "dbname=suppliers user=postgres password=postgres"')
parser.add_argument('output', action='store', type=str, help='Output db, example: "dbname=zetaweb user=postgres password=postgres"')
options = parser.parse_args()

#
# SET UP DB CONNECTIONS
#
print('Input: ' + options.input)
print('Output: ' + options.output)

indb = psycopg2.connect(options.input)
outdb = psycopg2.connect(options.output)

incur = indb.cursor()
outcur = outdb.cursor()

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
        # cursor.execute(statement, (AsIs(','.join(columns)), tuple(values)))
        print(outcur.mogrify(statement, (AsIs(','.join(columns)), tuple(values))))
    else:
        statement = 'UPDATE dir_domaininfo SET (%s) = (%s) WHERE id = %s'
        # cursor.execute(statement, (AsIs(','.join(columns)), tuple(values)))
        print(outcur.mogrify(statement, (AsIs(','.join(columns)), tuple(values), domain['id'])))



def SavePage(page, update=False):
    columns = page.keys()
    values = [page[column] for column in columns]

    if not update:
        statement = 'INSERT INTO site_info (%s) values %s'
        print(outcur.mogrify(statement, (AsIs(','.join(columns)), tuple(values))))
    else:
        statement = 'UPDATE site_info SET (%s) = (%s) WHERE id = %s'
        # cursor.execute(statement, (AsIs(','.join(columns)), tuple(values)))
        print(outcur.mogrify(statement, (AsIs(','.join(columns)), tuple(values), page['id'])))


def ProcessUnmatchedDomainFields(fields, existing_record):
    # TODO: Pass in all values for existing as key-value pairs of some sort.
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
        elif field == 'domains_linking_in':
            # Handled by domains_linking_in_last_updated.
            pass
        elif field == 'domains_linking_in_last_updated':
            if 'domains_linking_in' in fields:
                if inval < outval:
                    print('Existing value is newer, not copying')
                else:
                    print('Input value is newer, copying over')
                    existing_record['domains_linking_in_last_updated'] = inval
                    existing_record['domains_linking_in'] = fields['domains_linking_in'][0]
                    needs_save = True
            else:
                # TODO: Don't ignore this. The number may not have changed.
                print('No domains_linking_in in mismatched fields, ignoring difference in domains_linking_in_last_updated.')
        elif field == 'whois_last_updated':
            # TODO: Copy in all whois fields:
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
            # We need to be smart about this -- if a domain goes private or expires, we don't
            # want to delete previous data.
            #
            #if 'robots_ip' in fields:
            #    if inval < outval:
            #        print('Existing value is newer, not copying')
            #    else:
            #        print('Input value is newer, copying over')
            #        existing_record['robots_last_updated'] = inval
            #        existing_record['robots_ip'] = fields['robots_ip'][0]
            #        needs_save = True
            #else:
            #    print('No robots_ip in mismatched fields, ignoring difference in robots_last_updated.')
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


def ProcessUnmatchedPageFields(fields, existing_record):
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


#
# Here we do domains.
#
print('--- PROCESSING DOMAINS ---')

incur.execute("SELECT * FROM dir_domaininfo")
print('Number of dir_domaininfo: {0}'.format(incur.rowcount))

colnames = [desc[0] for desc in incur.description]
# print(colnames)

existing_query = 'SELECT * FROM dir_domaininfo WHERE URL = %s'

ignored_columns = ['id', 'majestic_rank', 'majestic_outdated', 'majestic_refsubnets', 'majestic_rank_date', 'alexa_rank', 'alexa_outdated',
'alexa_rank_date', 'quantcast_rank', 'quantcast_rank_date', 'quantcast_outdated',
'domcop_rank', 'domcop_pagerank', 'domcop_pagerank_outdated', 'domcop_pagerank_date']

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
            #print('Existing column {0} ({1}) is {2} in source'.format(index, existing_colnames[index], colpos[existing_colnames[index]]))
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
                #print('Field {0} ({1}) does not match. Input: {2}, Output: {3}'.format(existing_colnames[index], index, inval, outval))
                unmatched_fields[existing_colnames[index]] = (inval, outval)
        ProcessUnmatchedDomainFields(unmatched_fields, existing_record)
    else:
        print('The domain {0} is new.'.format(url))
        record = {}
        for index in range(len(row)):
            if colnames[index] != 'id':
                record[colnames[index]] = row[index]
        SaveDomain(record)
    row = incur.fetchone()

print('--- END PROCESSING DOMAINS ---\n')

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
            #print('Existing column {0} ({1}) is {2} in source'.format(index, existing_colnames[index], colpos[existing_colnames[index]]))
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
                #print('Field {0} ({1}) does not match. Input: {2}, Output: {3}'.format(existing_colnames[index], index, inval, outval))
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

incur.close()
outcur.close()
