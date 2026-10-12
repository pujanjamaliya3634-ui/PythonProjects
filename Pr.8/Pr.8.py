
import numpy as np


def create_array():
    print("\nArray Creation:")
    print("1. 1D Array")
    print("2. 2D Array")
    print("3. 3D Array")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("Enter number of elements: "))
            if n <= 0:
                print("Size must be positive.")
                return None
            values = list(map(float, input(
                f"Enter {n} elements separated by space: "
            ).split()))
            if len(values) != n:
                print("Incorrect number of elements.")
                return None
            arr = np.array(values)

        elif choice == 2:
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))

            if rows <= 0 or cols <= 0:
                print("Dimensions must be positive.")
                return None

            total = rows * cols
            values = list(map(float, input(
                f"Enter {total} elements separated by space: "
            ).split()))

            if len(values) != total:
                print("Incorrect number of elements.")
                return None

            arr = np.array(values).reshape(rows, cols)

        elif choice == 3:
            depth = int(input("Enter the number of layers: "))
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))

            if min(depth, rows, cols) <= 0:
                print("Dimensions must be positive.")
                return None

            total = depth * rows * cols
            values = list(map(float, input(
                f"Enter {total} elements separated by space: "
            ).split()))

            if len(values) != total:
                print("Incorrect number of elements.")
                return None

            arr = np.array(values).reshape(depth, rows, cols)

        else:
            print("Invalid choice.")
            return None

        print("\nArray created successfully:")
        print(arr)
        return arr

    except ValueError:
        print("Please enter valid numbers.")
        return None


def mathematical_operations(arr):
    print("\nMathematical Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = int(input("Enter your choice: "))

        if choice not in (1, 2, 3, 4):
            print("Invalid choice.")
            return

        values = list(map(float, input(
            f"Enter the same-size array elements "
            f"({arr.size} elements separated by space): "
        ).split()))

        if len(values) != arr.size:
            print("Incorrect number of elements.")
            return

        second = np.array(values).reshape(arr.shape)

        print("\nOriginal Array:")
        print(arr)
        print("\nSecond Array:")
        print(second)

        if choice == 1:
            result = arr + second
            name = "Addition"
        elif choice == 2:
            result = arr - second
            name = "Subtraction"
        elif choice == 3:
            result = arr * second
            name = "Multiplication"
        else:
            if np.any(second == 0):
                print("Error: Division by zero is not allowed.")
                return
            result = arr / second
            name = "Division"

        print(f"\nResult of {name}:")
        print(result)

    except ValueError:
        print("Please enter valid numbers.")


def combine_split_arrays(arr):
    print("\nCombine or Split Arrays:")
    print("1. Combine Arrays")
    print("2. Split Array")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            values = list(map(float, input(
                f"Enter the elements of another array to combine "
                f"({arr.size} elements separated by space): "
            ).split()))

            if len(values) != arr.size:
                print("Incorrect number of elements.")
                return

            second = np.array(values).reshape(arr.shape)

            print("\nOriginal Array:")
            print(arr)
            print("\nSecond Array:")
            print(second)

            axis = 0 if arr.ndim == 1 else 0
            result = np.concatenate((arr, second), axis=axis)

            print("\nCombined Array:")
            print(result)

        except ValueError:
            print("Invalid input.")

    elif choice == "2":
        if arr.shape[0] < 2:
            print("Array needs at least two rows/elements to split.")
            return

        try:
            parts = int(input("Enter number of parts (2 or more): "))
            if parts < 2 or parts > arr.shape[0]:
                print("Parts must be between 2 and the first dimension.")
                return

            results = np.array_split(arr, parts, axis=0)

            print("\nSplit Arrays:")
            for i, part in enumerate(results, start=1):
                print(f"Part {i}:")
                print(part)

        except ValueError:
            print("Enter a valid integer.")

    else:
        print("Invalid choice.")


def search_sort_filter(arr):
    print("\nSearch, Sort, and Filter:")
    print("1. Search a value")
    print("2. Sort the array")
    print("3. Filter values")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            value = float(input("Enter value to search: "))
            positions = np.argwhere(arr == value)

            if positions.size:
                print("Value found at index/indices:")
                print(positions)
            else:
                print("Value not found.")

        except ValueError:
            print("Enter a valid number.")

    elif choice == "2":
        print("\nOriginal Array:")
        print(arr)

        result = np.sort(arr, axis=-1)

        print("\nSorted Array:")
        print(result)
        print("(Sorting applied row-wise.)")

    elif choice == "3":
        try:
            limit = float(input("Filter values greater than: "))
            result = arr[arr > limit]

            print("\nFiltered Values:")
            print(result)

        except ValueError:
            print("Enter a valid number.")

    else:
        print("Invalid choice.")


def aggregates_statistics(arr):
    print("\nAggregates and Statistics:")
    print("1. Sum")
    print("2. Mean")
    print("3. Median")
    print("4. Standard Deviation")
    print("5. Variance")

    choice = input("Enter your choice: ")

    print("\nOriginal Array:")
    print(arr)

    if choice == "1":
        print("Sum of Array:", np.sum(arr))
    elif choice == "2":
        print("Mean of Array:", np.mean(arr))
    elif choice == "3":
        print("Median of Array:", np.median(arr))
    elif choice == "4":
        print("Standard Deviation:", np.std(arr))
    elif choice == "5":
        print("Variance:", np.var(arr))
    else:
        print("Invalid choice.")


def main():
    arr = None

    while True:
        print("\n====================================")
        print("Welcome to the NumPy Analyzer!")
        print("====================================")
        print("Choose an option:")
        print("1. Create a NumPy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            new_arr = create_array()
            if new_arr is not None:
                arr = new_arr

        elif choice in ("2", "3", "4", "5"):
            if arr is None:
                print("\nPlease create an array first using option 1.")
                continue

            if choice == "2":
                mathematical_operations(arr)
            elif choice == "3":
                combine_split_arrays(arr)
            elif choice == "4":
                search_sort_filter(arr)
            elif choice == "5":
                aggregates_statistics(arr)

        elif choice == "6":
            print("\nThank you for using the NumPy Analyzer! Goodbye!")
            break

        else:
            print("Invalid option. Please select a valid option.")


if __name__ == "__main__":
    main()
