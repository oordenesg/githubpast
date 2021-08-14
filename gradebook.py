# You are a student and you are trying to organize your subjects and grades using Python. Let’s explore what we’ve learned about lists to organize your subjects and scores.
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# 1.  Create a list called subjects and fill it with the classes you are taking: "physics","calculus","poetry","history"
subjects = ["physics","calculus","poestry","history"]

# 2. Create a list called grades and fill it with your scores: 98, 97, 85, 88
grades = [98,97,85,88]

# 3. Manually (without any methods) create a two-dimensional list to combine subjects and grades. Use the table below as a reference to associated values. 
# Assign the value into a variable called gradebook
gradebook = [["physics",98],["calculus",97],["poetry",85],["history",88]]

# 4. Your grade for your computer science class just came in! You got a perfect score, 100! #Use the .append() method to add a list with the values of "computer science" 
# and an associated grade value of 100 to our two-dimensional list of gradebook.
gradebook.append(["computer science",100])

# 5. Your grade for "visual arts" just came in! You got a 93! Use append to add ["visual arts", 93] to gradebook.
gradebook.append(["visual arts",93])

# 6. Our instructor just told us they made a mistake grading and are rewarding an extra 5 points for our visual arts class. Access the index of the grade for your visual arts class and modify it to be 5 points greater.
gradebook[5][1] = gradebook[5][1] + 5

# 7. You decided to switch from a numerical grade value to a Pass/Fail option for your poetry class. #Find the grade value in your gradebook for your poetry class and use the .remove() method to delete it.
gradebook[2].remove(85)

# 8. Use the .append() method to then add a new "Pass" value to the sublist where your poetry class is located.
gradebook[2].append("Pass")

# 9. You also have your grades from last semester, stored in last_semester_gradebook. Create a new variable full_gradebook that combines 
# both last_semester_gradebook and gradebook using + to have one complete grade book. Print full_gradebook to see our completed list.
full_gradebook  = gradebook + last_semester_gradebook
print(gradebook)

