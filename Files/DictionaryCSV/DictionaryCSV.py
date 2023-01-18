import csv
with open('new1.csv','w') as outf:
    fields = ['Name', 'Department', 'Birthday Month']
    content = csv.DictWriter(outf, fieldnames=fields)
    content.writeheader()
    content.writerow({'Name': 'John', 'Department': 'Accounts', 'Birthday Month': 'November'})
    content.writerow({'Name': 'Amy', 'Department': 'IT', 'Birthday Month': 'March'})

with open('new1.csv','r') as f:
    data=csv.reader(f)
    for r in data:
        print(','.join(r))
