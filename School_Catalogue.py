## School Catalogue

# We need to create classes for primary and high schools. Because these classes share properties and methods, 
# each will inherit from a parent School class. Our parent and three child classes have the following properties, getters, setters, and methods:

# 1. School
# Properties: name (string), level (one of three strings: 'primary', 'middle', or 'high'), and numberOfStudents (integer)
# Getters: all properties have getters
# Setters: the numberOfStudents property has a setter
# Methods: A __repr__ method that displays information about the school.

# 2. Primary
# Includes everything in the School class, plus one additional property
# Properties: pickupPolicy (string, like "Pickup after 3pm")

# 3. Middle
#Does not include any additional properties or methods

# 4. High
#Includes everything in the School class, plus one additional property
#Properties: sportsTeams (list of strings, like ['basketball', 'tennis'])



class School:
  def __init__(self,name,level,numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def get_name(self):
    return self.name
  def get_level(self):
    return self.level
  def get_numberofstudents(self):
    return self.numberOfStudents

  def set_numberOfStudents(self,new_numberOfStudents):
    self.numberOfStudents = new_numberOfStudents

  def __repr__(self):
    return f'A {self.level} school named {self.name} with {self.numberOfStudents} students'


class PrimarySchool(School):
  def __init__(self,name,numberOfStudents,pickupPolicy):
    super().__init__(name,"primary",numberOfStudents)
    self.pickupPolicy = pickupPolicy
    
  def get__primarySchool(self):
    return self.pickupPolicy

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + "The pickup polity is {pickupPolicy}".format(pickupPolicy = self.pickupPolicy)

class HighSchool(School):
  def __init__(self,name,numberOfStudents,sportsTeams):
    super().__init__(name,'high',numberOfStudents)
    self.sportsTeams = sportsTeams

  def get_highSchool(self):
    return self.sportsTeams
  
  def __repr__(self):
    return f"These are the sports {self.sportsTeams}"


  
 # Try School

mySchool = School("Codecademy", "high", 100)
print(mySchool)
print(mySchool.get_name())
print(mySchool.get_level())
mySchool.set_numberOfStudents(200)
print(mySchool.get_numberofstudents())

# Try PrimarySchool
testSchool = PrimarySchool("Codecademy",300,"Pickup Allowed")
print(testSchool.get__primarySchool())
print(testSchool)

# Try High School

testHSchool = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(testHSchool.get_highSchool())
print(testHSchool)
