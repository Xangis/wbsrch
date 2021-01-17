import psycopg2
import argparse

parser = argparse.ArgumentParser(description="Sync data between databases")
parser.add_argument('input', action='store', type=str, help='Input db, example: "dbname=suppliers user=postgres password=postgres"')
parser.add_argument('output', action='store', type=str, help='Output db, example: "dbname=zetaweb user=postgres password=postgres"')
options = parser.parse_args()

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

incur.close()
outcur.close()
