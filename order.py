#input: csv file in current directory named "order.csv" which first column is the name of product you want, and second column is name of maker. 

import csv

print("〇〇株式会社")
print("〇〇様")
print("いつもお世話になっております。")
print("東京大学情報理工学研究科システム情報池内研究室の〇〇です。")
print("以下の製品のお見積もりをいただけないでしょうか。")
print("何卒よろしくお願い致します。")
print("\n")

with open('./order.csv') as f:
    reader = csv.reader(f)
    l = [row for row in reader]

    i = 0
    for i in range(len(l)):
    
        print("メーカ:" + l[i][0])
        print("製品名:" + l[i][1])
        print("個数:1")

        print("\n")

print("東京大学大学院情報理工学研究科システム情報学専攻池内研究室")
print("〇〇")
