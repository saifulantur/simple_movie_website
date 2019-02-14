import media
import fresh_tomatoes

toy_story = media.Movie ("Toy Story",
                         "This is the story line of toy story",
                         "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=7LgyNeG2Pv8")

avatar = media.Movie ("Avatar",
                         "This is the story line of avatar",
                         "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=KGeX3dTO6JU&list=RDMMKGeX3dTO6JU&start_radio=1")

got = media.Movie ("GOT",
                         "This is the story line of game of thrones",
                         "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=KGeX3dTO6JU&list=RDMMKGeX3dTO6JU&start_radio=1")

dark = media.Movie ("Dark",
                         "This is the story line of dark",
                         "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=KGeX3dTO6JU&list=RDMMKGeX3dTO6JU&start_radio=1")

vikings = media.Movie ("Vikings",
                         "This is the story line of vikings",
                         "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=KGeX3dTO6JU&list=RDMMKGeX3dTO6JU&start_radio=1")


movies = [toy_story, avatar, got, dark, vikings]
fresh_tomatoes.open_movies_page(movies)                        
#print(avatar.storyline)
