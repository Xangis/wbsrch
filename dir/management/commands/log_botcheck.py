# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from optparse import make_option
from dir.utils import GetSearchLogModelFromLanguage, IsBotAgent
import time

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-l', '--language', default='en', action='store', type='string', dest='language', help='Language to use for pending indexes (default=en).'),
    )

    def handle(self, *args, **options):
        lang = options['language']
        log_model = GetSearchLogModelFromLanguage(lang)
        total = log_model.objects.all().count()
        print u'{0} total log entries'.format(total)
        logs = log_model.objects.filter(is_bot=False, browserstring__isnull=False)
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
        print u'{0} of {1} log entries were checked. {2} newly marked as bots. Others were already bots or had no browser string.'.format(checked, total, changed)
