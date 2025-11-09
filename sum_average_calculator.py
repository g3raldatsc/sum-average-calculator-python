def main():
    print("Sum and Average Calculator\n")
    try:
        numbers = input("Enter numbers separated by spaces: ").split()
        numbers = [float(num) for num in numbers]
        if not numbers:
            print("No numbers entered.")
            return
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    total = sum(numbers)
    average = total / len(numbers)

    print("\nResults:")
    print(f"Numbers entered: {numbers}")
    print(f"Total: {total}")
    print(f"Average: {average}")

if __name__ == "__main__":
    main()