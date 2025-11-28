#Usecase for the stack
#Balanced Parenthesis Checker
#The problem - given a string of chars - determine if brackets, braces etc are balanced
#Useful for compiler logic
from stack import Stack

def parenthesis_checker(input):
    s1 = Stack(len(input))
    if(len(input) == 0):
        return 'Fail - Input Empty'
    else:
        for x in input:
            #Checks that the ASCII value of the input is a opening bracket
            if(ord(x) == 40 or ord(x) == 91 or ord(x) == 123):
                s1.push(x)
        #once all pushing is done

        
     
    



input_string1 = "[{()}]" #Pass the test
input_string2 = "((()})" #fail (mixed values)
input_string3 = "((())" #fail (missing closing)
input_string4 = "" #fail (empty)

print(parenthesis_checker(input_string1))
print(parenthesis_checker(input_string2))
print(parenthesis_checker(input_string3))
print(parenthesis_checker(input_string4))




