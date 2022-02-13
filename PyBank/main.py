import csv
from os import path

basepath=path.dirname(__file__)
filepath = path.abspath(path.join(basepath,'Resources/budget_data.csv'))
filepath1 = path.abspath(path.join(basepath,'analysis/text_file.txt'))
with open(filepath, 'r') as ed:
    csv_reader = csv.reader(ed)
    next(csv_reader)
    date=[]
    P_L=[]
   
    for line in csv_reader:
        date.append(line[0])
        P_L.append(int(line[1]))
       
    
    # print(P_L)
    
    total = 0
    for i in P_L:
        total+=(i)

    
    change  = []
    for i in range(len(P_L)):
        if i == (len(P_L)-1):
            break
        change.append(P_L[i+1]-P_L[i])
    change.insert(0,0)



    average_change = sum(change)/85

    high = max(change)
    low = min(change)
    high_index = change.index(high)
    low_index  = change.index(low)
    
    print("Financial Analysis\n -------------------------\n "
        "Total Months:{} \n Total: ${}\n Average Change: ${:.2f}\n"
         " Greatest Increase in Profits: {} (${}) \n "
        "Greatest Decrease in Profits: {} (${})".format(len(date),total,
        average_change, date[high_index],high, date[low_index], low))
    
    
    with open(filepath1, 'w') as o:
        o.write("Financial Analysis\n -------------------------\n "
        "Total Months:{} \n Total: ${}\n Average Change: ${:.2f}\n"
         " Greatest Increase in Profits: {} (${}) \n "
        "Greatest Decrease in Profits: {} (${})".format(len(date),total,
        average_change, date[high_index],high, date[low_index], low))
