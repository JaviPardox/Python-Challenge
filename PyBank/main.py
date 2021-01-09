#!/usr/bin/env python
# coding: utf-8

# In[31]:



# os allows to create file paths accross operating systems
import os 

# csv allows to read csv files 
import csv 

#compute all parameters 
def computeParam(balanceChange):
    
    maxInc = 0
    maxIncIndex = 0
    maxDec = 0
    maxDecIndex = 0
    diff = 0
    total = 0
    diffList = []
    avrgDiff = 0
    
    for i in range(len(balanceChange)):
        
        if(i+1 < len(balanceChange)):
            
            diff = balanceChange[i+1] - balanceChange[i]
            diffList.append(diff)
            
            if(diff > maxInc):
                
                maxInc = diff
                maxIncIndex = i+1
            
            if(diff < maxDec):
                
                maxDec = diff
                maxDecIndex = i+1
        
        total += balanceChange[i]
        avrgDiff = round(sum(diffList)/len(diffList),2)
            
    return maxInc,maxDec,maxIncIndex,maxDecIndex,total,avrgDiff

#concatenates file path
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

#open csv file
with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    parameters = []
    dates = []
    balanceChanges = []
    
    next(csvreader) #skip first line
    
    for row in csvreader:
            
        dates.append(row[0])
        balanceChanges.append(int(row[1]))


parameters = computeParam(balanceChanges)

#declaring path for output file 
output_path = os.path.join('.', 'Analysis', 'analysis.csv')

with open(output_path, 'w', newline='') as csvfile:
    
    csvwriter = csv.writer(csvfile, delimiter=',')
    
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['------------------'])
    csvwriter.writerow(['Total months: ', len(dates)])
    csvwriter.writerow(['Total: $', parameters[4]])
    csvwriter.writerow(['Average Change: $', parameters[5]])
    csvwriter.writerow(['Greatest increase in Profits:', dates[parameters[2]], parameters[0]])
    csvwriter.writerow(['Greatest decrease in Profits: ', dates[parameters[3]], parameters[1]])
            
     
print("Financial Analysis")
print("------------------")
print("Total months: " + str(len(dates)))
print("Total: $" + str(parameters[4]))
print("Average Change: $" + str(parameters[5]))
print("Greatest increase in Profits: " + str(dates[parameters[2]]) + " ($" + str(parameters[0]) + ")")
print("Greatest decrease in Profits: " + str(dates[parameters[3]]) + " ($" + str(parameters[1]) + ")")


# In[ ]:




