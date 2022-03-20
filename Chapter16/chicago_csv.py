import csv
from fileinput import filename
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'Chapter16/csv/Chicago.csv' #assign the csv file to filename
with open(filename) as file: #we assign the object of filename to file
    reader = csv.reader(file) #we call csv.reader and pass it  the file object as an argument to create a reader oobject
    header_row = next(reader) #Store data from the first row with next function
    print(header_row)

    for index, column_header in enumerate(header_row): #Use this for loop/enumerate to find the indeces of date and temp min. (4,6)
        print(index, column_header)
    
    dates, highs, lows = [], [], [] # create a list
    for row in reader: # find the rows in reader
        if row[5] == '': # if the values in it are blank
            blank = (row[5]) #assign them to a variable that doesn't matter
        elif row[6] == '':
            blank = (row[6])
        else:
            low = int(row[6])
            lows.append(low)
            high = int(row[5]) #change the string to an int if its not blank and assign to variable high
            highs.append(high) #add the aformentioned variable to the list
        
    for row in reader:
        current_date = datetime.strptime(row[4], '%Y-%m-%d')
        dates.append(current_date)
    for i in dates:
        print(i) # I cannot figure out why this doesnt work sadly.
    print(highs) #print them to make sure they work (they do, just numbers now)
    print(lows)
    print(len(highs)) # find the number of values in the list (599, or roughly )




    #plotting the high temperatures
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(highs, c='orange')
    ax.plot(lows, c='blue')

    #Format plot
    ax.set_title("Daily high and low Temperatures, Chicago, 2022", fontsize = 24)
    ax.set_xlabel('', fontsize =16)
    ax.set_ylabel("Temperature (F)", fontsize = 16)
    ax.tick_params(axis = "both", which= "major", labelsize=16)

    plt.show()


