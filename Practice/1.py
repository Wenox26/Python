#SORTING USER INPUT ARRAYS FROM LOWEST TO HIGHEST


def main():
    userInput = input("Enter numbers in an array[separate numbers by spaces]:")

    numbers = [float(num) for num in userInput.split()]

    numbers.sort()

    print("Sorted numbers low to high")
    for num in numbers:
        print(num)

if __name__ == "__main__":
    main()

