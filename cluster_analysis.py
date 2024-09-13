import pandas as pd

def analyze_clusters(data_cleaned, cluster_labels):
    """
    Funkce pro přidání štítků shluků do datasetu, výpočet průměrných hodnot 
    pro numerické proměnné v každém shluku a přidání procentuálního rozdělení 
    'Attrition_Flag'. Zobrazí výsledky v přehledné tabulce.
    
    Parametry:
    - data_cleaned: původní nebo předzpracovaný dataset
    - cluster_labels: štítky shluků vytvořené K-means algoritmem
    """
    # Přidání štítků shluků (cluster_labels) do datasetu
    data_cleaned['Cluster'] = cluster_labels

    # Zobrazení prvních několika řádků datasetu s přiřazenými shluky
    print(data_cleaned.head())
    
    # Výběr pouze numerických sloupců
    numerical_columns = data_cleaned.select_dtypes(include=['number']).columns

    # Výpočet průměrných hodnot pro numerické proměnné v každém shluku
    cluster_analysis = data_cleaned.groupby('Cluster')[numerical_columns].mean()

    # Přidání procentuálního rozdělení Attrition_Flag v rámci každého shluku
    attrition_distribution = data_cleaned.groupby('Cluster')['Attrition_Flag'].value_counts(normalize=True).unstack()

    # Spojení obou tabulek: numerické hodnoty a procenta Attrition_Flag
    final_analysis = pd.concat([cluster_analysis, attrition_distribution], axis=1)

    # Zobrazení výsledků v přehledné tabulce
    display(final_analysis)

# Příklad použití funkce
# analyze_clusters(data_cleaned, cluster_labels)