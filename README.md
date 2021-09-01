# How to Python

## Introduction 

Python is one of the most useful programming languages due to its flexibility and speed. Currently, Python programming has become one of the most demanding professional skills. To start with this new languague, we can add our first line of code. 

```python
my_name = "New_student" ## My name
print("Hello and welcome " + my_name + "!") ## Print the result
## Hello and welcome New_student!
```

As you saw previously, the code has two elements. The function or variables and comments. Using *#*, we are telling the computer to ignore that part of a program. So we can say that text written in a program but not run by the computer is called a comment. Another element in our previous code is the *print* function. In Python, the print() function is used to tell a computer to talk. The printed words that appear as a result of the *print* function are referred to as *output* of our program. 

In programming, computers refer to block of text as strings. In Python a string is either surrounded by double quotes or single quotes like "Hello World" or 'Hellor World'.  

Using Python, we can store data for reuse. This is what we called a variable. In this programming laguangue, we assign variables by using the equal sign *=*. Let's see an example

```python
message_string = "Hello there"
# Prints "Hello there"
print(message_string)
```

If the context of a program changes, we can update a variable but perform the same logical process on it. Let's see how to update a variable. 

```python
# Greeting
message_string = "Hello there!!!"
print(message_string)
 
# Farewell
message_string = "Bye! Take care"
print(message_string)
```

When we create a program it is normal to make mistakes. Python refers to mistakes as *errors* and will point to the location where an error ocurred with a *^* character.  When programs throw errors that we didn't expect to encounter we call those *errors bugs*.  Two common errors that we encounter while writing Python are SyntaxError and NameError.

- SyntaxError: Something is wrong with the way our program is written
- NameError: Ocurrs when Python interpreter a sees a word it does not recognize.

In general, computers can understand other types of data. One of the most relevant is *Numbers* and it has multiple ways of storing numbers. Within this data type, we can fin different types of data.  

1. An integer, or int, is a whole number. It has no decimal point and contains all counting numbers (1, 2, 3, …) as well as their negative counterparts and the number 0

2. A floating-point number, or a float, is a decimal number. It can be used to represent fractional quantities as well as precise measurements.

```python
# Define the release and runtime integer variables below:
release_year = 2009
runtime = 2
# Define the rating_out_of_10 float variable below: 
rating_out_of_10 = 7.6
```

Since we've already stored some numerical variables, we can also performe some calculations using programming language. Python performs addition, substraction, multiplication and division with *+, -, *, /*.

```python
# Prints "500"
print(573 - 74 + 1)
 
# Prints "50"
print(25 * 2)
 
# Prints "2.0"
print(10 / 5)
```
It is important to be careful when dividing by 0. In thi case, Python will raise a *ZeroDivisionError*.

When performing arithmetic operations on variables does not change the variable. Two variables can be added together, divided by 2, and multiplied by a third variable without Python distinguishing between the variables and literals. Let's see an example

```python
coffee_price = 1.50
number_of_coffees = 4
 
print(coffee_price * number_of_coffees) # Prints "6.0"
print(coffee_price) # Prints "1.5"
print(number_of_coffees) # Prints "4"
 
coffee_price = 2.00 # Updating the price 
 
print(coffee_price * number_of_coffees) # Prints "8.0"
print(coffee_price) # Prints "2.0"
print(number_of_coffees) # Prints "4"
```

If we want to work with exponents, Python can also perform this operation. Typing superscript numbers isn't always easy on modern keyboards. To do this opereation, we use te notation "**".

```python
print(2 ** 10) # 2 to the 10th power, or 1024
print(8 ** 2) # 8 squared, or 64
print(9 ** 3) # 9 * 9 * 9, 9 cubed, or 729
print(4 ** 0.5) # We can even perform fractional exponents
```

In Python can also obtained the remainder of a division calculation. This is called "modulo operator". If the number is divisible, then the result of the modulo operator will be 0. 

```python
print(29 % 5) # Prints 4 because 29 / 5 is 5 with a remainder of 4
print(32 % 3) # Prints 2 because 32 / 3 is 10 with a remainder of 2
print(44 % 2) # Modulo by 2 returns 0 for even numbers and 1 for odd numbers
```
The + operator doesn’t just add two numbers, it can also “add” two strings! The process of combining two strings is called string concatenation. Performing string concatenation creates a brand new string. Let's see an example

```python
greeting_text = "Hey there!"
question_text = "How are you doing?"
full_text = greeting_text + question_text
print(full_text) # Prints "Hey there!How are you doing?"

# To solve this, we can use " "

full_text = greeting_text + " " + question_text
print(full_text) # Prints "Hey there! How are you doing?"

# Let's see a new example

birthday_string = "I am "
age = 10
birthday_string_2 = " years old today!"
full_birthday_string = birthday_string + str(age) + birthday_string_2
# We have 2 options: 
print(full_birthday_string) # Prints "I am 10 years old today!"
# or 
print(birthday_string, age, birthday_string_2) # This also prints "I am 10 years old today!"
```
We can update variables using a shorthand called "plus equal".  When we have a number saved in a variable and want to add to the current value of the variable, we can use the += operator.

```python

number_of_miles_hiked = 12
number_of_miles_hiked += 2
print(number_of_miles_hiked) # Prints 14

#We can use this operator with strings

hike_caption = "What an amazing time to walk through nature!"
 
# Almost forgot the hashtags!
hike_caption += " #nofilter"
hike_caption += " #blessed"
```

## Boolean Expressions

When we want to built control flows into our programs, we want to be able to check if somethind is true or not. To do this, we can use boolean expression. These are statements that can either be True or False. Let's check the statement "Today is a weekday". This expression can be True if today is Tuesday, or it can be False if today is Saturday. There are no other options. However, the statement "Friday is the best day of the week" can be true or false depending on personal preferences.

Now that we understand what booleans expressions are, let's learn how to create them in Python. To do this we can use relational operators. The two relational operators we’ll cover first are:

1. Equals: ==
2. Not equals: !=

These operators compare two items and return True or False if they are equal or not. We can create boolean expressions by comparing two values using these operators:

```python
1 == 1     # True
2 != 4     # True
3 == 5     # False
'7' == 7   # False
```
If we write True or False in the code editor, they will appear in a different color than other variables.  This is because these True or False are their own sepcial type: bool. These are the only bool types that we can us in Python. There are several ways to use True or Fals. Let's check some of them. 

```python
# Set a variable equal to a boolean expression
set_to_true = True
set_to_false = False

# another option

bool_one = 5 != 7 
bool_two = 1 + 1 != 2
bool_three = 3 * 3 == 9
```
Booleans are important expression since they are relevant when building blocks of conditional statements.  Let's think about this situation. If it is raining, then bring an umbrella. Can we use a boolean expression here? Yes, we can. Right, "it is raining" is the boolean expression, and this conditional statement is checking to see if it is True. So, we can say if "it is raining" == True then the rest of the conditional statement will be executed and you will bring an umbrella.

This is the form of a conditional statement:  If [it is raining], then [bring an umbrella]

In Python, this conditiona statement looks very similar.

```python
if is_raining:
  print("bring an umbrella")
  
### A new example

user_name = "angela_catlady_87"

if user_name == "Dave":
  print("Get off my computer Dave!")

if user_name == "angela_catlady_87":
  print("I know it is you, Dave! Go away!")
```

Now that we have covered conditional statemetns, it is important to explore in more ways to use boolean expressions. In python, we can use relational operations to evaluate numbers or conditions. The commons are:

1. > greater than
2- >= greater than or equal to
3. < less than
4. <= less than or equal to

We can use them in functions or loops to evaluate if our data meet some conditions or not. We will see more them more often in the future. Now, let's concentrate in relational operations. Let's imagine that we're running a movie streaming platform and we want to check  if our users are over 13 or not. In Python, we can write a condition to evaluate this.

```python
if age <= 13:
  print("Sorry, parental control required")
```

This function will compare the age (as an input) with the condition "<=13". If this is true, then print("Sorry, parental control required"). Let's see more examples.

```python
x = 20
y = 20
if x == y:  
  print("These numbers are the same")

credits = 120
if credits >= 120:
  print("You have enough credits to graduate!")
```
In some cases, we need to check more than one conditional statement. In these cases, we can build a large boolean expression using boolean operators. These operators (also known as logical operators) combine smaller boolean expressions into larger boolean expressions. There are three boolean operators that we will cover: **and**,**or**,**not**. Now, let's use theres operators.

```python
(1 + 1 == 2) and (2 + 2 == 4)   # True
(1 > 9) and (5 != 6)            # False
(1 + 1 == 2) and (2 < 1)        # False 
(0 == 10) and (1 + 1 == 1)      # False

## Using the last example

credits = 120
gpa = 3.4
if credits >= 120 and gpa >= 2:
  print("You meet the requirements to graduate!")
```

Let's check how to se the *or* statement.

```python
True or (3 + 4 == 7)    # True
(1 - 1 == 0) or False   # True
(2 < 0) or True         # True
(3 == 8) or (3 > 4)     # False

## Using the previous example
credits = 118
gpa = 2.
if credits >= 120 or gpa >= 2.0:
  print("You have met at least one of the requirements.")
```

The final boolean operator we will cover is not. This operator is straightforward: when applied to any boolean expression it reverses the boolean value. So if we have a True statement and apply a not operator we get a False statement.

```python
not 1 + 1 == 2  # False
not 7 < 0       # True
```

 Once we start including lots of if statements in a function the code becomes a little cluttered and clunky. Luckily, there are other tools we can use to build control flow. else statements allow us to elegantly describe what we want our code to do when certain conditions are not met. else statements always appear in conjunction with if statements. Consider our waking-up example to see how this works:
 
 ```python
 if weekday:
  print("wake up at 6:30")
else:
  print("sleep in")
  
 ## Using the previous example
 
credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
    print("You do not meet the requirements to graduate.")
 ```

We can use elif statements to control the order we want our program to check each of our conditional statements. First, the if statement is checked, then each elif statement is checked from top to bottom, then finally the else code is executed if none of the previous conditions have been met.

```python
print("Thank you for the donation!")
 
if donation >= 1000:
  print("You've achieved platinum status")
elif donation >= 500:
  print("You've achieved gold donor status")
elif donation >= 100:
  print("You've achieved silver donor status")
else:
  print("You've achieved bronze donor status")
```

## List 

When we work with data, it is important to collect and store datapoints. In Python, a list is one of the many built-in data structures that allows us to do this. Let's imagine that we want to make a list of the heights of students in a class. Noelle is 61 inches tall, Ava is 70 inches, Sam is 67 inches and  Mia is 64 inches. Using Python, we can create a variable called **heights** to store these values. 

```python
# Create a variable called heights to store values.
heights = [61, 70, 67, 64] # A list begins and ends with square brackets [ ]
```

List can contain different data types. Using the last example, instead of storing each student's height, we can create a list that contains their names. We can even combine multiple data types in just one list as well. In general, *List* can contain any data type in Python. For example strings, intergers, booleans and float numbers. Let's check some examples.

```python
names = ["Noelle", "Ava", "Sam", "Mia"]
mixed_list_string_number = ["Noelle", 61]
mixed_list_common = ["Mia", 27, False, 0.5]
empty_list = [] # We can also create an empty list
```

There are internal built-in functions that we can use to create, manipulate, and even delete data from our list. We called them methods. For lists, methods will the form of *list_name*.method(). Some of them will require an input value that will go between the parenthesis of the method(). One of most popular methods is *.append()* and it allows us to add a new element to the end of a list. 

```python
append_example = [ 'This', 'is', 'an', 'example']
append_example.append('list')
print(append_example) # it will print ['This', 'is', 'an', 'example', 'list']

## Let's check a new example

example_list = [1, 2, 3, 4]
example_list.append(5)  #Using Append
print(example_list)

example_list.remove(5) #Using Remove
print(example_list)
```

We can add additional elements using the *+* operator to combine two list (this is aslo known as concatenation). 

```python
items_sold = ["cake", "cookie", "bread"]
items_sold_new = items_sold + ["biscuit", "tart"]
print(items_sold_new)

# A second example
my_list = [1, 2, 3]
my_list + 4 # It will print an error
my_list + [4] # It will print [1,2,3,4]
```

Let's imagine we are interviewing candidates for a job. We will call each candidate in order, represented by a Python list. 

```python
calls = ["Juan", "Zofia", "Amare", "Ezio", "Ananya"]
```


In Python, we call the location of an element in a list its index. Python lists are zero-indexed. This means that the first element in a list has index 0, rather than 1.In this example, the element with index 2 is "Amare". We can select a single element from a list by using square brackets ([]) and the index of the list item. If we wanted to select the third element from the list, we’d use calls[2]:

```python
print(calls[2]) ## The output will be Amare 
```

We can select the last element of a list by using negative index. We can use the index *-1* to select the last item of a list. Let's see the following example.

```python
pancake_recipe = ["eggs", "flour", "butter", "milk", "sugar", "love"]
print(pancake_recipe[-1]) # The ouput will be 'love'

#### A second example

hopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]
last_element = shopping_list[-1]
index5_element = shopping_list[5]
print(last_element) # "cereal"
print(index5_element) # "cereal
```

In list, we can update or modify a value by using the index. To do this, reassing the value using the specific index of the element. 

```python
# First example
garden = ["Tomatoes", "Green Beans", "Cauliflower", "Grapes"]
garden[2] = "Strawberries"
print(garden) # it will print ["Tomatoes", "Green Beans", "Strawberries", "Grapes"]

# Second example
garden_waitlist = ["Jiho","Adam","Sonny","Alisha"]
garden_waitlist[1] = "Calla"
print(garden_waitlist)
garden_waitlist[-1] = "Alex"
print(garden_waitlist)
```

We can also remove elements from our list by using the built-in function *.remove()*. Let's see how to use the function.

```python
# First example
shopping_line = ["Cole", "Kip", "Chris", "Sylvana"]
shopping_line.remove("Chris")
print(shopping_line) # ["Cole", "Kip", "Sylvana"]

# Second example

order_list = ["Celery","Orange Juice","Orange","Flatbread"]
print(order_list)
order_list.remove("Flatbread")
print(order_list)
new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
print(new_store_order_list)
new_store_order_list.remove("Mango")
print(new_store_order_list)
new_store_order_list.remove("Onions") # It will print an error. We don't have onions.
```


As we saw previously, list can be filled with number or strings. However, list can contain other lists as well. We will commonly refer to these as two-dimensional lists. Let's see an example. Noelle is 61 inches tall, Ava is 70 inches, Sam is 67 inches and Mia is 64 inches. Previously, we saw that we could create a list representing both Noelle’s name and height:

```python
noelle = ["Noelle", 61]
# We can put several of these lists into one list, such that each entry in the list represents a student and their height:
heights = [["Noelle", 61], ["Ava", 70], ["Sam", 67], ["Mia", 64]]

# Second example
heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64],["Vik",68]]
ages = [["Aaron",15],["Dhruti",16]]
```

Two-dimensional lists can be accessed using brackets as well. However, instead of providing a single pair of brackets [ ] we will use an additional set for each dimension past the first.

```python
# Using the previous example
noelles_height = heights[0][1] 
print(noelles_height) ## It will print 61

# Second example
class_name_test = [["Jenny",90],["Alexus",85.5],["Sam",83],["Ellie",101.5]]
print(class_name_test)

sams_score = class_name_test[2][1]
print(sams_score)

ellies_score = class_name_test[-1][-1]
print(ellies_score)
```

Using this example, let's imagine that our list stores the student’s favorite hobby and one of them "Jenny" changed her hobby. Let's do that.

```python
class_name_hobbies = [["Jenny", "Breakdancing"], ["Alexus", "Photography"], ["Grace", "Soccer"]] # Original list
# "Jenny" changed their mind and is now more interested in "Meditation".
class_name_hobbies[0][1] = "Meditation"
print(class_name_hobbies) # [["Jenny", "Meditation"], ["Alexus", "Photography"], ["Grace", "Soccer"]]

# Second example
incoming_class = [["Kenny","American",9],["Tanya","Russian",9],["Madison","Indian",7]]
print(incoming_class)
incoming_class[2][2] = 8
print(incoming_class)
incoming_class[-3][-3] = "Ken"
print(incoming_class)
``` 

Now are going to explore additional ways of working with lists. Using built-in functions we can:

1. Add and remove items from a list using a specific index.
2. Create lists with continuous values.
3. Get the length of a list.
4. Select portions of a list (called slicing).
5. Count the number of times that an element appears in a list.
6. Sort a list of items.


The method .insert() allows us to add a new element to a specific index in a list. This method takes two inputs, the index and the element we want to insert. This method can also handle shifting over elements and ca be used with negative indices. Let's see an example

```python
store_line = ["Karla", "Maxium", "Martim", "Isabella"]
store_line.insert(2, "Vikor")
print(store_line)  # The output will be  ['Karla', 'Maxium', 'Vikor', 'Martim', 'Isabella']
``` 
Some important details about this method are:
1. The order and number of the inputs is important. The .insert() method expects two inputs, the first being a numerical index, followed by any value as the second input.
2. When we insert an element into a list, all elements from the specified index and up to the last index are shifted one index to the right. This does not apply to inserting an element to the very end of a list as it will simply add an additional index and no other elements will need to shift. 

Let's see an second example

```python
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"] 
front_display_list.insert(0,"Pineapple")
print(front_display_list) # ['Pineapple', 'Mango', 'Filet Mignon', 'Chocolate Milk']
```

Python gives us a method to remove elements from a list as well. This method is quite similar to .insert(). However, the .pop() method takes an optional single input: The index for the element you want to remove. Let's see how it works

```python
# First example
cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]
removed_element = cs_topics.pop() # without index means "remove the last element"
print(cs_topics)
print(removed_element) # ["Python", "Data Structures", "Balloon Making", "Algorithms"]

# Second example
data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
data_science_topics.pop()
print(data_science_topics) # ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics"]
data_science_topics.pop(3)
print(data_science_topics) # ['Machine Learning', 'SQL', 'Pandas', 'Statistics']
```

In Python, we can also create a list of consecutive numbers like [0,1,2,3,4,5,6]. Typing out all those numbers is overwhelming. However, Python gives us an easy way of creating these type of lists using a built-in function called *range()*. This function takes a single input and generates numbers starting at 0 and ending at the number before the input. Let's see an example:

```python
# First example
my_range = range(10)
print(my_range) # It will print range(0, 10)
print(list(my_range)) # It will print [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Second example
zero_to_seven = range(8)
print(list(zero_to_seven)) # [0, 1, 2, 3, 4, 5, 6, 7]
``` 
If we use this same method but with two inputs, we cancreate a list that starts at a different number. For example, range(2,9) would generate numbers starting at 2 and ending at 8.

```python
my_list = range(2, 9)
print(list(my_list)) # It will print [2, 3, 4, 5, 6, 7, 8]
```
If we use a third input our method, we can create a list that "skips" numbers. For example, range(2, 9, 2) will give us a list where each number is 2 greater than the previous number.

```python
my_range2 = range(2, 9, 2)
print(list(my_range2)) # It will print [2, 4, 6, 8]

# Second exaxmple
range_diff_five = range(0,40,5)
print(list(range_diff_five)) # It will print [0, 5, 10, 15, 20, 25, 30, 35]
```

Sometimes, we need to find the number of times in a list. We can do this by using the .len() method.

```python
# First example
my_list = [1, 2, 3, 4, 5]
print(len(my_list)) # It will print 5

# Second example

long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]
range_list = range(2, 3000, 10)

long_list_len = len(long_list)
print(long_list_len) # It will print 18

range_list_length = len(range_list)
print(range_list_length) # It will print 300

range_list = range(2, 3000, 100)
range_list_length = len(range_list)
print(range_list_length) # It will print 30
```

If we want to extract only a portion of a lists. We can use the following sintax table[start:end]. 
```python
# First example
letters = ["a", "b", "c", "d", "e", "f", "g"]
sliced_list = letters[1:6]
print(sliced_list) # It will print ["b", "c", "d", "e", "f"]

# Second Example
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]
beginning = suitcase[0:4]

print(beginning) # It will print ['shirt', 'shirt', 'pants', 'pants']
beginning = suitcase[0:2]
print(beginning) # ['shirt', 'shirt']
middle = suitcase[2:4]
print(middle) # ['pants', 'pants']
```

Slicing syntax in Python is very flexible. Let’s look at a few more problems we can tackle with slicing. Let's see some examples

```python
# First example

# fruits = ["apple", "cherry", "pineapple", "orange", "mango"]
# If we want to select the first n elements of a list, we could use the following code:

fruits[:n]
print(fruits[:3]) # Would output ['apple', 'cherry', 'pineapple']

# We can do something similar when we want to slice the last n elements in a list:
# fruits[-n:] For our fruits list, suppose we wanted to slice the last two elements.

print(fruits[-2:]) # Would output ['orange', 'mango']

# Negative indices can also accomplish taking all but n last elements of a list.
# fruits[:-n]
print(fruits[:-1]) # Would output ['apple', 'cherry', 'pineapple', 'orange']

# Second example

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

last_two_elements = suitcase[-2:]
print(last_two_elements)

slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)
```

If we want to count occurrences of an item in a list. We can use the .count() method. Let's see how it works.

```python
letters = ["m", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"]
num_i = letters.count("i")
print(num_i) # Would output 4

```
We can also use this function to count elements in a two-dimensional list. 

```python
# First example
number_collection = [[100, 200], [100, 200], [475, 29], [34, 34]]
num_pairs = number_collection.count([100, 200])
print(num_pairs) # Would output 2

# Second examle
votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]
jake_votes = votes.count("Jake")
print(jake_votes) # Would output 9
```
Often, we will want to sort a list in either numerical (1, 2, 3, …) or alphabetical (a, b, c, …) order. We can sort a list using the method .sort().

```python
# First example
names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
names.sort()
print(names) # ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']

names.sort(reverse=True)
print(names) # ['Xander', 'Willow', 'Giles', 'Buffy', 'Angel']
``` 

A second way of sorting a list in Python is to use the built-in function sorted(). The sorted() function is different from the .sort() method in two ways:

1. It comes before a list, instead of after as all built-in functions do.
2. It generates a new list rather than modifying the one that already exists.

```python
# First example
names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
sorted_names = sorted(names)
print(sorted_names) # Would output ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']

# Note that using sorted did not change names:
print(names) # Would output ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']

# Second example
games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]
games_sorted = sorted(games)
print(games) # Would output ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
print(games_sorted) # Would output ['Minecraft', 'Pacman', 'Pokemon', 'Portal', 'Tetris', 'The Sims']
```

## Loops 

In programming, the process of using an initialization, repetitions, and an ending condition is called a loop. In a loop, we perform a process of iteration (repeating tasks.
Using Python there two types of iteration.

- Indefinite iteration, where the number of times the loop is executed depends on how many times a condition is met.
- Definite iteration, where the number of times the loop will be executed is defined in advance (usually based on the collection size).

In this section, we’ll learn how to use Python to implement both definite and indefinite iteration in our own programs.

Let's imagine we have a list of ingredients and we want to print out all of them.

```python
ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
#If we only use print(), our program might look like this:

print(ingredients[0])
print(ingredients[1])
print(ingredients[2])
print(ingredients[3])
print(ingredients[4])
```

This process is managable when we write 5 or 10 print() statements. However, let's imagine that our list has 100,000 elements. It would take an extremely long time and by the end, we could still end up with inconsistencies and mistakes. To do this, we can use loops. 

Let’s start with your first type of loop, a for loop, a type of definite iteration. In our examples, we will be using Python lists as our collection of elements.
With for loops, on each iteration, we will be able to perform an action on each element of the collection. Before we work with any collection, let’s examine the general structure of a for loop:

```python
for <temporary variable> in <collection>:
  <action>
Let’s break down each of these components:
```

A for keyword indicates the start of a for loop. A <temporary variable> that is used to represent the value of the element in the collection the loop is currently on. An in keyword separates the temporary variable from the collection used for iteration. A <collection> to loop over. In our examples, we will be using a list. An <action> to do anything on each iteration of the loop. Now, let's use our previous example to create a for loop.
 
```python
ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
for ingredient in ingredients:
  print(ingredient)
 
# This code outputs: milk,sugar,vanilla extract,dough, chocolate
```
 
Let's see more examples
 
 ```python
 board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]
sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
  print(game)
for sport in sport_games:
  print(sport)
 ````
 
 Sometimes we won't be iterating through a specific list, but rather only want to perform a certain action multiple times. To create a for loop we can use the built-in function range(). Let's see an example
 
```python
six_steps = range(6) 
# six_steps is now a collection with 6 elements:
# 0, 1, 2, 3, 4, 5
```
 We can use the six_steps variable directly in our for loop to perfrom a six-step interation:
 
```python
for temp in range(6):
  print("Learning Loops!")
```

If we want to add additional information, we can use the same variable to track it.
 
```python
for temp in range(6):
  print("Loop is on iteration number " + str(temp + 1))
```

For loops are not the only type of loops we can use. Another type of loop is called a while loop and is a form of indefinite iteration. 
A while loop performs a set of instructions as long as a given condition is true. The structure follows this pattern:
 
```python
while <conditional statement>:
  <action>
Let’s examine this example, where we print the integers 0 through 3:
```
Let's see a simple loop using *while*
   
```python
count = 0
while count <= 3:
  # Loop Body
  print(count)
  count += 1
```
                
Lets analyze this loop: 
                
1. The first variable count is equal to 0. The conditional statement in the while loop is count <= 3, which is true at the initial iteration of the loop. With this the loop body executes. Inside the loop, it is possible to see that we want to increment to count by 1

2. When loop finish the firts iteration, Python returns to the top of the loop and check the condition again. After the first iteration count should be equal to 1. With this, the condition still evaluates to true and to the loop continues.

3. This process continues until the count variable becomes 4. At that point, the condition is false and the loop will stop. 
   
Let’s write a while loop that counts down from 10 to 0(inclusive).
 
```python
countdown = 10;

while countdown >=0:
  print(countdown)
  countdown += -1

print("We have liftoff!")
```
   
A while loop is not only for counting.  We can use this tool to iterate through a list as well.
Lets check an example.

```python
ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

length = len(ingredients)
index = 0
 
while index < length:
  print(ingredients[index])
  index += 1

# our final output wouldbe 
# milk
# sugar
# vanilla extract
# dough
# chocolate
```
                     
lets check a new example.

```python
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 
length = len(python_topics)
index = 0
while index < length:
  print('I am learning about ' + python_topics[index])
  index += 1
```
       
In Python, Loops are very versatile. This programming languague provides a set of control
statements that we can use to get more control.

Let's check an example that we may encounter to see a use case for loop control statements.
If we want to search a list to check if a specific value exists, we can use a if statement to check this.

```
items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]

for item in items_on_sale:
  if item == "knit dress":
    print("Found it")
```


This code goes through each item in items_on_sale and checks for a match. Once "knit_dress" is found in the list items_on_sale, we don’t need to go through the rest of the items_on_sale list. Unfortunately, our loop will keep running until we reach the end of the list.
