class account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit_counter(self):
        print("How much money do you want to put on your deposit?")
        self.minus = int(input())
        self.deposit = 0
        if self.balance == 0:
            print("Your balance its 0")
            exit()
        elif self.deposit >= 0 and self.balance >= 0 and self.balance >= self.minus:
            self.deposit = self.minus
            self.balance -= self.minus
            print("Your deposit: ", self.deposit)
            print(f"Your balance: {self.balance}" )
        else:
            print("Negative balance")
            exit()


    def babkitratim(self):    
        self.withdraw = int(input())
        if self.balance == 0:
            print('Your balance its 0')
            exit()
        elif self.balance < self.withdraw:
            print('Withdraw can not be more then balance !')
            return 0
        else:
            self.balance -= self.withdraw
            print(f"Balance: {self.balance}")



print("Write your name: ")
owner = input().capitalize()

print(f"Hello, {owner}, how much money do you have ?")
balance = int(input())

person = account(owner, balance)

print("Choose option: deposit  or  withdraw")
option = input().lower()

non_stop = True
while non_stop:
    if option == "deposit":
        person.deposit_counter()
        print("Do you want one more deposit or make withdraw? Just print Y or N or W")
        answer = input().upper()
        if answer == "Y":
            person.deposit_counter()
        elif answer == "W":
            person.babkitratim()
        else:
            non_stop = False
    else:
        print("How much do you want pay ?")
        person.babkitratim()
        print("Do you want more or switch to deposit ? Just write Y or N or D")
        answer_2 = input().upper()
        if answer_2 == "Y":
            person.babkitratim()
        elif answer_2 == "D":
            person.deposit_counter()
        else:
            non_stop == False