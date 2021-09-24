 # This lesson has shown you the vast variety of string methods and their power. Whatever the problem you are trying to solve, if you are working with strings then string methods are likely going to be part of the solution.

# .upper(), .title(), and .lower() adjust the casing of your string.
# .split() takes a string and creates a list of substrings.
# .join() takes a list of strings and creates a string.
# .strip() cleans off whitespace, or other noise from the beginning and end of a string.
# .replace() replaces all instances of a character/string in a string with another character/string.
# .find() searches a string for a character/string and returns the index value that character/string is found at.
# .format() allows you to interpolate a string with variables.


highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# 1. First, start by printing highlighted_poems to the terminal and see how it displays.

print(highlighted_poems)

# 2. Start by splitting highlighted_poems at the commas and saving it to highlighted_poems_list. Print highlighted_poems_list, how does the structure of the data look now?

highlighted_poems_list = highlighted_poems.split(',')
print(highlighted_poems_list)

# 3. Notice that there is inconsistent whitespace in highlighted_poems_list. Let’s clean that up. Start by creating a new empty list, highlighted_poems_stripped. Print highlighted_poems_stripped.

highlighted_poems_stripped = []
for author in highlighted_poems_list:
  highlighted_poems_stripped.append(author.strip())

print(highlighted_poems_stripped)

# 4. .Next we want to break up all the information for each poem into it’s own list, so we end up with a list of lists. Create a new empty list called highlighted_poems_details
#  Iterate through highlighted_poems_stripped and split each string around the : characters and append the new lists into highlighted_poems_details.

highlighted_poems_details = []
for i in highlighted_poems_stripped:
  highlighted_poems_details.append(i.split(':'))

print(highlighted_poems_details)

# 5.  Now we want to separate out all of the titles, the poets, and the publication dates into their own lists. Create three new empty lists, titles, poets, and dates.
# Iterate through highlighted_poems_details and for each list in the list append the appropriate elements into the lists titles, poets, and dates.

titles = []
poets = []
dates = []

for element in highlighted_poems_details:
  titles.append(element[0])
  poets.append(element[1])
  dates.append(element[2])
  
  
# 6. Finally, write a for loop that uses .format() to print out the following string for each poem: The poem TITLE was published by POET in DATE.

for i in range(0,len(titles)):
  print("The poem {} was published by {} in {}.".format(titles[i],poets[i],dates[i]))
