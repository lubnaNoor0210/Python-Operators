def divide_numbers():
    try:
        num1 = float(input("Enter numerator:"))
        num2 = float(input("Enter denominator:"))
        result= num1/num2
    except ZeroDivisionError:
        print("Cannot divide by zero!")

    except ValueError:
        print("Please enter valid value")
    else:
        print(f"✅ Result: {result}")
    finally:
        print("🔚 Operation completed.")
divide_numbers()
    