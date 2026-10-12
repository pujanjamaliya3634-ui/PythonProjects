
import os
import math
import random
import string
import uuid
import secrets
import datetime
import time
import importlib


def datetime_operations():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Current Date and Time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        elif choice == "2":
            try:
                d1 = datetime.datetime.strptime(
                    input("Enter the first date (YYYY-MM-DD): "), "%Y-%m-%d"
                )
                d2 = datetime.datetime.strptime(
                    input("Enter the second date (YYYY-MM-DD): "), "%Y-%m-%d"
                )
                print("Difference:", abs((d2 - d1).days), "days")
            except ValueError:
                print("Invalid date format.")

        elif choice == "3":
            try:
                date = input("Enter date (YYYY-MM-DD): ")
                fmt = input("Enter format (example: %d-%m-%Y): ")
                parsed = datetime.datetime.strptime(date, "%Y-%m-%d")
                print("Formatted Date:", parsed.strftime(fmt))
            except ValueError:
                print("Invalid date or format.")

        elif choice == "4":
            input("Press Enter to start stopwatch...")
            start = time.time()
            input("Press Enter to stop stopwatch...")
            print("Elapsed time:", round(time.time() - start, 2), "seconds")

        elif choice == "5":
            try:
                seconds = int(input("Enter countdown seconds: "))
                if seconds < 0:
                    print("Enter a non-negative number.")
                    continue
                while seconds > 0:
                    print("Time remaining:", seconds, "seconds")
                    time.sleep(1)
                    seconds -= 1
                print("Time's up!")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "6":
            break

        else:
            print("Invalid option.")

        print("=" * 25)


def mathematical_operations():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                n = int(input("Enter a number: "))
                if n < 0:
                    print("Factorial is not defined for negative integers.")
                else:
                    print("Factorial:", math.factorial(n))
            except ValueError:
                print("Please enter an integer.")

        elif choice == "2":
            try:
                p = float(input("Enter principal amount: "))
                r = float(input("Enter rate of interest (in %): "))
                t = float(input("Enter time (in years): "))

                if p < 0 or r < 0 or t < 0:
                    print("Values cannot be negative.")
                else:
                    amount = p * (1 + r / 100) ** t
                    print("Compound Interest:", round(amount - p, 2))
                    print("Total Amount:", round(amount, 2))
            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "3":
            try:
                angle = float(input("Enter angle in degrees: "))
                radians = math.radians(angle)
                print("Sine:", round(math.sin(radians), 4))
                print("Cosine:", round(math.cos(radians), 4))
                print("Tangent:", round(math.tan(radians), 4))
            except ValueError:
                print("Please enter a valid angle.")

        elif choice == "4":
            print("1. Circle")
            print("2. Rectangle")
            print("3. Triangle")
            shape = input("Choose a shape: ")

            try:
                if shape == "1":
                    r = float(input("Enter radius: "))
                    print("Area:", round(math.pi * r * r, 2))

                elif shape == "2":
                    length = float(input("Enter length: "))
                    width = float(input("Enter width: "))
                    print("Area:", length * width)

                elif shape == "3":
                    base = float(input("Enter base: "))
                    height = float(input("Enter height: "))
                    print("Area:", 0.5 * base * height)

                else:
                    print("Invalid shape.")

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "5":
            break

        else:
            print("Invalid option.")

        print("=" * 25)


def random_data_generation():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                low = int(input("Enter minimum number: "))
                high = int(input("Enter maximum number: "))
                if low > high:--:
                 print("Minimum cannot exceed maximum.")
                else:
                    print("Random Number:", random.randint(low, high))
            except ValueError:
                print("Enter valid integers.")

        elif choice == "2":
            try:
                size = int(input("Enter list size: "))
                if not 1 <= size <= 10000:
                    print("Size must be between 1 and 10000.")
                else:
                    print("Random List:", [
                        random.randint(1, 100) for _ in range(size)
                    ])
            except ValueError:
                print("Enter a valid size.")

        elif choice == "3":
            try:
                length = int(input("Enter password length: "))
                if not 1 <= length <= 256:
                    print("Length must be between 1 and 256.")
                else:
                    chars = string.ascii_letters + string.digits + "!@#$%"
                    password = "".join(
                        secrets.choice(chars) for _ in range(length)
                    )
                    print("Generated Password:", password)
            except ValueError:
                print("Enter a valid length.")

        elif choice == "4":
            print("Generated OTP:", "".join(
                secrets.choice(string.digits) for _ in range(6)
            ))

        elif choice == "5":
            break

        else:
            print("Invalid option.")

        print("=" * 25)


def generate_uuid():
    print("\nGenerate Unique Identifiers:")
    print("Generated UUID:", uuid.uuid4())


def file_operations():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "5":
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid option.")
            continue

        filename = input("Enter file name: ").strip()

        if not filename:
            print("File name cannot be empty.")
            continue

        try:
            if choice == "1":
                with open(filename, "x", encoding="utf-8"):
                    pass
                print("File created successfully!")

            elif choice == "2":
                data = input("Enter data to write: ")
                with open(filename, "w", encoding="utf-8") as file:
                    file.write(data)
                print("Data written successfully!")

            elif choice == "3":
                with open(filename, "r", encoding="utf-8") as file:
                    print("File Content:\n" + file.read())

            elif choice == "4":
                data = input("Enter data to append: ")
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(data + "\n")
                print("Data appended successfully!")

        except FileExistsError:
            print("File already exists.")
        except FileNotFoundError:
            print("File not found. Create or write the file first.")
        except OSError as error:
            print("File error:", error)

        print("=" * 25)


def explore_module_attributes():
    print("\nExplore Module Attributes:")
    module_name = input("Enter module name to explore: ").strip()

    try:
        module = importlib.import_module(module_name)
        attributes = dir(module)
        print("Available Attributes in this module:")
        print(attributes[:50])
        print("Total attributes:", len(attributes))
    except ImportError:
        print("Module not found or could not be imported.")


def main():
    while True:
        print("\n==========================")
        print("Welcome to Multi-Utility Toolkit")
        print("==========================")
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        print("==========================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            datetime_operations()
        elif choice == "2":
            mathematical_operations()
        elif choice == "3":
            random_data_generation()
        elif choice == "4":
            generate_uuid()
        elif choice == "5":
            file_operations()
        elif choice == "6":
            explore_module_attributes()
        elif choice == "7":
            print("\nThank you for using the Multi-Utility Toolkit!")
            break
        else:
            print("Invalid option. Please select a valid option.")


if __name__ == "__main__":
    main()
