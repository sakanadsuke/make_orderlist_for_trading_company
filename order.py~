#input: csv file in current directory named "order.csv" which first column is the name of product you want, and second column is name of maker. 

import csv

with open('./order.csv') as f:
    reader = csv.reader(f)
    l = [row for row in reader]

    i = 0
    for i in range(len(l)):
    
        print("製品名:" + l[i][0])
        print("メーカ:" + l[i][1])
        print("個数:1")

        print("\n")
