# Import necessary modules
import os
import csv

nettotal = 0

# Set the path to read the relevant csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 

    csv_header = next(csvreader)

    months = []
    amounts = []
    changes = []
    maxdate = ''
    mindate = ''
    i = 0

    for row in csvreader:
        months.append(row[0])
        amounts.append(int(row[1]))

        nettotal += int(row[1])
        if i > 0:
            changes.append(int(amounts[i]) - int(amounts[i-1]))
        i += 1

    
    totalmonths = len(months)
    average = round(sum(changes)/len(changes), 2)
    maximum = max(changes)
    maxdate = str(months[changes.index(max(changes))])
    mindate = str(months[changes.index(min(changes))])
    minimum = min(changes)

    print('Financial Analysis')
    print('---------------------------------------------------')
    print(f'Total Months: {totalmonths}')
    print(f'Total: ${nettotal}')
    print(f'Average Change: ${average}')
    print(f'Greatest Increase in Profits: {maxdate} (${maximum})')
    print(f'Greatest Decrease in Profits: {mindate} (${minimum})')

    output_path = os.path.join('Analysis', 'Results.txt')
    with open(output_path, 'w') as outfile:
        outfile.write(
            f'Financial Analysis\n'
            f'---------------------------------------------------\n'
            f'Total Months: {totalmonths}\n'
            f'Total: ${nettotal}\n'
            f'Average Change: ${average}\n'
            f'Greatest Increase in Profits: {maxdate} (${maximum})\n'
            f'Greatest Decrease in Profits: {mindate} (${minimum})')

        