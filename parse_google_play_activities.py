import os

import pandas as pd

class GoogleMonthlyActivities:
    def __init__(self, name, charges, fees):
        self.name = name
        self.charges = charges
        self.fees = fees

    def __str__(self):
        return 'Name: ' + self.name + ', Charges: ' + str(self.charges) + ', Fees: ' + str(self.fees) + ', Sum: ' + str(self.charges + self.fees)

all_files = os.listdir('.')
sorted_csv_files = sorted([x for x in all_files if x.endswith('.csv')])
activities = []

for file in sorted_csv_files:
    if file.endswith('.csv'):
        df = pd.read_csv(file)
        charges = df.loc[df['Transaction Type'].isin(['Charge', 'Charge refund']), 'Amount (Merchant Currency)'].sum()
        fees = df.loc[df['Transaction Type'].isin(['Google fee', 'Google fee refund', 'Tax']), 'Amount (Merchant Currency)'].sum()
        activities.append(
            GoogleMonthlyActivities(file, charges, fees)
        )
    for activity in activities:
        print(activity)

total_income = round(sum([x.charges for x in activities]), 2)
total_expenses = round(sum([x.fees for x in activities]), 2)
print('\nTotal Income: $' + str(total_income))
print('Total expenses: $' + str(total_expenses))
print('Net income: ' + str(total_income + total_expenses))