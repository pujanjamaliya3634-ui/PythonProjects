print("Welcome to the Interactive Personal Data Collector!")
print()

# Get information from the user
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
favorite_number = int(input("Please enter your favourite number: "))

print()
print("Thank you! Here is the information we collected:")
print()


# Calculate approximate birth year
birth_year = 2023 - age

print("Your birth year is approximately: {birth_year} (based on your age of {age})")

print()

# Goodbye message
print("Thank you for using the Personal Data Collector. Goodbye!")