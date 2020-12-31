# Import necessary modules
import os
import csv

# Set variables
candidate = []
candidatevotes = []
khanvotes = 0
correyvotes = 0
livotes = 0
otooleyvotes = 0

# Set the path to read the relevant CSV file
csvpath = os.path.join('Resources', 'election_data.csv')

# Open as CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip header
    csv_header = next(csvreader)

    # Append to lists accordingly
    for row in csvreader:
        candidate.append(row[2])

        if row[2] == 'Khan':
            khanvotes += 1
        if row[2] == 'Correy':
            correyvotes += 1
        if row[2] == 'Li':
            livotes += 1
        if row[2] == "O'Tooley":
            otooleyvotes += 1

    candidatevotes.append(khanvotes)
    candidatevotes.append(correyvotes)
    candidatevotes.append(livotes)
    candidatevotes.append(otooleyvotes)

    winner = str(candidate[candidatevotes.index(max(candidatevotes))])
    totalvotes = len(candidate)
    khanpercent = ('${:.3f}'.format(round(((khanvotes/totalvotes)*100), 3)))
    correypercent = ('${:.3f}'.format(round(((correyvotes/totalvotes)*100), 3)))
    lipercent = ('${:.3f}'.format(round(((livotes/totalvotes)*100), 3)))
    otooleypercent = ('${:.3f}'.format(round(((otooleyvotes/totalvotes)*100), 3)))

    print(f'Election Results')
    print(f'---------------------------')
    print(f'Total Votes: {totalvotes}')
    print(f'---------------------------')
    print(f'Khan: {khanpercent}% ({khanvotes})')
    print(f'Correy: {correypercent}% ({correyvotes})')
    print(f'Li: {lipercent}% ({livotes})')
    print(f"O'Tooley: {otooleypercent}% ({otooleyvotes})")
    print(f'---------------------------')
    print(f'Winner: {winner}')
    print(f'---------------------------')

    # Export to Results.txt
    output_path = os.path.join('Analysis', 'Results.txt')
    with open(output_path, 'w') as outfile:
        outfile.write(
            f'Election Results\n'
            f'---------------------------\n'
            f'Total Votes: {totalvotes}\n'
            f'---------------------------\n'
            f'Khan: {khanpercent}% ({khanvotes})\n'
            f'Correy: {correypercent}% ({correyvotes})\n'
            f'Li: {lipercent}% ({livotes})\n'
            f"O'Tooley: {otooleypercent}% ({correyvotes})\n"
            f'---------------------------\n'
            f'Winner: {winner}\n'
            f'---------------------------\n')
