from django.core.management.base import BaseCommand, CommandError
from core import filler as fil


class Command(BaseCommand):
    help = 'Fills the current model via OFF'

    def add_arguments(self, parser):
        parser.add_argument('nb_products', nargs='?', type=int, default=10000)

    def handle(self, *args, **options):
        """ test filler is instancied """
        limit_nb_products = 0
        if 'nb_products' in options:
            limit_nb_products = options['nb_products']

        fil.Filler().start(limit_nb_products)
        pass



