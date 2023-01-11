from function import sieve

if __name__ == "__main__":
    print("Type 'q' to quit")
    while True:
        user_input = input("Enter the upper bound of the set you want to check for prime numbers: ")

        if user_input.lower() == 'q':
            break

        # Assertion test
        try:
            user_input = int(user_input)
        except ValueError:
            print("\nGiven input is not a number!\n")
        else:
            print()
            # Function
            print(sieve(user_input))
            print()
