import lyricsgenius as lg
from lyricsgenius import Genius
import os
#from dotenv import load_dotenv
#api_key = 
#local testing code only. remove before adding to git

#import key from .env
api_key = os.environ['GENIUS_API_KEY']

genius = lg.Genius(api_key)

lyrics = []

user_artist = input("Please provide a music artist stage name: ").strip().title()

#Searches 5 most popular songs
artist = genius.search_artist(user_artist, max_songs=5,sort="popularity")

#this can print the same list that is already returned from the api
print(artist.songs)


#iteraties through the list of artist.songs that was created via the api search
for song in artist.songs:
    if song is not None:
        # prints the song lyrics
        print(song.title)
        print(song.lyrics[:100])





#if artist:
    
#    for song in songs:
#        print(songs)
#else:
#    print("Arist not found")