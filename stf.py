import pandas as pd

menu_stocks = {}
stocks = {}

def init():
    f = open('stf.csv')
    f.readline()

    while True:
        token = f.readline()

        if not token:
            break
        
        tokens = token.split(',')
        menu_stocks[int(tokens[0])] = tokens[1]
        stocks[tokens[1]] = [int(tokens[2]), int(tokens[3])]
    pass

def sell(key, count):
    global stocks
    print(f"Sell {key}, amount:{stocks[key][0]}")
    if stocks[key][0] >= count:
        stocks[key][0] = stocks[key][0] - count
        print(f"sell {key}: {stocks[key][1] * count}")
    else:
        print("Cannot sell {key}")

def plus_stock(name, amount, price):
    with open('stf.csv','a') as f:
        f.write(name, amount, price)

def print_store():
    print("==========STF============")
    for key, item in stocks.items():
        print(f"{key}:{item}")

def print_menu():
    for key, item in menu_stocks.items():
        print(f"{key}. Buy {item}")    
    print("99. Bye")
    print("=========================")



init()
while True:
    print_store()
    print_menu()

    choice = int(input("Enter Choice:"))

    if choice != 99:
        if choice !=97:
            amount = int(input("Enter amount:"))
            sell(menu_stocks[choice], amount)
            pass
    elif choice == 97:
        input()
        plus_stock()
    elif choice == 99:
        break
    else:
        pass