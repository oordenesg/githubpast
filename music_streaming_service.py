# We are building a music streaming service. We have provided two lists, representing songs in a user’s library and the amount of times each song has been played.
# Using a list comprehension, create a dictionary called plays that goes through zip(songs, playcounts) and creates a song:playcount pair for each song in songs and each playcount in playcounts.
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

zipped_plays = zip(songs,playcounts)
plays = {songs:playcounts for songs,playcounts in zipped_plays}

# After printing plays, add a new entry to it. The entry should be for the song "Purple Haze" and the playcount is 1.

plays.update({"Purple Haze": 1})

# This user has caught Aretha Franklin fever and listened to “Respect” 5 more times. Update the value for "Respect" to be 94 in the plays dictionary.

plays['Respect'] = 94

# Create a dictionary called library that has two key: value pairs: key "The Best Songs" with a value of plays, the dictionary you created, key "Sunday Feelings" with a value of an empty dictionary

library  = {"The Best Songs":plays, "Sunday Feelings":{}}
