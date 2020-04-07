
# import re
#
# formulas = ['ethanol;C2H6O', 'glucose;C6H12O6', 'caffeine;C8H10N4O2',
#             'adenosine triphosphase;C10H16N5O13P3', 'sodium chlorate;NaClO3']
#
# molecule = 'H2ClO3H5'
# my_dict = {}
#
# with_indices = re.findall('[A-Z][a-z]*\d+', molecule)
# without_indices = re.findall('[A-Z][a-z]*(?![0-9])', molecule)
# print(with_indices)
# for part in with_indices:
#     elem = re.findall('[A-Z][a-z]*', part)[0]
#     if not elem in my_dict:
#         my_dict[elem] = int(re.findall('[1-9]+', part)[0])
#     else:
#         my_dict[elem] += int(re.findall('[1-9]+', part)[0])
# for part in without_indices:
#     if part[0] in my_dict:
#         elem = re.findall('[A-Z][a-z]*', part)[0]
#         my_dict[elem] += 1
#     else:
#         elem = re.findall('[A-Z][a-z]*', part)[0]
#         my_dict[elem] = 1
# print(molecule)
# print(my_dict)

# ======================================================================================

import pandas as pd
import re

file = pd.read_csv(r'C:\Users\1\PycharmProjects\Test\UFAZ/Formula.csv', header=None)

counter = 0
for line in file.iloc[:][0]:
    molec_name = re.findall('.+?(?=;)', line)[0]
    formula = re.findall('\;(.*)', line)[0]
    my_dict = {}
    # print(molec_name)
    with_indices = re.findall('[A-Z][a-z]*\d+', formula)
    without_indices = re.findall('[A-Z][a-z]*(?![0-9])', formula)

    for part in with_indices:
        elem = re.findall('[A-Z][a-z]*', part)[0]
        if not elem in my_dict:
            my_dict[elem] = int(re.findall('[1-9]+', part)[0])
        else:
            my_dict[elem] += int(re.findall('[1-9]+', part)[0])
    for part in without_indices:
        elem = re.findall('[A-Z][a-z]*', part)[0]
        if elem in my_dict:
            my_dict[elem] += 1
        else:
            my_dict[elem] = 1
    if 'H' in my_dict and my_dict['H'] == 4:
        print(molec_name, 'success')
        counter += 1
        # break



