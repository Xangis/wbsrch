class ModelDatabaseRouter(object):
    """Allows each model to set its own destiny"""

    def db_for_read(self, model, **hints):
        # Specify target database with field in_db in model's Meta class
        if hasattr(model._meta, 'in_db'):
            # print u'Model has database: {0}'.format(model._meta.in_db)
            return model._meta.in_db
        return 'default'

    def db_for_write(self, model, **hints):
        # Specify target database with field in_db in model's Meta class
        if hasattr(model._meta, 'in_db'):
            # print u'Model has database: {0}'.format(model._meta.in_db)
            return model._meta.in_db
        return 'default'

    def allow_syncdb(self, db, model):
        # Specify target database with field in_db in model's Meta class
        if hasattr(model._meta, 'in_db'):
            # print u'Model has database: {0}'.format(model._meta.in_db)
            if model._meta.in_db == db:
                return True
            else:
                return False
        else:
            # Random models that don't specify a database can only go to 'default'
            if db == 'default':
                return True
            else:
                return False

    def allow_migrate(self, db, model):
        if hasattr(model._meta, 'in_db'):
            # print u'Model has database: {0}'.format(model._meta.in_db)
            if model._meta.in_db == db:
                return True
            else:
                return False
        else:
            # Random models that don't specify a database can only go to 'default'
            if db == 'default':
                return True
            else:
                return False
