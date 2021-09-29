# Imports "fresh tomatoes" file, which contains all of the HTML, CSS,
# and other content that provides the broad framework for the movie site and
# aggregates this file, and the media.py file, all together
import fresh_tomatoes

# Imports the class I've defined that stores the information (title, storyline,
# poster URL, trailer URL) for each movie in a standard fashion
import media

# Movie 1: Freddy Got Fingered
fgf = media.Movie("Freddy Got Fingered",
	"A struggling cartoonist tries to start" 
	"his career and clashes with his father.",
	"http://www.impawards.com/2001/posters/freddy_got_fingered_ver1.jpg",  # noqa
	"https://youtu.be/raLEbdAVYaM")

# Movie 2: The Dark Knight
dark_knight = media.Movie("The Dark Knight", 
	"The Joker threatens to disrupt the order" 
	"of Batman's Gotham City",
	"https://fanartexhibit.files.wordpress.com/2009/01/oscars_2.jpg",  # noqa
	"https://youtu.be/kmJLuwP3MbY")

# Movie 3: What's Eating Gilbert Grape?
wegg = media.Movie("What's Eating Gilbert Grape?", 
	"A small-town man has a lot of responsibility.",
	"http://www.impawards.com/1993/posters/whats_eating_gilbert_grape_ver1.jpg",  # noqa
	"https://youtu.be/wpSGFets1oM")

# Movie 4: Anchorman 1
anchorman = media.Movie("Anchorman: The Legend of Ron Burgundy", 
	"A newsteam in San Diego has a new reporter.",
	"http://images1.fanpop.com/images/photos/1500000/Anchorman-Posters-anchorman-1552244-334-474.jpg",  # noqa
	"https://youtu.be/Ip6GolC7Mk0")

# Movie 5: Mrs. Doubtfire
mrs_doubtfire = media.Movie("Mrs. Doubtfire", 
	"A divorced dad devises a plan to spend" 
	"more time with his children.",
	"http://moviefiles.alphacoders.com/416/poster-4168.jpg",  # noqa
	"https://youtu.be/eJCPPcCOCPo")

# Movie 6: Skyfall
skyfall = media.Movie("007: Skyfall", 
	"Bond's loyalty to M is tested as her" 
	"past comes back to haunt her.",
	"http://www.ew.com/sites/default/files/i/2012/09/17/skyfall-poster_510x756.jpg",  # noqa
	"https://youtu.be/6kw1UVovByw")

# Indexes 6 movies in a list
movies = [fgf, dark_knight, mrs_doubtfire, anchorman, wegg, skyfall]

# Puts it all together using the fresh tomatoes file and opens the website
fresh_tomatoes.open_movies_page(movies)
