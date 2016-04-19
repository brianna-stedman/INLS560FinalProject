#!/usr/bin/python3

file = "CandidateSummary.csv"

with open(file) as f:
    campaign_line_list = f.readlines()
    
print(type(campaign_line_list))


column_headers = campaign_line_list[0].split(',')

print(column_headers)

option_number = 0
for column in column_headers:
    option_number += 1
    print(str(option_number) + '.' + column)
    
campaign_table = []

for row in campaign_line_list:
    campaign_table.append(row.split(","))

for list in campaign_table:
    print(list[3])
    







