import csv

csv_dict = {}


with open("CandidateSummary.csv") as f:
    reader = csv.reader(f)
    
    for row in reader:
        primary_key = row[0]
        if primary_key not in csv_dict:
            csv_dict[primary_key] = {"Candidate Name": row[1], 
            "Candidate Office": row[2], "Candidate Office State": row[3],
            "Candidate Office District": row[4], "Candidate Party Affiliation": row[5],
            "Candidate Incumbant Challenger Open Seat": row[6], "Candidate Street": row[7],
            "Candidate City": row[8], "Candidate State": row[9], "Candidate Zip Code": row[8],
            "Individual Contributions": row[9], "Party Committee Contributions": row[10],
            "Other Committee Contributions": row[11], "Candidate Contribution": row[12],
            "Total contributions": row[13], "Operating Expenditures": row[14],
            "Cash On Hand Beginning of Period": row[15], "Cash On Hand Close of Period": row[16],
            "Net Contribution": row[17], "Net Operation Expenditures": row[18], 
            "Coverage Start Date": row[19], "Coverage End Date": row[20]
            }
            
print(csv_dict['P60013794'])
    



