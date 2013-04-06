from optparse import make_option
from django.core import management
from django.core.management.base import NoArgsCommand, CommandError
from movies.api import *

class Command(NoArgsCommand):
    option_list = NoArgsCommand.option_list + (
        make_option(
            "--movie",
            action="store",
            dest="movie",
            help="Capture movie name"),
    )
    help = "Updates news from different sources.."
    def handle_noargs(self, **options):

        movie_name = options.get("movie")
        if(movie_name): search_and_save(movie_name)

