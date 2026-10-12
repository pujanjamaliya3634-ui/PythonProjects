
import os
from datetime import datetime

FILE_NAME = "journal.txt"


def add_entry():
    entry = input("\nEnter your journal entry: ")

    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(f"[{date_time}]\n")
        file.write(entry + "\n\n")

    print("\nEntry added successfully!")


def view_entries():
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        print("\nNo journal entries found. Start by adding a new entry!")
        return

    print("\nYour Journal Entries:")
    print("-" * 35)

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        print(file.read())


def search_entry():
    if not os.path.exists(FILE_NAME):
        print("\nError: The journal file does not exist. Please add a new entry first.")
        return

    keyword = input("\nEnter a keyword or date to search: ").lower()

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        content = file.read().strip()

    if not content:
        print("\nNo journal entries found.")
        return

    entries = content.split("\n\n")
    found = []

    for entry in entries:
        if keyword in entry.lower():
            found.append(entry)

    if found:
        print("\nMatching Entries:")
        print("-" * 35)

        for entry in found:
            print(entry)
            print()
    else:
        print(f"\nNo entries were found for the keyword: {keyword}.")


def delete_all_entries():
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        print("\nNo journal entries to delete.")
        return

    confirm = input(
        "\nAre you sure you want to delete all entries? (yes/no): "
    ).lower()

    if confirm == "yes":
        open(FILE_NAME, "w", encoding="utf-8").close()
        print("\nAll journal entries have been deleted.")
    else:
        print("\nDeletion cancelled.")


def main():
    while True:
        print("\n========== Welcome Menu ==========")
        print("Welcome to Personal Journal Manager!")
        print("Please select an option:\n")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_entry()

        elif choice == "2":
            view_entries()

        elif choice == "3":
            search_entry()

        elif choice == "4":
            delete_all_entries()

        elif choice == "5":
            print(
                "\nThank you for using Personal Journal Manager. Goodbye!"
            )
            break

        else:
            print(
                "\nInvalid option. Please select a valid option from the menu."
            )


if __name__ == "__main__":
    main()
    