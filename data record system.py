import re
import time
class record:
    def __init__(self,name):
        self.name = name
        self.loop = True
    def program(self):
        choice = int(self.menu())

        if choice == 1:
            print("you are being directed to addRecord menu")
            time.sleep(3)
            self.addRecord()

        if choice == 2:
            print("you are being directed to deleteRecord menu")
            time.sleep(3)
            self.deleteRecord()

        if choice == 3:
            print("you are being directed to getRecord menu")
            time.sleep(3)
            self.getRecord()

        if choice == 4:
            print("exiting...")
            time.sleep(3)
            self.exitProgram()

    def menu(self):
        def control(choice):
            if re.search("[^1-4]",choice):
                raise Exception("please enter a number between 1-4")
            elif len(choice) != 1:
                raise Exception("please enter a number between 1-4")

        while True:
            try:
                choice = input("hello , welcome to the {}'s data record system...\n\nplease enter the operation that you want\n[1]addRecord\n[2]deleteRecord\n[3]getRecord\n[4]exit\n".format(self.name))
                control(choice)
            except Exception as error:
                print(error)
                time.sleep(3)
            else:
                break

        return choice
    def addRecord(self):
        def checkname(name):
            if name.isalpha() == False:
                raise Exception("Your name should contain only alphabatic charecter")

        while True:
            try:
                name = input("please enter your name: ")
                checkname(name)
            except Exception as nameError:
                print(nameError)
                time.sleep(3)
            else:
                break

        def checksurname(surname):
            if surname.isalpha() == False:
                raise Exception("Your surname should contain only alphabatic charecter")

        while True:
            try:
                surname = input("please enter your surname: ")
                checksurname(surname)
            except Exception as surnameError:
                print(surnameError)
                time.sleep(3)
            else:
                break

        def checkage(age):
            if age.isdigit() == False:
                raise Exception("Your age should contain only numeric charecter")

        while True:
            try:
                age = input("please enter your age: ")
                checkage(age)
            except Exception as ageError:
                print(ageError)
                time.sleep(3)
            else:
                break

        def checkTC(Tc):
            if Tc.isdigit() == False or len(Tc) !=11:
                raise Exception("please enter correct Tc")

        while True:
            try:
                Tc = input("please enter Tc")
                checkTC(Tc)
            except Exception as TcError:
                print(TcError)
                time.sleep(3)
            else:
                break

        def checkMail(mail):
            if not re.search("@" and ".com",mail):
                raise Exception("please enter correct mail")

        while True:
            try:
                mail = input("please enter mail:")
                checkMail(mail)
            except Exception as mailError:
                print(mailError)
                time.sleep(3)
            else:
                break

        with open("ex1.txt",'r',encoding="utf-8") as doc:
            numberOfRecords = doc.readlines()

        id = len(numberOfRecords) + 1

        with open("ex1.txt",'a+',encoding="utf-8") as doc:
            doc.write("{}- {} {} {} {} {}\n".format(id,name,surname,age,Tc,mail))
            print("addRecord work succesfully")
        self.backToMenu()

    def deleteRecord(self):
        x = input("please enter id of record that want to delete:")

        with open("ex1.txt","r",encoding="utf-8") as doc:
            list = []
            list2 = doc.readlines()
            for i in range(0,len(list2)):
                list.append(list2[i].split("-")[0])

        del list2[list.index(x)]

        with open("ex1.txt","w+",encoding="utf-8") as newdoc:
            id =1
            for i in list2:
                newdoc.write("{}- {}\n".format(id,i.split("-")[1]))
                id += 1

        print("record is deleting...\n")
        time.sleep(3)
        print("succesfully deleted")
        self.backToMenu()

    def getRecord(self):

        with open("ex1.txt","r",encoding="utf-8") as doc:
            for i in doc:
                print(i)

        self.backToMenu()

    def exitProgram(self):

        print("exiting... thank you")
        time.sleep(3)
        self.loop = False
        exit()

    def backToMenu(self):

        while True:
            x = int(input("press 5 to back to menu or press 6 for exiting: "))

            if x == 5:
                print("main menu opening...")
                time.sleep(3)
                self.program()
                break

            if x == 6:
                print("exiting...")
                time.sleep(3)
                self.exitProgram()
                break
            else:
                print("please enter a correct number")


system = record('onur')

while system.loop:
    system.program()