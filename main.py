# Created by: Jess Gallo
# Date Created: 5/9/2022
# Last Modified: 5/11/2022
# Description: The purpose of this programming problem is to determine the status of a customer account
# history at the time a new purchase is made. The input is a sequence of customer account events, in
# chronological order. Each event has three fields, all of which are of string type

# This program assumes entries are inputted through terminal

import pandas as pd

print('Commands:\n'
      'Press "1" to start')

# Variables
DATE = []
CUSTOMER_ACCOUNT_ID = []
EVENT_TYPE = []
start = '1'
customer_history = 'CH'
user_input = input()
element_dict = {'DATE': [], 'CUSTOMER_ACCOUNT_ID': [], 'EVENT_TYPE': []}
# element_df = pd.DataFrame(element_dict)
customer_history_dict = {'DATE': [], 'CUSTOMER_ACCOUNT_ID': [], 'HISTORY_REPORT': []}
count = 0

while True:
    if user_input == start:
        print('Instructions:\n'
              'Enter Input in format "DATE,CUSTOMER_ACCOUNT_ID,EVENT_TYPE" \n'
              'Enter "CH" when input is finished and you want a report\n')
        user_input2 = input()

        # assumed all user input is something like this: 2015-05-05,person@mail.com,PURCHASE
        # this updates as user input is appended
        if ',' in user_input2:
            element = str(user_input2).split(',')

            element_dict['DATE'].append(element[0])
            element_dict['CUSTOMER_ACCOUNT_ID'].append(element[1])
            element_dict['EVENT_TYPE'].append(element[2])

            '''
            # checks the dictionary of whatever the user just inputs
            if element_dict['CUSTOMER_ACCOUNT_ID'] == element[1]:
                if element_dict['EVENT_TYPE'] is False:
                    history_report = 'NO_HISTORY'

                    customer_history_dict['DATE'].append(element[0])
                    customer_history_dict['CUSTOMER_ACCOUNT_ID'].append(element[1])
                    customer_history_dict['HISTORY_REPORT'].append(history_report)

                    print(customer_history_dict)

                elif element[2] == 'PURCHASE':
                    history_report2 = 'UNCONFIRMED_HISTORY: '

                    for val in element_dict.values():
                        if val == 'PURCHASE':
                            count += 1

                    customer_history_dict['DATE'].append(element[0])
                    customer_history_dict['CUSTOMER_ACCOUNT_ID'].append(element[1])
                    customer_history_dict['HISTORY_REPORT'].append(history_report2)

                    print('UNCONFIRMED_HISTORY: ', count)

            elif element_dict['EVENT_TYPE'] == 'FRAUD_REPORT':
                history_report = 'FRAUD_HISTORY: '
            for val in element_dict[[0]].items():
                print("{}".format(val))
            '''
        elif user_input2 == 'CH':
            # where we will print but calculations go through during input
            element_df = pd.DataFrame(element_dict)
            print(element_df)

            # change DATE column to datetime
            element_df['DATE'] = pd.to_datetime(element_df['DATE'])

            print(element_df.dtypes)

            output2 = element_df.groupby(['CUSTOMER_ACCOUNT_ID', 'EVENT_TYPE'])['CUSTOMER_ACCOUNT_ID'].count()
            print(output2)


