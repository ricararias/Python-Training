'''
#print('hello my name is Ricardo')
#print('what Im really looking for')
#print(5,-7,8)
#print("my name could be Ricardito")
#print("    /|")
#print("   / |")
#print("  /  |")
#print(" /   |")
#print("/____|")
#x=25
#y='result'
#print (x,y)
#print( 'Hello' )
'''
'''
name='Jhon'
age='25'
print('this guy who is called ' + name + ' has '+ age +' years old')
name='Ricardo'
age='40'
print('this guy who is called ' + name + ' has '+ age +' years old')


name='ricardo'
age='25'
#print('this guy who is called ' + name + ' has '+ age +' years old')
print(name.replace('r','z'))


name='Jhon'
age=25
print('this guy who is called ' + name + ' has '+ str(age) +' years old')
'''

#name = input("Enter your name: ")
#age = input("Enter your age: ")
#print("hello " + name + "!" + " your age " + age)

'''
number1=(input("Enter a number: "))
number2=(input("Enter another number: "))
result= (float(number1)+float(number2))
#print(result)
print ("the result of the sum is: " + str(result))
'''

'''
color=input("Enter a color: ")
plural_noun=input("Enter a plural noun: ")
celebrity=input("Enter a celebrity: ")
print("roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)
'''

#string
'''
lucky_numbers=[22, 5, 82, 19, 23, 26]
friends=["kevin", "Oscar", "Karen", "Oscar", "Jim", "Oscar", "Tobby"]
#friends.extend(lucky_numbers)
friends.append("Ricardo")
#friends.insert(1,"orlando")
#friends.remove("Jim")
#friends.clear()
#friends.pop()
#print(friends.count("Oscar"))
#lucky_numbers.sort()
#lucky_numbers.reverse()
#friends2=friends.copy()
print(friends)
'''

#coordinates=(4, 5)  #can't change these values - tuples
#print (coordinates[1])

#functions:
'''
def say_hi(name, age):
    print("hello " + name + " you are " + age)

say_hi("Mike", "29")
say_hi("Steve", "32")

def  cube(num):
    return num*num*num

result = cube(4)
print(result)
'''

#if condition
'''
is_male = False
is_tall = False

if is_male and is_tall:
    print("you are a male and tall")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and (is_tall):
    print("you are no a male but you are tall")
else:
    print("you are either not a male or not tall or both")
'''

#Function
'''
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_num(15,2,9))
'''

#Calculator
'''
num1=float(input("enter the first number: "))
op=input("enter the operation: ")
num2=float(input("enter the second number: "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("invalid operation")
'''


#dictionary
'''
monthConversions={
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "Jun",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
print(monthConversions.get("Oct", "Not a valid key"))
'''

'''
i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with lopp!")
'''

'''
secret_word = "giraffe"
guess = ""
guess_count = 1
guess_limit = 3

while guess != secret_word and guess_count <= guess_limit:
    guess = input("Enter guess " + str(guess_count) + ": ")
    guess_count += 1

if guess_count > guess_limit and guess != secret_word:
    print("You loose!")
else:
    print("You win!")
'''


#loop
'''
friends = ["Jim", "Karen", "Kevin"]
#for friend in friends:
#    print(friend)

for index in range(friends.__len__()):
    print(friends[index])
'''

#Exponent function
#print(2**3)
'''
def raise_to_power(base_number, pow_number):
    result = 1
    for index in range(pow_number):
        result = result * base_number
    return result

print(raise_to_power(2, 4))
'''

'''
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
#print(number_grid[2][1])

#nestle for lup
for row in number_grid:
    for col in row:
        print(col)
'''

#Building a Translator
'''
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
'''


#Try Except
'''
try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid input")
'''


#Reading files
'''
employee_file = open("employees1.txt", "w")

employee_file.write("\nKelly - Costumer Service")

#print(employee_file.read())
#print(employee_file.readline())


employee_file.close()
'''


#Modules and pip
































