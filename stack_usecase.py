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
            # Close Bracket Check
            elif(ord(x) == 41):
                if(s1.top == -1):
                    return 'Fail - Closing without an open'
                peeked_char = s1.peek()
                if(ord(peeked_char) == 40):
                    s1.pop()
                else:
                    return 'Fail - Incorrect Closing'
            elif(ord(x) == 93):
                if(s1.top == -1):
                    return 'Fail - Closing without an open'
                peeked_char = s1.peek()
                if(ord(peeked_char) == 91):
                    s1.pop()
                else:
                    return 'Fail - Incorrect Closing'
            elif(ord(x) == 125):
                if(s1.top == -1):
                    return 'Fail - Closing without an open'
                peeked_char = s1.peek()
                if(ord(peeked_char) == 123):
                    s1.pop()
                else:
                    return 'Fail - Incorrect Closing'
        #if leaves the for loop and is empty - it must have passed
        if(s1.top != -1):
            return 'Fail - missing a closer'
        else:
            return 'Pass'
        #once all pushing is done

        
     
    



input_string1 = "[{()}]" #Pass the test
input_string2 = "((()})" #fail (mixed values)
input_string3 = "((())" #fail (missing closing)
input_string4 = "" #fail (empty)
input_string5 = ")())" #fail (starts with a closing)
input_string6 = "()))" #fail (ends with 3 closing)

print(parenthesis_checker(input_string1))
print(parenthesis_checker(input_string2))
print(parenthesis_checker(input_string3))
print(parenthesis_checker(input_string4))
print(parenthesis_checker(input_string5))
print(parenthesis_checker(input_string6))
