#print()
#input() # argument
#len() # return
#int() #
#str()
#pop()
#append()
#insert()
#extend()
#remove()

# Definition
#z = f(x,y)
#def hello():
    #print("hello world")
    #return 5 #(after you use return that specific function ends)

#calling the function
#result = hello() #(= refers to variable)
#print(result)


#name = "Asli" #global
#formal parameters are number1 and number2
#def add (number1, number2): # number1 = 5 and number2 = 3
    #number1 and number2 are localvariables
 #   result = number1 + number2
  #  return result

#print(add(5, 3))


#Demonstrate another function

# def convert_cm_to_in(length_cm):
#     length_in_inches = length_cm / 2.54
#     return length_in_inches

# print(convert_cm_to_in(20))


#Find the min value
numbers = [4,7,10,1,2]
min_value = numbers[0] 
min_location = 0
index = 0

for num in numbers:
    if num < min_value:
        min_value = num
        min_location = index
    index += 1

print(min_value, min_location)