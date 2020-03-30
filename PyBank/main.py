import os
import csv
budget_data = os.path.join("Resources","budget_data.csv")

with open (budget_data) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvfile)
    #test if file loaded correctly
    #print(f'Header: {csv_header}')

    #define variables
    dates = []
    pl = []

    for row in csvreader:
        dates.append(row[0])
        pl.append(int(row[1]))
    
    #validate
    #print(dates)
    #print(pl)

#total number of months
#assuming none of the months are repeated
    month_total = len(dates)
    #validate
    # print(month_total)
    
#net total Profit/Loss over the entire period
net_total = sum(pl)
#validate
# print(net_total)

#average changes in pl over the period
avg = net_total/month_total
#validate
# print(avg)

#max pl - find max, index max, apply index to dates column to pull date of max
max_pl = max(pl)
max_index = pl.index(max_pl)
max_date = dates[max_index]
#validate
# print(max_index)
# print(max_date)

#max loss decrease over the period - date & amount
min_pl = min(pl)
min_index = pl.index(min_pl)
min_date = dates[min_index]
#validate
# print(min_date)


# Print results in the following format

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)


print("Financial Analysis")
print("---------------------------")

print("Total Months: " + str(month_total))

print("Total: " + "$" + str(net_total))

print("Average Change: " + "$" + str(int(avg)))

#Fix max_pl number format
print("Greatest Increase in Profits: " + str(max_date) + " " + "(" + "$" + str(max_pl) + ")")

#fix min_pl number format
print("Greatest Decrease in Profits: " + str(min_date) + " " + "(" + "$" + str(min_pl) + ")")

#export file
output = os.path.join("complete_budget.csv")
with open (output, "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=" ")
    csvwriter.writerow("Financial Analysis")
    csvwriter.writerow("---------------------------")
    csvwriter.writerow("Total Months: " + str(month_total))
    csvwriter.writerow("Total: " + "$" + str(net_total))
    csvwriter.writerow("Average Change: " + "$" + str(int(avg)))
    csvwriter.writerow("Greatest Increase in Profits: " + str(max_date) + " " + "(" + "$" + str(max_pl) + ")")
    csvwriter.writerow("Greatest Decrease in Profits: " + str(min_date) + " " + "(" + "$" + str(min_pl) + ")")