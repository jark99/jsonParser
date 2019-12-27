import json
import csv, sys
from pathlib import Path


# # Find the absolute path of EXE, append Json and CSV to create FilePaths
# exepath = Path(sys.executable).resolve()
# csv_path = exepath.parent / "JSONparser.csv"
# files = exepath.parent.glob("*.json")
#
# #Loop over any JSON file
# for i in files:
# #Open the JSON file location, assign variable JS

with open(r"C:\Users\gd92\Documents\Mod-AWS Ranger_20190816.json") as file:
        js = json.load(file)
        #Open the CSV file location, assign variable wr
        with open("JSONparser.csv", 'w', newline='') as fd:
            # write to CSV with headings for Data to be Parsed
            wr = csv.writer(fd)
            wr.writerow(('Database name', 'Group', 'isAllowed', 'Type', 'Description', 'Table', 'Columns'))
            # Start Loop over JSON Objects and assign to values, iterate over multiple objects
            for policy in js['policies']:
                desc = policy['description']
                if 'database' in policy['resources']:
                    db_values = policy['resources']['database']['values']
                if policy['isEnabled'] == True:
                    if 'table' in policy['resources']:
                     tables = policy['resources']['table']['values']
                     if 'column' in policy['resources']:
                         columns = policy['resources']['column']['values']
                     for item in policy['policyItems']:
                         users = item['users']
                         access_val = item['accesses'][0]['isAllowed']
                         access_type = item['accesses'][0]['type']
                         user_Group = item['groups']
                         for grp in user_Group:
                             for db in db_values:
                                 for tbl in tables:
                                     for cols in columns:
                                         #for grp in user_Group:
                                         if db != '*':
                                             wr.writerow((db, grp, access_val, access_type, desc, tbl, cols))