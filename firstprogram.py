# for single comment ctrl slash
"""
for multi line comment shift alt A

"""
#python is dynamically typed language
name = "Sarvika"
age = 16
location = "Kathmandu"
#concate
print("My name is "  +name + "age is" +str(age)+"location is" +location)
#f string
print(f"My name is {name} and age is {age} and the location is {location}")
#format old version
print("My name is %s and age is %d and location is %s" %(name, age, location))
#format new version
print("My name is {0} and age is {1} and location is {2}".format(name,age,location))

print(type(location))

name = input("Enter the name")
age = int(input("Enter the age"))
location = input("Enter the location")
#concate
print("My name is "  +name + "age is" +str(age)+"location is" +location)
#f string
print(f"My name is {name} and age is {age} and the location is {location}")
#format old version
print("My name is %s and age is %d and location is %s" %(name, age, location))
#format new version
print("My name is {0} and age is {1} and location is {2}".format(name,age,location))

