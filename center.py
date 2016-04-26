import movie
import fresh_tomatoes

#Init a movie instance with Title, Summary, Image_url and youtube url
DeadPool = movie.MovieInfo(
	"DeadPool",
	"2016 American superhero film based on the Marvel Comics character of the same name",
	"https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
	"https://www.youtube.com/watch?v=gtTfd6tISfw")

Captain_America = movie.MovieInfo(
	"Captain America: Civil War",
	"Political interference in the Avengers' activities causes a rift between former allies Captain America and Iron Man",
	"https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
	"https://www.youtube.com/watch?v=1L3c17AmCZw")

Batman_Superman = movie.MovieInfo(
	"Batman v Superman: Dawn of Justice",
	"2016 American superhero film featuring the DC Comics characters Batman and Superman",
	"https://upload.wikimedia.org/wikipedia/en/2/20/Batman_v_Superman_poster.jpg",
	"https://www.youtube.com/watch?v=fis-9Zqu2Ro")

#Define an array and pass as argument to function"""
movies = [DeadPool,Captain_America,Batman_Superman]
fresh_tomatoes.open_movies_page(movies)