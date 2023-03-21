#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os

import csv

csvpath = os.path.join("/Users/devangpatel/Desktop/PythonChallenge/PyPoll/Resources/election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    Candidate = []
    candidateList = []
    totalVoters = 0
    votes = {}
  #  CandidateDict = {}

    for row in csvreader:
        Candidate = row[2]
        if Candidate not in candidateList:
            candidateList.append(Candidate)
            votes[Candidate] = 0
        votes[Candidate] += 1
        totalVoters += 1


# We will now print out the results.  In the midst of printing this out, we'll calculate the % of votes cast
# for each candidate, and we will also declare a winner based on the highest number of votes.

    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str('{:,.0f}'.format(totalVoters)))
    print("-------------------------")
    for i in votes:
        PctVotes = '{:,.3f}'.format((votes[i]/totalVoters)*100)
        print(i + ": " + str(PctVotes) +
              "% (" + str('{:,.0f}'.format(votes[i])) + ")")
    print("-------------------------")
    keyMax = max(votes, key=votes.get)
    print("Winner:  " + keyMax)
    print("-------------------------")


# In[ ]:





# In[ ]:




