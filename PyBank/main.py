# Import necessary modules
import os
import csv

# Set variables
nettotal = 0
i = 0
months = []
amounts = []
changes = []
maxdate = ''
mindate = ''

# Set the path to read the relevant csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open as CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
    
    # Skip header
    csv_header = next(csvreader)
    
    # Append to lists accordingly
    for row in csvreader:
        months.append(row[0])
        amounts.append(int(row[1]))
        
        # All integer values in row 1 added to get net total
        nettotal += int(row[1])
        
        # Append the differences between subsequent rows to the changes list, as long as i > 0
        if i > 0:
            changes.append(int(amounts[i]) - int(amounts[i-1]))
        i += 1

    # Set remaining variables
    totalmonths = len(months)
    average = round(sum(changes)/len(changes), 2)
    maximum = max(changes)
    maxdate = str(months[(changes.index(max(changes)) + 1)])
    mindate = str(months[(changes.index(min(changes)) + 1)])
    minimum = min(changes)

    # Print results
    print('Financial Analysis')
    print('---------------------------------------------------')
    print(f'Total Months: {totalmonths}')
    print(f'Total: ${nettotal}')
    print(f'Average Change: ${average}')
    print(f'Greatest Increase in Profits: {maxdate} (${maximum})')
    print(f'Greatest Decrease in Profits: {mindate} (${minimum})')

    # Export to Results.txt
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

        