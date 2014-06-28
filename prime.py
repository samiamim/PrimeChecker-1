num_check = int(input("Enter a number: ")) # Takes the input from the user and sets it to the variable num_check

if num_check > 1: # Prime numbers are greater than 1 (excluding 1 itself) so this is to filter out numbers less than 1 that cannot be prime
    for n in range(2,num_check): # Checks for factors
        if (num_check % n) == 0: # Here, if the division of the input (num_check) is equal to 0 then it cannot be a prime number.
            print(num_check, "is not a prime number") # If it fails the tests then it cannot be a prime number
            break

        else:
            print (num_check, "is a prime number!") #If it passes these tests they it is a prime number
            break
    else:
        print (num_check, "is not a prime number as it is equal or less than 1") # If the number is less than or equal to 1 then it is not prime.
