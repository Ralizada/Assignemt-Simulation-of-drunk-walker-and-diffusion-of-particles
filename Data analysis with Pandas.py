

import pandas as pd
import re


df = pd.read_csv(r'C:\Users\1\PycharmProjects\Test\UFAZ/AminoAcids.csv')
# print(df[:5][:])

print(df[df['Name'] == 'Lysine'])

print(df[df["Molecular Weigth"] == df["Molecular Weigth"].max()])

print(df[df["Polarization"] == 'positive'])

print(df.groupby("Polarization").count())

print(df.loc[df.groupby(["Polarization"])['Molecular Weigth'].idxmax()])

df.groupby("Polarization")["Molecular Weigth"].mean()

df.groupby("Polarization")["Molecular Weigth"].std()


def parse_formula(formula):
    my_dict = {}
    with_indices = re.findall('[A-Z][a-z]*\d+', formula)
    without_indices = re.findall('[A-Z][a-z]*(?![0-9])', formula)

    for part in with_indices:
        elem = re.findall('[A-Z][a-z]*', part)[0]
        if not elem in my_dict:
            my_dict[elem] = int(re.findall('[0-9]+', part)[0])
        else:
            my_dict[elem] += int(re.findall('[0-9]+', part)[0])
    for part in without_indices:
        elem = re.findall('[A-Z][a-z]*', part)[0]
        if elem in my_dict:
            my_dict[elem] += 1
        else:
            my_dict[elem] = 1
    return my_dict


print(df['Molecular Formula'].map(parse_formula))

dictionaries = df['Molecular Formula'].map(parse_formula)
df['H'] = [dct['H'] for dct in dictionaries]
df['C'] = [dct['C'] for dct in dictionaries]
df['N'] = [dct['N'] for dct in dictionaries]
df['O'] = [dct['O'] for dct in dictionaries]

print(df.sort_values("H", ascending=False).head(2))

df.to_csv(r"C:\Users\1\PycharmProjects\Test\UFAZ/NewAminoAcids.csv", index=False)
