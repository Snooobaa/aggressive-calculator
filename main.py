
def main():
    num1 = input("Enter first number:")
    if num1.isnumeric == False:
        print("go screw yourself")
        exit()
        
    num2 = input("Enter second number:")
    if num2.isnumeric == False:
        print("go screw yourself")
        exit()
    
    num1 = int(num1)
    num2 = int(num2)

    print("Select from the following:")
    print("1. Addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")
    option = input()

    if option.isnumeric() == False:
        print("go screw yourself")
        exit()
    elif option == "1":
        print(f"your answer is {addition(num1, num2)}")
    elif option == "2":
        print(f"your answer is {subtraction(num1, num2)}")
    elif option == "3":
        print(f"your answer is {multiplication(num1, num2)}")
    elif option == "4":
        print(f"your answer is {division(num1, num2)}")
    else:
        print("that's not an option screw yourself")
        exit()



def addition(num1, num2) -> int:
    return num1 + num2

def subtraction(num1, num2) -> int:
    return num1 - num2

def multiplication(num1, num2) -> int:
    return num1 * num2

def division(num1, num2) -> int:
    return num1 / num2

main()