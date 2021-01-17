import psycopg2
import optparse

parser = optparse.OptionParser()
parser.add_option('-i', '--input', action='store', type='string', dest='input', help='Input db, example: "dbname=suppliers user=postgres password=postgres"')
parser.add_option('-o', '--output', action='store', type='string', dest='output', help='Output db, example: "dbname=zetaweb user=postgres password=postgres"')
(options, args) = parser.parse_args()

print('Input: ' + options.input)
print('Output: ' + options.output)

indb = psycopg2.connect(options.input)
outdb = psycopg2.connect(options.output)

incur = indb.cursor()
outcur = outdb.cursor()

incur.execute("SELECT version()")
outcur.execute("SELECT version()")

in_version = incur.fetchone()
print('In Database Version: ' + in_version)

out_version = incur.fetchone()
print('Out Database Version: ' + out_version)

incur.close()
outcur.close()
