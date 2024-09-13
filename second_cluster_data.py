import pandas as pd

def display_second_cluster_data():
    # Data ve formátu Series
    data_second_cluster = pd.Series({
        (45, 'F', 'Less than $40K'): 125,
        (44, 'F', 'Less than $40K'): 115,
        (43, 'F', 'Less than $40K'): 108,
        (50, 'F', 'Less than $40K'): 106,
        (49, 'F', 'Less than $40K'): 104,
        (60, 'M', '$120K +'): 1,
        (52, 'M', 'Less than $40K'): 1,
        (32, 'M', '$120K +'): 1,
        (35, 'M', 'Less than $40K'): 1,
        (73, 'M', '$40K - $60K'): 1
    }).reset_index(name='count')

    # Přidání názvů sloupců
    data_second_cluster.columns = ['Customer_Age', 'Gender', 'Income_Category', 'Count']

    # Zobrazení DataFrame
    print(data_second_cluster)

# Zavolání funkce z .py souboru
if __name__ == "__main__":
    display_second_cluster_data()