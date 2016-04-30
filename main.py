#!/usr/bin/python3

import csv                          ### importing necessary modules
import re
import collections
import Helpers



     
while True:
    print("")
    print("Campaign csv files:  1. 2008. 2. 2010 3. 2012 4. 2014 5.2016")
    user_csv_choice = int(input("To work with a campaign csv file from a certain year, input one of the option numbers above (1-5): "))      ### letting the user pick a csv file based off of what year they want to look at.

    try: ### setting user_csv_choice to a particular .csv file.
        if user_csv_choice == 1:
            csv_file = "CandidateSummary2008.csv"
            print("You are now working with data from the 2008 campaign.")
            #break
        elif user_csv_choice == 2:
            csv_file = "CandidateSummary2010.csv"
            print("You are now working with data from the 2010 campaign.")
            #break
        elif user_csv_choice == 3:
            csv_file = "CandidateSummary2012.csv"
            print("You are now working with data from the 2012 campaign.")
            #break
        elif user_csv_choice == 4:
            csv_file = "CandidateSummary2014.csv"
            print("You are now working with data from the 2014 campaign.")
            #break
        elif user_csv_choice == 5:
            csv_file = "CandidateSummary2016.csv"
            print("You are now working with data from the 2016 campaign.")
            #break
    except:
        print("Invalid csv choice. Please choose a number 1-5.")
        continue
    
    while True:
        with open(csv_file) as f:
            reader = csv.DictReader(f)
        
        
            user_first_option = int(input("Please pick from this first tier of options: 1. Find a Candidate 2. General Candidate Data by State 3. Help 4. Leave : "))
            
            try:
                if user_first_option == 1:
                    Helpers.search_candidate(reader)
                    continue
                elif user_first_option == 2:
                    Helpers.candidate_by_state(reader)
                    continue
                elif user_first_option == 3: 
                    print("")
                    print("BEGINNING OF HELP SCREEN(scroll down to see more)")
                    print("")
                    print("This is the help screen! Hope this helps.")
                    print("This is script that reads csv files from www.fec.gov. There are currently 5 csv files that work with the script for the 2008, 2010, 2012, 2014, and 2016 campaigns.")
                    print("For each csv file, this program is able to do two things 1. Search for a candidate or 2. Visualize candidate data by state")
                    print("")
                    print("If you choose to search for a candidate, simply begin by querying a candidate name.")
                    print("From there you will be greeted with a list of candidate names that matched your search, like so:")
                    print("1: Candidate A")
                    print("2: Candidate B")
                    print("3: Candidate C")
                    print("To pick Candidate A you would input 1. For Candidate B you would input 2, and so on. Once you've selected a candidate, the program will pull up some stats related to their campaign.")
                    print("Here's some example output:")
                    print("")
                    print("Candidate name: TRUMP, DONALD J")
                    print("Type of office: P")
                    print("Candidate Office State: US")
                    print("Incumbent/Challenger/Open: OPEN")
                    print("Candidate Address: 725 FIFTH AVENUE,NEW YORK,NY")
                    print("Individual Contributions: $9,527,020.19")
                    print("Other Committee Contributions: ")
                    print("Total Contributions: $9,809,453.45")
                    print("")
                    print("This program also has the functionality to provide a data visualization of each individual candidate depending on a user-selected state.")
                    print("Simply type in the two-letter abbreviation of the state to see a data visualization of the total contributions given to each candidate in that state.")
                    print("And if one candidate catches your eye, feel free to search his/her name using the search a candidate option outlined above!")
                    print("Best of luck. And if this Elliot, thanks for all the work/patience you did for this class. Definitely opened a lot of doors for me. Take care.")
                    print("")
                    print("END OF HELP")
                    print("")
                    continue 
                elif user_first_option == 4:
                    break
            except:
                ("Invalid Input. Please press 1, 2, 3, or 4.")
                break
            continue 
    
    


    
   