class InvalidLanguageException(Exception):
    language = None

    def __init__(self, language):
        super(InvalidLanguageException, self).__init__(language)
        self.language = language
