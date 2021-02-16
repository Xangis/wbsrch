from django.core.management.base import BaseCommand
from dir.utils import GenerateMonthlySearchReports
import datetime


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-m', '--month', default=None, action='store', type=int, dest='month', help='Month to index.)')
        parser.add_argument('-y', '--year', default=None, action='store', type=int, dest='year', help='Year to index.')
        parser.add_argument('-l', '--language', default=None, action='store', type=str, dest='language', help='2-letter code of language to index, leave blank for all.')

    def handle(self, *args, **options):
        language = options.get('language', None)
        if language:
            print('generate_search_report: Only generating for language {0}'.format(language))
        if options['month'] and options['year']:
            print('generate_search_report: Date specified as: ' + str(options['year']) + '-' + str(options['month']))
            GenerateMonthlySearchReports(month=options['month'], year=options['year'], language=language)
        else:
            d = datetime.date.today()
            first = datetime.date(day=1, month=d.month, year=d.year)
            lastmonth = first - datetime.timedelta(days=1)
            print('generate_search_report: Date not specified. Using ' + str(lastmonth.year) + '-' + str(lastmonth.month))
            GenerateMonthlySearchReports(month=lastmonth.month, year=lastmonth.year, language=language)
