# Data Analyzer and Transformer Program

data = []

while True:

    print("\n===== DATA ANALYZER AND TRANSFORMER =====")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data by Threshold")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # 1. Input Data
    if choice == "1":

        data = input("Enter numbers separated by space: ").split()

        # Convert into integers
        for i in range(len(data)):
            data[i] = int(data[i])

        print("Data entered successfully!")
        print("Data:", data)

    # 2. Display Data Summary
    elif choice == "2":

        if len(data) == 0:
            print("Please enter data first!")

        else:
            print("\nData Summary")
            print("Total elements:", len(data))
            print("Minimum value:", min(data))
            print("Maximum value:", max(data))
            print("Sum:", sum(data))
            print("Average:", sum(data) / len(data))

    # 3. Calculate Factorial
    elif choice == "3":

        number = int(input("Enter a number: "))

        factorial = 1

        for i in range(1, number + 1):
            factorial = factorial * i

        print("Factorial:", factorial)

    # 4. Filter Data by Threshold
    elif choice == "4":

        if len(data) == 0:
            print("Please enter data first!")

        else:
            threshold = int(input("Enter threshold value: "))

            result = []

            for x in data:
                if x >= threshold:
                    result.append(x)

            print("Filtered data:", result)

    # 5. Sort Data
    elif choice == "5":

        if len(data) == 0:
            print("Please enter data first!")

        else:
            print("1. Ascending")
            print("2. Descending")

            option = input("Enter choice: ")

            if option == "1":
                data.sort()
                print("Ascending order:", data)

            elif option == "2":
                data.sort(reverse=True)
                print("Descending order:", data)

            else:
                print("Invalid choice!")

    # 6. Dataset Statistics
    elif choice == "6":

        if len(data) == 0:
            print("Please enter data first!")

        else:
            minimum = min(data)
            maximum = max(data)
            total = sum(data)
            average = total / len(data)

            print("\nDataset Statistics")
            print("Minimum:", minimum)
            print("Maximum:", maximum)
            print("Total:", total)
            print("Average:", average)

    # 7. Exit
    elif choice == "7":

        print("Thank you!")
        break

    else:
        print("Invalid choice!")