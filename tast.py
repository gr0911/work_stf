def count_rows(filename):
    with open(filename, 'r', encoding="euckr") as f:
        row_count = sum(1 for line in f) - 1  # 첫 번째 행(헤더) 제외
    return row_count

filename = 'tast.csv'
total_rows = count_rows(filename)
print("Total rows in CSV file:", total_rows)


def plus_stock(name, amount, price):
    with open('tast.csv', 'a', encoding="euckr") as f:
        # 총 행 개수를 구하고 다음 ID 값 계산
        total_rows = count_rows('tast.csv')
        next_id = total_rows + 1

        # 새로운 행 추가
        added_stock = [str(next_id), name, amount, price]
        added_stock_str = ",".join(added_stock)
        f.write(added_stock_str + '\n')  # 줄바꿈 문자 추가


n=input()
a=input()
v=input()

plus_stock(n,a,v)