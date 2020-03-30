import os
import csv

election_data = os.path.join("Resources","election_data.csv")

with open (election_data) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvfile)

    #validate file was loaded correctly
    # print(f'Header: {csv_header}')

#Define variables
    voter_id = []
    county = []
    candidate = []

    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

# #validate - note: large data set. cannot print all the rows
# print(voter_id)
# print(county)
# print(candidate)


# Total number of votes cast
    total_votes = len(voter_id)
    #print(total_votes)

# Complete list of candidates who received votes

runners_list = []
correy_votes = 0
otooley_votes = 0
khan_votes = 0
li_votes = 0

#ran multiple if statements based on the same row in 1 loop for efficiency
def set_of_runners(candidate):
    for i in candidate:
        if i not in runners_list:
            runners_list.append(i)
    #validate if the list works
    # print(runners_list)

        #need to reference variables for 2nd if statement as 'global' in order to make them accessible throughout the whole doc
        global correy_votes
        global otooley_votes
        global khan_votes
        global li_votes

        if i == "Correy":
                correy_votes = correy_votes + 1
        elif i == "O'Tooley":
                otooley_votes = otooley_votes + 1
        elif i == "Khan":
                khan_votes = khan_votes + 1
        elif i == "Li":
                li_votes = li_votes + 1

    #votes per candidate
    # print("Correy: " + str(correy_votes))
    # print("O'Tooley: " + str(otooley_votes))
    # print("Khan: " + str(khan_votes))
    # print("Li: " + str(li_votes))
    
    #list of candidates
    # print(runners_list)

#need to call the defined function in order for it to run
set_of_runners(candidate)

#create a list of votes to find max and call index for location
#list is organized in the same order as list of candidates so that the location of max votes will match location of winner candidate
votes_list = [khan_votes, correy_votes, li_votes, otooley_votes]
#validate
#print(votes_list)

winner = max(votes_list)
#validate
# print(winner)

max_index = votes_list.index(winner)
#validate
# print(max_index)

winner_name = runners_list[max_index]
#validate
# print(winner_name)


# Percentage of votes each candidate won
cper = correy_votes/total_votes
oper = otooley_votes/total_votes
kper = khan_votes/total_votes
lper = li_votes/total_votes

#validate
# print(cper)
# print(oper)
# print(kper)
# print(lper)


# Print the following:
# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan

print("Election Results")
print("---------------------------")

print("Total Votes: " + str(total_votes))

print("---------------------------")

print("Khan: "+ '{:.3%}'.format(kper) + " " + "(" + str(khan_votes) + ")")

print("Correy: " + '{:.3%}'.format(cper) + " " + "(" + str(correy_votes) + ")")

print("Li: " + '{:.3%}'.format(lper) + " " + "(" + str(li_votes) + ")")

print("O'Tooley: " + '{:.3%}'.format(oper) + " " + "(" + str(otooley_votes) + ")")

print("---------------------------")

print("Winner: " + str(winner_name))

# export file
output = os.path.join("ElectionResults.csv")
with open (output, "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=" ")
    csvwriter.writerow("Election Results")
    csvwriter.writerow("---------------------------")
    csvwriter.writerow("Total Votes: " + str(total_votes))
    csvwriter.writerow("---------------------------")
    csvwriter.writerow("Khan: " + '{:.3%}'.format(kper) + " " + "(" + str(khan_votes) + ")")
    csvwriter.writerow("Correy: " + '{:.3%}'.format(cper) + " " + "(" + str(correy_votes) + ")")
    csvwriter.writerow("Li: " + '{:.3%}'.format(lper) + " " + "(" + str(li_votes) + ")")
    csvwriter.writerow("O'Tooley: " + '{:.3%}'.format(oper) + " " + "(" + str(otooley_votes) + ")")
    csvwriter.writerow("---------------------------")
    csvwriter.writerow("Winner: " + str(winner_name))