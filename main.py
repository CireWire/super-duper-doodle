from summary import summary
from dataMining import datamining


def main():
    while True:
        # Display options to user
        print("Welcome to the EV Data Analysis Program!")
        print("Please select an option from the menu below:")
        print("1. Summary")
        print("2. Data Mining")
        print("3. Exit")

        # Prompt user for input
        user_input = input("Enter a number: ")

        if user_input == "1":
            # Run the summary function
            summary()

        elif user_input == "2":
            # Run the data mining function
            datamining()

        elif user_input == "3":
            # Exit the program
            print("Thank you for using the EV Data Analysis Program!")
            break

        else:
            # Invalid input
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
