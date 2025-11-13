while True:
    print("=================================================================")
    print("Welcome to the Pattern Generator and Number Analyzer")
    print("=================================================================")
    print("Select an option:")
    print("1. Generate pattern")
    print("2. Analyze a range of numbers")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("You chose: Generate pattern")
            for i in range(1, 6):
                for j in range(i):
                    print("*", end=" ")
                print()  

        case 2:
            print("You chose: Analyze a range of numbers")
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            total_sum = 0

            for num in range(start, end + 1):
                if num % 2 == 0:
                    print(f"Number {num} is Even")
                else:
                    print(f"Number {num} is Odd")
                total_sum += num

            print(f"Sum of all numbers from {start} to {end} is: {total_sum}")

        case 3:
            print("Exiting program. Goodbye!")
            break  

        case _:
            print("Invalid choice. Please try again.")

    
        
        
        
        
        
        
   



















