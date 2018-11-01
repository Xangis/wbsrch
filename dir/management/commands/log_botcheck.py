# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from optparse import make_option
from dir.utils import GetSearchLogModelFromLanguage, IsBotAgent
from dir.models import language_list
import time

def CheckLogsForBots(lang, options):
    log_model = GetSearchLogModelFromLanguage(lang)
    total = log_model.objects.all().count()
    logs = log_model.objects.filter(is_bot=False, browserstring__isnull=False)
    print u'{0} total log entries in {1}, {2} need to be checked'.format(total, lang, logs.count())
    changed = 0
    checked = 0
    for log in logs:
        if IsBotAgent(log.browserstring):
            log.is_bot = True
            log.save()
            changed += 1
        checked = checked + 1
        if checked % 100000 == 0:
            print u'{0} checked.'.format(checked)
    print u'{0} of {1} log entries in {2} were checked. {3} newly marked as bots. Others were already bots or had no browser string.'.format(checked, total, lang, changed)

class Command(BaseCommand):
    help = """
    This command examines the search logs for known bot user agent strings and marks searches as bot
    searches. It should be run when we add new user agents to the bot list in utils.IsBotAgent.

    It is not necessary otherwise, since the logger automatically flags searches as bots as they are done.
    """
    option_list = BaseCommand.option_list + (
        make_option('-l', '--language', default='en', action='store', type='string', dest='language', help='Language to use for search logs (default=en).'),
        make_option('-e', '--everything', default=False, action='store_true', dest='everything', help='Process everything, all languages.'),
    )

    def handle(self, *args, **options):
        lang = options['language']
        everything = options['everything']
        if everything:
            for lang in language_list:
                CheckLogsForBots(lang, options)
        else:
            CheckLogsForBots(lang, options)
