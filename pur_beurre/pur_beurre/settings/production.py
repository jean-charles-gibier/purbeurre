from . import *
import raven
import sentry_sdk
import pprint
from sentry_sdk.integrations.django import DjangoIntegration



INSTALLED_APPS += [
    'raven.contrib.django.raven_compat',
]

RAVEN_CONFIG = {
    'dsn': 'https://b5b43e5820b14b2594e5a1d2507869fc@o450466.ingest.sentry.io/5435011', # caution replace by your own!!
    # If you are using git, you can also automatically configure the
    # release based on the git info.
#    'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'INFO', # WARNING by default. Change this to capture more than warnings.
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'INFO', # To capture more than ERROR, change to WARNING, INFO, etc.
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {'custom-tag': 'x'},
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}


res_init =sentry_sdk.init(
    dsn="https://b5b43e5820b14b2594e5a1d2507869fc@o450466.ingest.sentry.io/5435011",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

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
