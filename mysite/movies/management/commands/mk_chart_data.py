import json

from django.core.management.base import BaseCommand, CommandError
from django.core import serializers
from movies.models import Movie, Showtime, Theater

class Command(BaseCommand):
    help = 'Making data source file for homepage bar chart'

    # add_arguments lets us specify arguments and options to read from the command
    # line when the command is executed.
    # We are going to add 1 argument- "json_file" which is a string (type=str)
    # representing the path to a json file containing our data to load.
    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    # The handle method is the main function of the command. This is the entry
    # point for our command and contains all our business logic.
    def handle(self, *args, **options):
        # Grab the path from our commandline arguments
        json_path = options['json_file']
        data = json.load(open(json_path))
        counts = dict.fromkeys(["Comedy", "Suspense/Thriller", "Drama", "Action/Adventure", "Sci-Fi/Fantasy", "Animated", "Romance", "Horror", "Family", "Spy Film", "Documentary", "Music/Performing Arts", "3D"], 0)

        for i, movie in enumerate(data):
            all_fields = movie['fields']
            genre = all_fields['movie_genre']
            counts[genre] = counts[genre] + 1

        with open('counts.json', 'w') as out:
            json.dump(counts, out)
