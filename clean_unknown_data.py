import pandas as pd

def clean_unknown_values(data):
    # 1. Rozdělení věku do skupin
    bins = [0, 30, 40, 50, 60, 100]  # Definujeme věkové kategorie
    labels = ['<30', '30-40', '40-50', '50-60', '60+']
    data['Age_Group'] = pd.cut(data['Customer_Age'], bins=bins, labels=labels, right=False)

    # 2. Náhrada hodnot 'Unknown' v Education_Level na základě příjmu a pohlaví
    education_mode_by_income_gender = data[data['Education_Level'] != 'Unknown'].groupby(['Income_Category', 'Gender'])['Education_Level'].agg(lambda x: x.mode()[0])

    def replace_unknown_education(row):
        if row['Education_Level'] == 'Unknown':
            try:
                return education_mode_by_income_gender.loc[(row['Income_Category'], row['Gender'])]
            except KeyError:
                return row['Education_Level']  # Pokud kombinace neexistuje, vrátíme původní hodnotu
        else:
            return row['Education_Level']

    data['Education_Level'] = data.apply(replace_unknown_education, axis=1)

    # 3. Náhrada hodnot 'Unknown' v Income_Category na základě vzdělání, pohlaví a věku
    income_mode_by_education_gender_age = data[data['Income_Category'] != 'Unknown'].groupby(['Education_Level', 'Gender', 'Age_Group'])['Income_Category'].agg(lambda x: x.mode()[0])

    def replace_unknown_income(row):
        if row['Income_Category'] == 'Unknown':
            try:
                return income_mode_by_education_gender_age.loc[(row['Education_Level'], row['Gender'], row['Age_Group'])]
            except KeyError:
                return row['Income_Category']  # Pokud kombinace neexistuje, vrátíme původní hodnotu
        else:
            return row['Income_Category']

    data['Income_Category'] = data.apply(replace_unknown_income, axis=1)

    # 4. Náhrada hodnot 'Unknown' v Marital_Status na základě pohlaví, věku a počtu závislých osob
    marital_mode_by_gender_age_dependents = data[data['Marital_Status'] != 'Unknown'].groupby(['Gender', 'Age_Group', 'Dependent_count'])['Marital_Status'].agg(lambda x: x.mode()[0])

    def replace_unknown_marital_status(row):
        if row['Marital_Status'] == 'Unknown':
            try:
                return marital_mode_by_gender_age_dependents.loc[(row['Gender'], row['Age_Group'], row['Dependent_count'])]
            except KeyError:
                return row['Marital_Status']  # Pokud kombinace neexistuje, vrátíme původní hodnotu
        else:
            return row['Marital_Status']

    data['Marital_Status'] = data.apply(replace_unknown_marital_status, axis=1)

    # Ověříme, že už nejsou žádné 'Unknown' hodnoty
    unknown_columns = ['Education_Level', 'Income_Category', 'Marital_Status']
    for column in unknown_columns:
        unknown_count = data[data[column] == 'Unknown'].shape[0]
        print(f"Počet zbývajících 'Unknown' hodnot ve sloupci {column}: {unknown_count}")

    return data

# Příklad použití funkce
# data = pd.read_csv('path_to_your_dataset.csv')  # Načteme dataset
# data_cleaned = clean_unknown_values(data)  # Vyčistíme data