
class calculator():

    @staticmethod
    def calculate(num1, num2, operator):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "ERROR: Division by zero"
            return num1/num2
        else:
            return "ERROR: Invalid operator"


    if __name__ == '__main__':
        while True:
            num1_input = input("Enter number 1: ")
            if num1_input.lower() == 'quit':
                break
            try:
                num1 = float(num1_input)
            except ValueError:
                print("ERROR: Enter a valid number")
                continue

            num2_input = input("Enter number 2: ")
            if num2_input.lower() == 'quit':
                break
            try:
                num2 = float(num2_input)
            except ValueError:
                print("ERROR: Enter a valid number")
                continue

            operator = input("Enter operator (+, -, *, /): ")
            result = calculate(num1, num2, operator)
            print(F"RESULT: {result}")