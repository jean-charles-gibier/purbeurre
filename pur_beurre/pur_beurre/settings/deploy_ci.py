from . import *

# CI : sim bdd de prod
if 'DEPLOY_ENVIRON' in os.environ and os.environ['DEPLOY_ENVIRON'] == 'PRODUCTION':
    DATABASES = {
    
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'purbeurre',
            'PASSWORD': 'purbeurre',
            'HOST': 'purbeurre.ctquseoiqna8.eu-west-3.rds.amazonaws.com',
            'PORT': 5432,
            'TEST': {
                        'NAME': 'test_postgres2',
                    },
        }
    
    }
