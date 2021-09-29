# Imports the ability to open a webpage
import webbrowser

# Defines the class "Movie" that stores information (title, storyline,
# poster image, and youtube trailer)
class Movie():
	"""This class provides a way to store movie-related information."""
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	# Movie Constructor
	def __init__(self, movie_title, movie_storyline, 
					poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	# Opens a webpage in default browser with the trailer URL
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
