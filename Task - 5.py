# Question 1:

data = [10,501,22,37,100,999,87,351]
result = filter (lambda x:x>4, data)
print(list(result))


# Question 2:

arr=[1,2,3,4] 
v=8
x=lambda arr,v: True if v in arr else False
  
if(x(arr,v)): 
  print("Element is Present in the list") 
else: 
  print("Element is Not Present in the list")


# Question 3:
from functools import reduce
 
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
                                 range(n-2), [0, 1])
 
print(fib(10))



# Question 4:

 # Part a:

import re
# Regular Expression for validating an email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
 
# Define a function for validating an Email
def check(email):
 
    # pass the regular expression and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        print("Valid Email")
 
    else:
        print("Invalid Email")
 
# Driver Code
if __name__ == '__main__':
 
    # Enter the email
    email = "ankit326@gmail.com"

    # Check  the email
    check(email)


    # Part b:
    import re
     # Define a function for Validating Phone number
    def validate_phone_number(regex, phone_number):
        match = re.search(regex, phone_number)
        if match:
            return True
        return False
    
    # Pass the regular expression and complie method 
    pattern = re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}")

    
    test_phone_number = [
        "+880-431-123-2345"

    ]

    for number in test_phone_number:
        print(f"{number}: {validate_phone_number(pattern, number)}")



    # Part c:

    import re
     # Define a function for Validating Phone number
    def validate_phone_number(regex, phone_number):
        match = re.search(regex, phone_number)
        if match:
            return True
        return False
    
    # Pass the regular expression and complie method 
    pattern = re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}")

    
    test_phone_number = [
        "+1-325-1234-5678"

    ]

    for number in test_phone_number:
        print(f"{number}: {validate_phone_number(pattern, number)}")
        
    
# Part d:
def main():
    passwd = 'Geek12@'
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
     
    # compiling regex
    pat = re.compile(reg)
     
    # searching regex                 
    mat = re.search(pat, passwd)
     
    # validating conditions
    if mat:
        print("Password is valid.")
    else:
        print("Password invalid !!")
 
# Driver Code     
if __name__ == '__main__':
    main()
        


