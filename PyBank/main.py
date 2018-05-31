
import csv
import os

data = os.path.join("budget_data_1.csv")
file_output = "budget_analysis_1.txt"

total_revenue = 0
total_months = 0
prev_revenue = 0
revenue_change_list = []
month_of_change = []
greatest_decrease = ["", 10000000]
greatest_increase = ["", 0]

with open(data) as revenue_data:
    reader = csv.DictReader(revenue_data)

    for row in reader:

        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Revenue"])

        revenue_change = int(row["Revenue"]) - prev_revenue
        prev_revenue = int(row["Revenue"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]

        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change

        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change

revenue_avg = sum(revenue_change_list) / len(revenue_change_list)


analysis = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(analysis)

with open(file_output, "w") as txt_file:
    txt_file.write(analysis)