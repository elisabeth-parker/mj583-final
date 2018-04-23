import datetime
import json

from django.core.management.base import BaseCommand, CommandError
from movies.models import Movie, Showtime, Theater

# Here we are creating a custom management command to load our winner data into
# Django models.
# The Command class is loaded by Django at runtime and executed when the file
# that contains it is specified as the command to manage.py
# In our case this file is called `load_winners.py` so the command we will use
# to execute this file is `manage.py load_winners path/to/winners.json`
class Command(BaseCommand):
    help = 'Load movie data into the database'

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

        # We are going to write output to the screen as we process things so
        # the user has feedback the script is running.
        self.stdout.write(self.style.SUCCESS('Loading JSON from "{}"'.format(json_path)))
        data = json.load(open(json_path))

        # Track the total number of records
        total = len(data)

        # Let the user know we're running
        self.stdout.write(self.style.SUCCESS('Processing {} rows'.format(total)))

        # Create an array to hang on to anything skipped while processing
        skipped = []

        # Loop over each row in the data with the enumerate function so we have
        # a row counter
        for i, row in enumerate(data):
            # for j, theater in enumerate(row):
            theaters = row['theaters']
            for j, theater in enumerate(theaters):
                try:
                    th_name = theater['name']
                    th_id = theater['id']
                    th_address = theater['address1']
                    th_phone = theater['phone']
                    th_geo = theater['geo']
                    th_lat = th_geo['latitude']
                    th_lng = th_geo['longitude']
                    th_city = theater['city']
                    # if th_city == "Cary" or th_city == "Raleigh" or th_city == "Morrisville" or th_city == "Cary" or th_city == "Holly Springs":
                    #     th_county = "Wake County"
                    # elif th_city == "Durham":
                    #     th_county = "Durham County"
                    # else:
                    #     th_county = "Orange County"
                    # for k, location in enumerate(th_geo):
                    #     th_lat = location[0]
                    #     th_long = location[1]

                    theater_instance, _ = Theater.objects.get_or_create(
                        name = th_name,
                        th_id = th_id,
                        address = th_address,
                        phone = th_phone,
                        lat = th_lat,
                        long = th_lng,
                        city = th_city,
                    )

                    th_movies = theater.get('movies')
                    if(th_movies):
                        th_movie_list = []
                        for m, movie in enumerate(th_movies):

                            movie_instance, _ = Movie.objects.get_or_create(
                                movie_id = movie['id'],
                                title = movie['title'],
                                runtime = movie['runtime'],
                                releaseDate = movie['releaseDate'][0:10],
                                poster = movie['poster']['size']['full'][2:],
                                rating = movie['rating'],
                                movie_genre = movie['genres'][0],
                            )
                            movie_instance.theaters.add(theater_instance)
                            theater_instance.movie_set.add(movie_instance)
                            #th_movie_list.append(movie["title"])

                            variants = movie.get('variants')
                            if variants:
                                for v, variant in enumerate(variants):
                                    amenityGroups = variant.get('amenityGroups')
                                    if amenityGroups:
                                        for a, amenity in enumerate(amenityGroups):
                                            showtimes = amenity.get('showtimes')
                                            if showtimes:
                                                for s, showtime in enumerate(showtimes):
                                                    showtime_instance, _ = Showtime.objects.get_or_create(
                                                        movie = movie_instance,
                                                        theater = theater_instance,
                                                        time = showtime['date'],
                                                        tickets = showtime['ticketingUrl'],
                                                    )
                # If we don't have some data/something breaks add the row to the skipped list and
                # continue to the next item in the for loop
                except:
                    skipped.append(theater)
                    print(th_name)
                    continue

                # Now we tell the user which object count we just updated.
                # By using the line ending `\r` (return) we return to the begginging
                # of the line and start writing again. This writes over the same line
                # and gives the illusion of the count incrementing without cluttering
                # the screens output.
                self.stdout.write(self.style.SUCCESS('Processed {}/{}'.format(i + 1, total)), ending='\r')
                # # We call flush to force the output to be written
                self.stdout.flush()

    # If we have any skipped rows write them out as json.
    # Then the user can manually evaluate / edit the json and reload it once
    # it has been fixed with `manage.py load_winners skipped.json`
        if skipped:
            self.stdout.write(self.style.WARNING("Skipped {} records".format(len(skipped))))
            with open('skipped.json', 'w') as fh:
                json.dump(skipped, fh)
