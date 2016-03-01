class SubDomainLanguage(object):
    def process_request(self, request):
        prefix = None
        try:
            prefix = request.META['HTTP_HOST'].split('.')[0]
            if prefix == 'no':
                prefix = 'nb'
            request.session['django_language'] = prefix
        except KeyError:
            pass
        if not prefix:
            request.session['django_language'] = 'en'
