


class playwith_numbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def substract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b


if __name__ == '__main__':
    a = int(input('Enter firt number :'))
    b = int(input('Enter second nummer :'))
    choice = 1
    while(choice!=0):
        ob = playwith_numbers(a, b)
        print("Addition is ",ob.add())
        print(f"Substraction is {ob.substract()}")
        print("Multiplication is ",ob.multiply())
        choice = int(input("Enter 0 to exit or 1 to continue :"))




