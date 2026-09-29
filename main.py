
print("Welcome to the Data Analyzer and Transformer Program!")

data = []


def conv(data):
    """Convert 2D data into 1D data."""

    if len(data) > 0 and isinstance(data[0], list):
        l = []

        for x in data:
            l.extend(x)

        return l

    else:
        return data


def k_argment(**arg):
    """Display values using keyword arguments."""

    for x, y in arg.items():
        print(x.capitalize(), ":", y)


def input_data():   
    """Take 1D or 2D array input from the user and store the data."""

    global data

    print("\nChoose Array Type:")
    print("1. 1D Array")
    print("2. 2D Array")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        values = input(
            "Enter data for a 1D array (separated by spaces):\n"
        )

        data = list(map(int, values.split()))

        print("Data:", data)
        print("1D Data has been stored successfully!")

    elif choice == 2:

        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        data = []

        for i in range(rows):

            row = []

            for j in range(cols):

                value = int(
                    input(f"Enter value [{i}][{j}]: ")
                )

                row.append(value)

            data.append(row)

        print("Data:", data)
        print("2D Data has been stored successfully!")

    else:
        print("Invalid array choice!")


def display_summary():
    """Display basic summary of the dataset."""

    if len(data) <= 0:
        print("No data found!")
        return

    value = conv(data)

    print("\nData Summary:-")
    print("Minimum value:-", min(value))
    print("Maximum value:-", max(value))
    print("Sum of all values:-", sum(value))
    print("Total elements:-", len(value))

    avg = sum(value) / len(value)

    print("Average value:-", round(avg, 2))


def fact(num):
    """Calculate factorial of a number using recursion."""

    if num <= 1:
        return 1

    else:
        return num * fact(num - 1)


def filter_data():
    """Filter data based on a threshold using lambda function."""

    if len(data) == 0:
        print("No data found!")
        return

    threshold = int(
        input("Enter a threshold value to filter out the data: ")
    )

    values = conv(data)

    fil_data = list(
        filter(lambda i: i >= threshold, values)
    )

    print(
        f"Filtered Data (values >= {threshold}): {fil_data}"
    )


def sort_data():
    """Sort the data in ascending or descending order."""

    if len(data) == 0:
        print("Please input data first!")
        return

    # Convert 2D data into 1D data
    values = conv(data)

    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        sorted_data = sorted(values)

        print("\nSorted Data in Ascending Order:")
        print(*sorted_data, sep=", ")

    elif choice == 2:

        sorted_data = sorted(values, reverse=True)

        print("\nSorted Data in Descending Order:")
        print(*sorted_data, sep=", ")

    else:
        print("Invalid sorting choice!")


def dataset_statistics(data):
    """Return minimum, maximum, sum and average as multiple values."""

    values = conv(data)

    minimum = min(values)
    maximum = max(values)
    total = sum(values)
    average = total / len(values)

    return minimum, maximum, total, average


def display_dataset_statistics():
    """Display dataset statistics using dataset_statistics function."""

    if len(data) == 0:
        print("No data found!")
        return

    minimum, maximum, total, average = dataset_statistics(data)

    print("\nDataset Statistics:")
    print("Minimum Value:", minimum)
    print("Maximum Value:", maximum)
    print("Sum of Values:", total)
    print("Average Value:", round(average, 2))


while True:

    print("\nSelect option:")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values + **kwargs)")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        print(input_data.__doc__)
        input_data()

    elif choice == 2:

        print(display_summary.__doc__)
        display_summary()

    elif choice == 3:

        print(fact.__doc__)

        num = int(input("Enter a number: "))

        if num < 0:
            print("Factorial is not possible!")

        else:
            result = fact(num)
            print(f"Factorial of {num} is: {result}")

    elif choice == 4:

        print(filter_data.__doc__)
        filter_data()

    elif choice == 5:

        print(sort_data.__doc__)
        sort_data()

    elif choice == 6:

        print(dataset_statistics.__doc__)

        if len(data) == 0:
            print("No data found!")
            continue

        
        minimum, maximum, total, average = dataset_statistics(data)

        k_argment(
            minimum=minimum,
            maximum=maximum,
            total=total,
            average=round(average, 2)
        )

    elif choice == 7:

        print("Exiting...")
        break

    else:

        print("Invalid Choice!")
