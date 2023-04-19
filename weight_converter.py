def kg_to_lb(weight):
    """Converts weight from kilograms to pounds."""
    return weight * 2.20462

def lb_to_kg(weight):
    """Converts weight from pounds to kilograms."""
    return weight / 2.20462

def main():
    print("Welcome to Weight Converter!")
    while True:
        weight = float(input("Enter weight: "))
        unit = input("Is it in kg or lb? ")
        if unit.lower() == "kg":
            result = kg_to_lb(weight)
            print(f"{weight} kg = {result} lb\n")
        elif unit.lower() == "lb":
            result = lb_to_kg(weight)
            print(f"{weight} lb = {result} kg\n")
        else:
            print("Invalid input. Please enter either 'kg' or 'lb'.\n")
        choice = input("Do you want to convert another weight? (y/n) ")
        if choice.lower() != "y":
            break

if __name__ == "__main__":
    main()
