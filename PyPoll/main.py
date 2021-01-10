#!/usr/bin/env python
# coding: utf-8

# In[22]:


# os allows to create file paths accross operating systems
import os 

# csv allows to read csv files 
import csv 


#concatenates file path
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

#open csv file from csvpath
with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip first line
    next(csvreader) 
    
    #variables to keep track of total votes and candidate's votes
    totalVotes = 0         
    votesKhan = 0
    votesCorrey = 0
    votesLi = 0
    votesOtooley = 0
    
    #winnerCount keeps track of who's winning up to that row
    winnerCount = 0        
    
    for row in csvreader:
            
        totalVotes += 1
        
        if(row[2] == "Khan"):
            votesKhan += 1
            if(votesKhan > winnerCount):
                winnerCount = votesKhan
                winner = "Khan"
            
        if(row[2] == "Correy"):
            votesCorrey += 1
            if(votesCorrey > winnerCount):
                winnerCount = votesCorrey
                winner = "Correy"
            
        if(row[2] == "Li"):
            votesLi += 1
            if(votesLi > winnerCount):
                winnerCount = votesLi
                winner = "Li"
            
        if(row[2] == "O'Tooley"):
            votesOtooley += 1
            if(votesOtooley > winnerCount):
                winnerCount = votesOtooley
                winner = "O'Tooley"
                
            
#declaring path for output file 
output_path = os.path.join('.', 'Analysis', 'pollAnalysis.csv')

#write to file 
with open(output_path, 'w', newline='') as csvfile:
    
    csvwriter = csv.writer(csvfile, delimiter=',')
    
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['------------------'])
    csvwriter.writerow(['Total Votes: ',totalVotes])
    csvwriter.writerow(['------------------'])
    csvwriter.writerow(['Khan',round((votesKhan/totalVotes)*100,3),votesKhan])
    csvwriter.writerow(['Correy',round((votesCorrey/totalVotes)*100,3),votesCorrey])
    csvwriter.writerow(['Li',round((votesLi/totalVotes)*100,3),votesLi])
    csvwriter.writerow(["O'Tooley",round((votesOtooley/totalVotes)*100,3),votesOtooley])
    csvwriter.writerow(['------------------'])
    csvwriter.writerow(['Winner', winner])
    csvwriter.writerow(['------------------'])
        
        
print("Election Results")
print("-----------------------")
print("Total Votes: " + str(totalVotes))
print("-----------------------")
print("Khan: " + str(round((votesKhan/totalVotes)*100,3)) + "% (" + str(votesKhan) + ")")
print("Correy: " + str(round((votesCorrey/totalVotes)*100,3)) + "% (" + str(votesCorrey) + ")")
print("Li: " + str(round((votesLi/totalVotes)*100,3)) + "% (" + str(votesLi) + ")")
print("O'Tooley: " + str(round((votesOtooley/totalVotes)*100,3)) + "% (" + str(votesOtooley) + ")")
print("-----------------------")
print("Winner: " + winner)
print("-----------------------")




    


# In[ ]:




