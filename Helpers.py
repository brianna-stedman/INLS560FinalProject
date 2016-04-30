#!/usr/bin/python3

import csv                    ### importing the necessary module. 
import re
import collections


def search_candidate(reader):  ### this is the function that runs if the user selects the '1. search a candidate' option.

    print("Welcome to candidate choice mode!")
    candidate_choice = input("Please type in a name of a candidate: " )
    capital_candidate_choice = candidate_choice.upper()
    formatted_candidate_choice = capital_candidate_choice.replace(',', ' ').split() ### Got this idea from Aaron Knight at the second Python meeting I attended. Breaks up user input into discrete name elements by replacing any commas a user might but in with a space, and then splitting on that space. 

    candidate_matches_dict = {}  ### this is where I will put the candidate names that match the user's search.
    candidate_match_dict_key = 0   ### I want a numeric key so each result that displays is asssociated with a number. Therefore a user just has to input a single number to view a candidate's stats, instead of having to type a name over.
    
    for row in reader:   ### loop through each row in reader (each row corresponds to a candidate)
        for name in formatted_candidate_choice: ### for each name element that the user puts in...remember we split the name up in the code directly above.
            if re.findall(name, row['Candidate Name']) and name not in candidate_matches_dict:  ##if the name element matches the string value at the key ['Candidate Name'], then add that row to candidate_matches_dict if it's not there already.
                candidate_match_dict_key += 1
                candidate_matches_dict[str(candidate_match_dict_key)] = row
                
            else:
                continue
    
    intermediate_candidate_matches_dict = {int(k): v for k,v in candidate_matches_dict.items()}       ### Changing each key in my dictionary to a numeric value so I can sort it below. 
    ordered_candidate_matches_dict = collections.OrderedDict(sorted(intermediate_candidate_matches_dict.items()))
   # print(ordered_candidate_matches_dict)
  
    print("Did you mean: ")
    
    for key in ordered_candidate_matches_dict:  ### print out every candidate name that matched the user's query along with it's corresponding key. 
      print(str(key) + ": " + ordered_candidate_matches_dict[key]['Candidate Name'])
    specific_candidate_choice = str(input("To see information on a specific candidate type the number that corresponds to the candidate name: ")) ### to see stats for a candidate, they just need to type in the candidate's corresponding number.
    try:
        if specific_candidate_choice in candidate_matches_dict: ### displaying the selected candidate's stats.
         print('Candidate name: ' + candidate_matches_dict[specific_candidate_choice]['Candidate Name'])
         print('Type of office: ' + candidate_matches_dict[specific_candidate_choice]['Candidate Office'])
         print('Candidate Office State: ' + candidate_matches_dict[specific_candidate_choice]['Candidate Office State'])
         print('Candidate Party Affiliation: ' + candidate_matches_dict[specific_candidate_choice]['Candidate Party Affiliation'])
         print('Incumbent/Challenger/Open: ' + candidate_matches_dict[specific_candidate_choice]['Candidate Incumbant Challenger Open Seat'])
         print('Candidate Address: '+ candidate_matches_dict[specific_candidate_choice]['Candidate Street 1'] + ',' + candidate_matches_dict[specific_candidate_choice]['Candidate City'] + ',' + candidate_matches_dict[specific_candidate_choice]['Candidate State'])
         print('Individual Contributions: ' + candidate_matches_dict[specific_candidate_choice]['Individual Contributions'])
         print('Other Committee Contributions: ' + candidate_matches_dict[specific_candidate_choice]['Other Committee Contribution'])
         print('Total Contributions: ' + candidate_matches_dict[specific_candidate_choice]['Total Contributions'])
    except KeyError:
        print("")
         
     
def candidate_by_state(reader): ### this is the function that activates qhen the user selects the '2. General Candidate Data by State' option.

    print("This option visualizes the total contributions for each candidate by state.")
    
    accepted_state_list = {"AL", "AK", "AS", "AZ", "AR",         ### making a list of all the state abbreviations that appear in the csv files.
    "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI",
    "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV",
    "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OR", "PA",
    "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA",
    "WV", "WI", "WY"}
    
    while True:
        user_state_abbreviation = input("Type in a state abbreviation to see the total contributions of each candidate in that state: ").upper()  ### user inputs state-abbreviation. Capitalization doesn't matter due to .upper()
        state_candidate_dict = {}   ### where I will put all the candidates that belong to the user-selected state. 
        state_candidate_dict_key = 0
        if user_state_abbreviation in accepted_state_list:
            for row in reader:
                if user_state_abbreviation == row['Candidate State']:   ### If the candidate is involved in the state that the user selected, add that candidate's row to the dictionary and give it a numerical key.
                    state_candidate_dict_key +=1
                    state_candidate_dict[str(state_candidate_dict_key)] = row
                    
                
            break
        else:
            print("Invalid state abbreviation. Here's a list of valid state abbreviations for reference: ")
            print(accepted_state_list)
            continue

    ordered_state_candidate_dict = collections.OrderedDict(sorted(state_candidate_dict.items())) ### ordering the keys in the new dictionary for display
    for key in ordered_state_candidate_dict:
    
        split_total_contributions = ordered_state_candidate_dict[key]['Total Contributions'].replace('$','') ### these three lines of code turn dollars to numbers. Ex: $100,000 to 100000
        split_total_contributions = split_total_contributions.replace(',', '')
        split_total_contributions = split_total_contributions.split()
        
        if len(split_total_contributions) < 1:   ### some candidates have empty values for the total contributies field. So I just print one asterisk for them.
            print(key, ":", ordered_state_candidate_dict[key]['Candidate Name'], '*')
        else:
            print(key, ":", ordered_state_candidate_dict[key]['Candidate Name'], "*" * int((float(split_total_contributions[0])/1000))) ### data visualization. Askterisk count roughly corresponds to the amount of total contributions the candiate received.

