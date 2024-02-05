name = None
balance = 50000
name = input("name: ")

def balance_check():
    print("------Balance Check------")
    print(f"Hello {name}, Your Balance: {balance}")


def deposit(num):
    print("------Deposit------")
    global balance
    balance += num
    print(f"Hello {name}, Successfully received {num}, Your Balance: {balance}")

def withdrawl(num):
    print("------Withdrawl------")
    global balance
    balance -= num
    print(f"Hello, Your Banlance: {balance}")

def menu():
    print("------Menu------")
    print("balance check\t1")
    print("Deposit\t\t2")
    print("Withdrawl\t3")
    print("Exit\t\t4")
    return input("Your Choice: ")

while True:
    keyboard = menu()
    if keyboard == "1":
        balance_check()
        continue
    elif keyboard == "2":
        num = int(input("Amount Deposited: "))
        deposit(num)
        continue
    elif keyboard == "3":
        num = int(input("Amount to Withdraw: "))
        withdrawl(num)
        continue
    else:
        print("quit")
        break
    
