
import csv
import os

data = os.path.join("election_data_1.csv")
file_output = "election_analysis_1.txt"

votes_total = 0

candidate_votes = {}    
candidate_options = []

winning_candidate = ""
winning_count = 0

with open(data) as election_data:
    reader = csv.DictReader(election_data)

    for row in reader:

        print(". ", end=""),

        votes_total = votes_total + 1

        candidate_name = row["Candidate"]

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

with open(file_output, "w") as txt_file:

    results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {votes_total}\n"
        f"-------------------------\n")
    print(results, end="")

    txt_file.write(results)

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / (float(votes_total) + .0000000000001)* 100

        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        txt_file.write(voter_output)

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

