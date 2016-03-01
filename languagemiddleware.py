from dir.models import language_list
from django.utils import translation

class LanguageFromDomain(object):
    def process_request(self, request):
        prefix = None
        try:
            prefix = request.META['HTTP_HOST'].split('.')[0]
        except KeyError:
            pass
        if not prefix or prefix not in language_list:
            prefix = 'en'
        request.LANGUAGE_CODE = prefix
        if prefix == 'no':
            translation.activate('nb')
        else:
            translation.activate(prefix)
