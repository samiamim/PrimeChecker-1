import math

def prime_checker():
    num_check = int(input("Enter a number: "))                                              # Takes the input from the user and sets it to the variable num_check

    sqr_test = math.sqrt(num_check)                                                         # Tests the number by square rooting it, if it returns an integar value then it cannot be a prime number
    sqr_test = int(sqr_test)
                                                                                            # Prime numbers are greater than 1 (excluding 1 itself) so this is to filter out numbers less than 1 that cannot be prime
    for n in range(sqr_test):                                                               # Checks for factors
        if num_check % (n+2) == 0:                                                          # Here, if the division of the input (num_check) is equal to 0 then it cannot be a prime number.
            print(num_check, "is not a prime number. It is a factor of ", n+2)              # If it fails the tests then it cannot be a prime number
            break
    else:
        print(num_check, "is a prime number!")


if __name__=='__main__':                                                                    # Runs the program
    prime_checker()
