#!/usr/bin/python3

import csv
import re
import collections


def search_candidate(reader):
    # for row in reader:
    #  print(row)
    #  break
    print("Welcome to candidate choice mode!")
    candidate_choice = input("Please type in a name of a candidate: " )
    capital_candidate_choice = candidate_choice.upper()
    formatted_candidate_choice = capital_candidate_choice.replace(',', ' ').split() 
    #print(formatted_candidate_choice)
    candidate_matches_dict = {}
    candidate_match_dict_key = 0
    
    for row in reader:
        #print("hello")
        for name in formatted_candidate_choice: 
            if re.findall(name, row['Candidate Name']) and name not in candidate_matches_dict:
                candidate_match_dict_key += 1
                candidate_matches_dict[str(candidate_match_dict_key)] = row
                
            else:
                continue
    
    intermediate_candidate_matches_dict = {int(k): v for k,v in candidate_matches_dict.items()}
    ordered_candidate_matches_dict = collections.OrderedDict(sorted(intermediate_candidate_matches_dict.items()))
   # print(ordered_candidate_matches_dict)
  
    print("Did you mean: ") 
    #print(candidate_matches_dict)
    for key in ordered_candidate_matches_dict:
      print(str(key) + ": " + ordered_candidate_matches_dict[key]['Candidate Name'])
    specific_candidate_choice = str(input("To see information on a specific candidate type the number that corresponds to the candidate name: "))
    if specific_candidate_choice in candidate_matches_dict:
     print('Candidate name: ' + candidate_matches_dict[specific_candidate_choice]['Candidate Name'])
     print('Type of office: ' + candidate_matches_dict[specific_candidate_choice]['Candidate Office'])
     print('Candidate Office State: ' + candidate_matches_dict[specific_candidate_choice]['Candidate Office State'])
     print('Candidate Party Affiliation: ' + candidate_matches_dict[specific_candidate_choice]['Candidate Party Affiliation'])
     print('Incumbent/Challenger/Open: ' + candidate_matches_dict[specific_candidate_choice]['Candidate Incumbant Challenger Open Seat'])
     print('Candidate Address: '+ candidate_matches_dict[specific_candidate_choice]['Candidate Street 1'] + ',' + candidate_matches_dict[specific_candidate_choice]['Candidate City'] + ',' + candidate_matches_dict[specific_candidate_choice]['Candidate State'])
     print('Individual Contributions: ' + candidate_matches_dict[specific_candidate_choice]['Individual Contributions'])
     print('Other Committee Contributions: ' + candidate_matches_dict[specific_candidate_choice]['Other Committee Contribution'])
     print('Total Contributions: ' + candidate_matches_dict[specific_candidate_choice]['Total Contributions'])
     
     
def candidate_by_state(reader):
    print("This option visualizes the total contributions for each candidate by state.")
    
    accepted_state_list = {"AL", "AK", "AS", "AZ", "AR",
    "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI",
    "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV",
    "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OR", "PA",
    "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA",
    "WV", "WI", "WY"}
    
    while True:
        user_state_abbreviation = input("Type in a state abbreviation to see the total contributions of each candidate in that state: ").upper()
        state_candidate_dict = {}
        state_candidate_dict_key = 0
        if user_state_abbreviation in accepted_state_list:
            for row in reader:
                if user_state_abbreviation == row['Candidate State']:
                    state_candidate_dict_key +=1
                    state_candidate_dict[str(state_candidate_dict_key)] = row
                    
                
            break
        else:
            print("Invalid state abbreviation. Here's a list of valid state abbreviations for reference: ")
            print(accepted_state_list)
            continue

    ordered_state_candidate_dict = collections.OrderedDict(sorted(state_candidate_dict.items()))
    for key in ordered_state_candidate_dict:
    
        split_total_contributions = ordered_state_candidate_dict[key]['Total Contributions'].replace('$','')
        split_total_contributions = split_total_contributions.replace(',', '')
        #split_total_contributions = split_total_contributions.replace('.', '')
        split_total_contributions = split_total_contributions.split()
        #formatted_total_contributions = split_total_contributions.join(' ')
        #formatted_total_contributes = split_total_contributions.join(' ')
    
        #formatted_total_contributions = split_total_contributions[0]
        if len(split_total_contributions) < 1:
            print(key, ":", ordered_state_candidate_dict[key]['Candidate Name'], '*')
        else:
            print(key, ":", ordered_state_candidate_dict[key]['Candidate Name'], "*" * int((float(split_total_contributions[0])/100)))

