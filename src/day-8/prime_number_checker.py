def prime_checker(number):
    checker = 2
    prime_number = True
    go = True
    while go:
        if number % checker == 0 and checker != number:
            prime_number = False
            go = False
        elif checker == number - 1:
            go = False
        checker += 1
    if prime_number or number == 1:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number:"))

prime_checker(number=n)
 