import csv
import os


# Assign a variable for the file to load and the path.
file_to_load = '/Users/sandeeppowar/Desktop/Analysis_Projects/datascience_bootcamp/Module3/Resources/election_results.csv'

# Create a filename variable to a direct or indirect path to the file.
file_to_save = '/Users/sandeeppowar/Desktop/Analysis_Projects/datascience_bootcamp/Module3/Resources/analysis/election_analysis.txt'

total_vote = 0
candidate_options = []
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0  
# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.

    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    
     # Print each row in the CSV file.
    for row in file_reader:
        total_vote = total_vote + 1 

# Print the candidate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:
          # Add the candidate name to the candidate list.
          candidate_options.append(candidate_name)

          candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # Save the results to our text file.
with open(file_to_save, "w") as txt_file:

     election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_vote:,}\n"
        f"-------------------------\n")
     print(election_results, end="")
     # Save the final vote count to the text file.
     txt_file.write(election_results)

     # Print the candidate list.
     #print(candidate_votes)

     # Determine the percentage of votes for each candidate by looping through the counts.
     # 1. Iterate through the candidate list.
     for candidate_name in candidate_votes:
          # 2. Retrieve vote count of a candidate.
          votes = candidate_votes[candidate_name]
          # 3. Calculate the percentage of votes.
          vote_percentage = float(votes) / float(total_vote) * 100
          # 4. Print the candidate name and percentage of votes.
          candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
          # Print each candidate, their voter count, and percentage to the terminal.
          print(candidate_results)
          #  Save the candidate results to our text file.
          txt_file.write(candidate_results)
          if (votes > winning_count) and (vote_percentage > winning_percentage):
               # If true then set winning_count = votes and winning_percent =
               # vote_percentage.
                    winning_count = votes
                    winning_percentage = vote_percentage
               # And, set the winning_candidate equal to the candidate's name.
                    winning_candidate = candidate_name
          winning_candidate_summary = (
                    f"-------------------------\n"
                    f"Winner: {winning_candidate}\n"
                    f"Winning Vote Count: {winning_count:,}\n"
                    f"Winning Percentage: {winning_percentage:.1f}%\n"
                    f"-------------------------\n")
          print(winning_candidate_summary)
          # Save the winning candidate's name to the text file.
          txt_file.write(winning_candidate_summary)     

