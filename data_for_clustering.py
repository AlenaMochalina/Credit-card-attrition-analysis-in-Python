
from sklearn.preprocessing import StandardScaler
import pandas as pd

def preprocess_for_clustering(data):
    """
    Funkce pro preprocessing dat pro shlukování.
    - Kategoriální data se zakódují pomocí One-Hot Encoding.
    - Numerická data se standardizují pomocí StandardScaler.
    - Nepotřebné sloupce se odstraní.
    """
    # Odstraníme nepotřebné sloupce
    data = data.drop(columns=[
        'CLIENTNUM', 
        'Attrition_Flag', 
        'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1',
        'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2'
    ])
    
    # Použijeme One-Hot Encoding na kategoriální proměnné
    data = pd.get_dummies(data, drop_first=True)
    
    # Standardizujeme numerická data
    scaler = StandardScaler()
    numeric_columns = data.select_dtypes(include=['int64', 'float64']).columns
    data[numeric_columns] = scaler.fit_transform(data[numeric_columns])
    
    return data, scaler

# Načtení dat
data = pd.read_csv(file_path)

# Předzpracování dat
processed_data, scaler = preprocess_for_clustering(data)

print(processed_data.head())
