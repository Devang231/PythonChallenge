#!/usr/bin/env python
# coding: utf-8

# In[26]:


# import the os module
import os

# reading CSV files
import csv

csvpath = os.path.join("/Users/devangpatel/Desktop/PythonChallenge/PyBank/Resources/budget_data.csv")

Date = []
Profit_and_Losses = []
Change = []
Average_Change = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    for column in csvreader:
        Date.append(column[0])
        Profit_and_Losses.append(int(column[1]))
        

Total_Months = len(Date)
Total_Profits = sum(Profit_and_Losses)

for column in range (0, len(Profit_and_Losses)-1):
    Change.append(int(Profit_and_Losses[column+1])-(int(Profit_and_Losses[column])))

Average_Change = sum(Change) / len(Change)

Max = max(Change)

Min = min(Change)

Increase_month = Date[Change.index(Max) + 1]

Decrease_month = Date[Change.index(Min) + 1]

print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total profits = ${Total_Profits}")
print(f"Average Change: (${Average_Change})")
print(f"Greatest Increase in Profits: {Increase_month} (${Max})")
print(f"Greatest Decrease in Profits: {Decrease_month} (${Min})")

output_path = os.path.join("Output.txt")
with open(output_path, 'w', newline='') as txtfile:
    txtfile.write(f"Total Months: {Total_Months}")
    txtfile.write(f"Total: ${Total_Profits}")
    txtfile.write(f"Average Change: ${Average_Change}")
    txtfile.write(f"Greatest Increase in Profits: {Increase_month} (${Max})")
    txtfile.write(f"Greatest Decrease in Profits: {Decrease_month} (${Min})")
    txtfile.close()


# In[ ]:





# In[ ]:




