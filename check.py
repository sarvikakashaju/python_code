#assignment

# Basic arithmetic
print(1 + 7) #Addition
print(12 - 7) #Subtraction
print(15 * 7) #Multipication
print(7 / 3) #division
print(17 // 5) #floor division
print(-13 // 5)   #floor division
print(17 % 5) #modulus
print(2 ** 10) #exponentation 

#Relational operator
print(10 == 10) 
print(10 > 20)  
#chained comparison
x=5
print(1 < x < 10) 
print(0 <= x <= 5)  
#string comparison
print("apple" < "banana") 
print("Python" == "python") 
print(1 == True)
print(0 == False) 
print(1 == "1") 

#assignment operator
score = 50
score += 10 
score *= 2 
score -= 20 
print(score) 
a = b = c = 0 
print(a, b, c) 
x, y, z = 1, 2, 3
print(x, y, z) 
a, b = 10, 20
a, b = b, a 
print(a, b) 

#Logical operator
age = 20
has_id = True
print(age >= 18 and has_id)
is_student = True
is_teacher = False
print(is_student or is_teacher)
print(not True)
print(not False)
print(False and 1/0)
print(True or 1/0)
marks = 72
print(marks >= 40 and marks <= 100)
print(marks < 40 or marks > 100)

#Bitwise operator
print(bin(12)) 
print(12 & 9) #and
print(12 | 9) #or
print(12 ^ 9) #xor
print(12 << 1) #left shift
print(40 >> 1) #right shift

#Membership & Identity Operators
a = {2, 3, 4}
b = {2, 3, 4}
c = a
print (a is b)
print (a is c)
print (a == b)
print (a == c)
print (id(a))
print (id(b))
print (id(c))