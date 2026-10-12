import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = None
current_plot = None


def create_sample_dataset():
    os.makedirs("data", exist_ok=True)

    data = {
        "SalesID": [101, 102, 103, 104, 105],
        "Product": [
            "Product A", "Product B", "Product C",
            "Product D", "Product E"
        ],
        "Region": [
            "North", "East", "West Coast", "South", "Central"
        ],
        "Sales": [500, 600, 700, 800, 550],
        "Year": [2022, 2022, 2022, 2022, 2022]
    }

    pd.DataFrame(data).to_csv("data/sales_data.csv", index=False)
    print("Sample dataset created: data/sales_data.csv")


def load_dataset():
    global df

    path = input(
        "Enter the path of the dataset (CSV file): "
    ).strip().strip('"')

    try:
        df = pd.read_csv(path)
        print("Dataset loaded successfully!")
        print(df.head())

    except FileNotFoundError:
        print("File not found.")
        choice = input(
            "Create a sample sales dataset? (yes/no): "
        ).lower()

        if choice == "yes":
            create_sample_dataset()
            df = pd.read_csv("data/sales_data.csv")
            print("Sample dataset loaded successfully!")
            print(df.head())

    except Exception as error:
        print("Error loading dataset:", error)


def explore_data():
    if df is None:
        print("Please load a dataset first.")
        return

    while True:
        print("\n== Explore Data ==")
        print("1. Display the first 5 rows")
        print("2. Display the last 5 rows")
        print("3. Display column names")
        print("4. Display data types")
        print("5. Display basic info")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(df.head())

        elif choice == "2":
            print(df.tail())

        elif choice == "3":
            print(list(df.columns))

        elif choice == "4":
            print(df.dtypes)

        elif choice == "5":
            df.info()

        elif choice == "6":
            break

        else:
            print("Invalid choice.")


def dataframe_operations():
    if df is None:
        print("Please load a dataset first.")
        return

    while True:
        print("\n== DataFrame Operations ==")
        print("1. Select a column")
        print("2. Filter rows")
        print("3. Sort data")
        print("4. Add a new column")
        print("5. Drop a column")
        print("6. Display current data")
        print("7. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            column = input("Enter column name: ")
            if column in df.columns:
                print(df[column])
            else:
                print("Column not found.")

        elif choice == "2":
            column = input("Enter column name: ")
            if column not in df.columns:
                print("Column not found.")
                continue

            value = input("Enter value to filter: ")
            matches = df[
                df[column].astype(str).str.lower()
                == value.lower()
            ]
            print(matches)

        elif choice == "3":
            column = input("Enter column name to sort: ")
            if column in df.columns:
                print(df.sort_values(by=column))
            else:
                print("Column not found.")

        elif choice == "4":
            column = input("Enter new column name: ")
            value = input("Enter value for all rows: ")
            df[column] = value
            print("Column added successfully!")
            print(df.head())

        elif choice == "5":
            column = input("Enter column name to drop: ")
            if column in df.columns:
                df.drop(columns=[column], inplace=True)
                print("Column dropped successfully!")
            else:
                print("Column not found.")

        elif choice == "6":
            print(df)

        elif choice == "7":
            break

        else:
            print("Invalid choice.")


def handle_missing_data():
    if df is None:
        print("Please load a dataset first.")
        return

    while True:
        print("\n== Handle Missing Data ==")
        print("1. Display rows with missing values")
        print("2. Fill missing values with mean")
        print("3. Drop rows with missing values")
        print("4. Replace missing values with a specific value")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            missing_rows = df[df.isnull().any(axis=1)]

            if missing_rows.empty:
                print("No missing values found in the dataset!")
            else:
                print(missing_rows)

        elif choice == "2":
            numeric_columns = df.select_dtypes(
                include="number"
            ).columns

            if len(numeric_columns) == 0:
                print("No numeric columns available.")
            else:
                for column in numeric_columns:
                    df[column] = df[column].fillna(
                        df[column].mean()
                    )
                print("Missing numeric values filled with mean.")

        elif choice == "3":
            df.dropna(inplace=True)
            df.reset_index(drop=True, inplace=True)
            print("Rows with missing values removed.")

        elif choice == "4":
            value = input("Enter replacement value: ")

            if value.lower() == "nan":
                print("Please enter a valid replacement value.")
                continue

            df.fillna(value, inplace=True)
            print("Missing values replaced successfully.")

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


def descriptive_statistics():
    if df is None:
        print("Please load a dataset first.")
        return

    print("\n== Descriptive Statistics ==")
    print("1. Display all statistics")
    print("2. Sum")
    print("3. Mean")
    print("4. Median")
    print("5. Minimum and Maximum")
    print("6. Standard Deviation")
    print("7. Back to Main Menu")

    choice = input("Enter your choice: ")
    numeric = df.select_dtypes(include="number")

    if numeric.empty:
        print("No numeric columns found.")
        return

    if choice == "1":
        print(df.describe(include="all"))

    elif choice == "2":
        print(numeric.sum())

    elif choice == "3":
        print(numeric.mean())

    elif choice == "4":
        print(numeric.median())

    elif choice == "5":
        print("Minimum:\n", numeric.min())
        print("Maximum:\n", numeric.max())

    elif choice == "6":
        print(numeric.std())

    elif choice == "7":
        return

    else:
        print("Invalid choice.")


def data_visualization():
    global current_plot

    if df is None:
        print("Please load a dataset first.")
        return

    while True:
        print("\n== Data Visualization ==")
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Stack Plot")
        print("7. Back to Main Menu")

        choice = input("Enter your choice: ")

        numeric = df.select_dtypes(include="number")

        if choice == "7":
            break

        if choice not in ("1", "2", "3", "4", "5", "6"):
            print("Invalid choice.")
            continue

        try:
            if choice in ("1", "2", "3"):
                x = input("Enter x-axis column name: ")

                if x not in df.columns:
                    print("Column not found.")
                    continue

            if choice in ("1", "2", "3"):
                y = input("Enter y-axis column name: ")

                if y not in df.columns:
                    print("Column not found.")
                    continue

                if not pd.api.types.is_numeric_dtype(df[y]):
                    print("The y-axis column must be numeric.")
                    continue

            plt.figure(figsize=(8, 5))

            if choice == "1":
                sns.barplot(data=df, x=x, y=y)
                plt.title("Bar Plot")

            elif choice == "2":
                plt.plot(df[x], df[y], marker="o")
                plt.xlabel(x)
                plt.ylabel(y)
                plt.title("Line Plot")

            elif choice == "3":
                plt.scatter(df[x], df[y])
                plt.xlabel(x)
                plt.ylabel(y)
                plt.title("Scatter Plot")

            elif choice == "4":
                if numeric.empty:
                    plt.close()
                    print("No numeric columns found.")
                    continue

                column = input("Enter column for pie chart: ")

                if column not in numeric.columns:
                    plt.close()
                    print("Enter a numeric column name.")
                    continue

                values = df[column].dropna()
                values = values[values >= 0]

                if values.empty or values.sum() == 0:
                    plt.close()
                    print("No suitable positive values to plot.")
                    continue

                plt.pie(
                    values,
                    labels=values.index.astype(str),
                    autopct="%1.1f%%"
                )
                plt.title("Pie Chart")

            elif choice == "5":
                if numeric.empty:
                    plt.close()
                    print("No numeric columns found.")
                    continue

                column = input("Enter column for histogram: ")

                if column not in numeric.columns:
                    plt.close()
                    print("Enter a numeric column name.")
                    continue

                plt.hist(df[column].dropna(), bins=10)
                plt.xlabel(column)
                plt.ylabel("Frequency")
                plt.title("Histogram")

            elif choice == "6":
                if numeric.empty:
                    plt.close()
                    print("No numeric columns found.")
                    continue

                print("Available numeric columns:")
                print(list(numeric.columns))

                columns = input(
                    "Enter columns separated by commas: "
                ).split(",")

                columns = [c.strip() for c in columns]

                if not columns or any(
                    c not in numeric.columns for c in columns
                ):
                    plt.close()
                    print("Invalid column names.")
                    continue

                values = numeric[columns].dropna()

                if values.empty:
                    plt.close()
                    print("No complete numeric rows available.")
                    continue

                plt.stackplot(
                    range(len(values)),
                    *[values[c].values for c in columns],
                    labels=columns
                )
                plt.legend(loc="upper left")
                plt.title("Stack Plot")
                plt.xlabel("Row")
                plt.ylabel("Value")

            plt.tight_layout()
            current_plot = plt.gcf()
            print("Generating plot...")
            plt.show()
            print("Plot generated successfully!")

        except Exception as error:
            plt.close("all")
            current_plot = None
            print("Unable to generate plot:", error)


def save_visualization():
    if current_plot is None:
        print("Please generate a visualization first.")
        return

    filename = input(
        "Enter file name to save the plot (e.g., scatter_plot.png): "
    ).strip()

    if not filename:
        print("File name cannot be empty.")
        return

    if not filename.lower().endswith(
        (".png", ".jpg", ".jpeg", ".pdf")
    ):
        filename += ".png"

    try:
        current_plot.savefig(filename, bbox_inches="tight")
        print(f"Visualization saved as {filename} successfully!")
    except Exception as error:
        print("Unable to save visualization:", error)


def main():
    while True:
        print("\n========== Data Analysis & Visualization Program ==========")
        print("Please select an option:")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
        print("=" * 60)

        choice = input("\nEnter your choice: ")

        if choice == "1":
            load_dataset()
        elif choice == "2":
            explore_data()
        elif choice == "3":
            dataframe_operations()
        elif choice == "4":
            handle_missing_data()
        elif choice == "5":
            descriptive_statistics()
        elif choice == "6":
            data_visualization()
        elif choice == "7":
            save_visualization()
        elif choice == "8":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option.")


if __name__ == "__main__":
    main()
