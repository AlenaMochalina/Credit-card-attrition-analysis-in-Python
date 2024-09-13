import pandas as pd

def calculate_cluster_attrition(data_cleaned):
    # Výpočet počtu zákazníků podle shluků a jejich Attrition_Flag
    cluster_attrition_counts = data_cleaned.groupby(['Cluster', 'Attrition_Flag']).size().unstack(fill_value=0)

    # Výpočet celkového počtu zákazníků v každém shluku
    total_customers_per_cluster = data_cleaned['Cluster'].value_counts().sort_index()

    # Přidání sloupce s celkovým počtem zákazníků pro lepší přehled
    cluster_attrition_counts['Total_Customers'] = total_customers_per_cluster

    # Zobrazení výsledků v přehledné tabulce
    cluster_attrition_counts.columns = ['Odešli', 'Zůstali', 'Celkem']
    cluster_attrition_counts.reset_index(inplace=True)

    # Zobrazení přehledné tabulky
    print(cluster_attrition_counts)

    return cluster_attrition_counts

# Příklad použití:
# result = calculate_cluster_attrition(data_cleaned)