

menu_stocks = {}
stocks = {}
num= None

def init():
    global menu_stocks, stocks 
    menu_stocks.clear() #init함수가 실행될 때마다 menu_stocks, stocks 딕셔너리를 초기화함.
    stocks.clear()

    with open('stf.csv', 'r', encoding="euckr") as f: 
        lines = f.readlines()

    for line in lines[1:]: #csv파일을 줄별로 읽은 후 ,를 구분점으로 각각 id값에 대응하는 name을 딕셔너리형태로 menu_stocks 딕셔너리에 넣고, name에 대응하는 amount,value값을 stocks 딕셔너리에 넣음.

        data = line.strip().split(',')
        id = int(data[0])
        name = data[1]
        amount = int(data[2])
        value = int(data[3])    
        
        menu_stocks[id] = name
        stocks[name] = [amount, value]#3단 논법과 같이, id값은 각각의 name에 대응하는 amount,value값과 간접적으로 대응함.


def sell(key, count): 
    global stocks
    print(f"Sell {key}, amount:{stocks[key][0]}")
    if stocks[key][0] >= count:
        stocks[key][0] = stocks[key][0] - count
        print(f"sell {key}: {stocks[key][1] * count}")
        
        with open('stf.csv', 'r', encoding="euckr") as f:
            lines = f.readlines()

        item_index = 0
        for line in lines:
            if line.split(',')[1] == key:
                break
            item_index += 1

        data = lines[item_index].strip().split(',')
        data[2] = str(stocks[key][0])  
        lines[item_index] = ','.join(data) +'\n'
        
        with open('stf.csv', 'w', encoding="euckr") as f:
            for line in lines[:-1]:  
                f.write(line)  
            f.write(lines[-1].strip())  
    else:
        print(f"Cannot sell {key}")


def plus_stock(name, amount, price):

    if len(stocks) <=90:
        with open('stf.csv', 'r', encoding="euckr") as f:
            lines = f.readlines()
        if len(lines) > 1:
            last_line = lines[-1]
            last_id = int(last_line.split(',')[0])
            next_id = last_id + 1
        else:
            last_id=0
            next_id = last_id+1
        if next_id in [97,98,99]: #0,97,98,99는 품목의 id로 사용될 수 없기 때문에 해당 숫자가 id로 배정될 경우 100,101,102로 배정되게 만들었음.
            next_id += 3
        
        with open('stf.csv', 'a', encoding="euckr") as f:
            added_stock = [str(next_id), name, amount, price]
            added_stock_str = ",".join(added_stock) + '\n'
            f.write(added_stock_str)
    else:
        print("Total Item number cannot exceed 90.") #기본적으로 예외처리는 하지 않아야하지만, 90개 이상으로 품목이 넘어가면 안된다는 가정 때문에 혹시나 해서 넣음.
        


def delete_stock():
    global num
    print("===Choosing Deleted Item===")
    for key, item in menu_stocks.items():
        print(f"{key}.{item}")
    print("===========================")

    num = int(input("Enter Choice:"))

    with open('stf.csv', 'r', encoding="euckr") as f:
        lines = f.readlines()
    update_lines = [lines[0]]
    for line in lines[1:]:
        data = line.strip().split(',')
        if int(data[0]) != num:
            if int(data[0])> num:
                data[0] = str(int(data[0]))
            updated_line = ','.join(data) + '\n'
            update_lines.append(updated_line)
    with open('stf.csv', 'w', encoding="euckr") as f:
        f.writelines(update_lines)


def debuging(*args):
    with open('history.csv','a',encoding="euckr") as f:
        for arg in args:
            f.write(f"{arg}\n")

def debuging_reset():
    with open('history.csv','w',encoding="euckr") as f:
        f.write('')

def stock_management():
    print


def print_store():
    print("==========STF============")
    for key, item in stocks.items():
        print(f"{key}:{item}")
    print("=========================")
    
def print_menu():
    print("0. View Item")
    for key, item in menu_stocks.items():
        print(f"{key}. Buy {item}")  
    print("97. Plus Item")  
    print("98. Delete Item")
    print("99. Bye")
    print("=========================")


init()
debuging_reset()
while True:
    print_store()
    print_menu()

    choice = int(input("Enter Choice:"))

    if choice == 99:
        debuging(choice)
        break
    elif choice == 98:
        delete_stock()
        init()
        debuging(choice,num)
    elif choice == 97:
        n = input("Enter Item Name:")
        a = input("Enter Item Amount:")
        v = input("Enter Item Value:")
        plus_stock(n,a,v)
        init()
        debuging(choice,n,a,v)
    elif choice == 0:
        print("=======Item List=======")
        for key, item in stocks.items():
            print(f"{key}:{item[0]}")
        print(" - - - - - - - - - - - ")
        debuging(choice)
    else:
        amount = int(input("Enter amount:"))
        sell(menu_stocks[choice], amount)
        init()
        debuging(choice,amount)