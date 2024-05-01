class customer:
    def __init__(self,name,surname,password,balance,dept,deptDueDate):
        self.name = name
        self.surname = surname
        self.password = password
        self.balance = balance
        self.dept = dept
        self.deptDueDate = deptDueDate

johnAccount = customer("john","cena","1234",5000,1500,"06/03/2024")
onurAccount = customer("onur","eğe","1478",600,1200,"07/03/2024")

currentCard = onurAccount

class ATM:
    def __init__(self,atmName):
        self.name = atmName
        self.securityControl()
        self.loop = True

    def securityControl(self):
        right = 2

        for i in range(0,3):
            password = input("please enter your password:")

            if password == currentCard.password:
                self.program()
            elif password != currentCard.password and right != 0:
                print("wrong password!!! try again.")
                right -= 1
            elif password != currentCard.password and right == 0:
                print("wrong password 3 times. your card was blocked. please contact with nearest branch")
                exit()

    def program(self):
        choice = self.menu()

        if choice == 1:
            self.balance()
        if choice == 2:
            self.dept()
        if choice == 3:
            self.withdraw()
        if choice == 4:
            self.deposit()
        if choice == 5:
            self.exit()
    def menu(self):
        choice = int(input("hello, welcome to the {} dear {} {}\n\nplease choose the transaction that you want\n\n"
                          "[1]balance inquiry\n[2]dept inquiry\n[3]withdraw\n[4]deposit\n[5]exit\n\nchoice:"
                          "".format(self.name,currentCard.name,currentCard.surname)))
        while choice<0 or choice>5:
            print("please enter a integer between 1 and 5\nreturning to menu")
            self.program()

        return choice

    def balance(self):
        print("Balance:{} $".format(currentCard.balance))
        self.loop = False
        self.backToMenu()

    def dept(self):
        print("your credit card dept:{} $\npayment due date:{}".format(currentCard.dept,currentCard.deptDueDate))
        self.loop = False
        self.backToMenu()

    def withdraw(self):
        amount = int(input("please enter the amount of money that you want to withdraw"))

        if amount > currentCard.balance:
            print("there are not enough money on your account.")
            self.backToMenu()
        else:
            currentCard.balance = currentCard.balance - amount
            print("please take your money.\nyour new balance:{} $".format(currentCard.balance))
            self.backToMenu()
    def deposit(self):
        amount2 = int(input("please enter the amount of money that you want to deposit "))
        currentCard.balance += amount2
        print("your new balance:{} $".format(currentCard.balance))
        self.backToMenu()
    def exit(self):
        print("thank you for choosing us. Have nice a day")
        self.loop = False
        exit()
    def backToMenu(self):
        x = int(input("please enter 7 for returning menu. for exitting enter 5."))

        if x == 7:
            self.program()
        elif x == 5:
            self.exit()


bank = ATM("Xbank")

while bank.loop:
    bank.program()