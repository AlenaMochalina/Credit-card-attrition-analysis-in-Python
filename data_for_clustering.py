from sklearn.preprocessing import LabelEncoder, StandardScaler
import pandas as pd

def preprocess_for_clustering(data):
    """
    Funkce pro preprocessing dat pro shlukování.
    - Kategoriální data se zakódují pomocí LabelEncoder.
    - Numerická data se standardizují pomocí StandardScaler.
    - Nepotřebné sloupce se odstraní.
    """
    # Odstraníme nepotřebné sloupce a použijeme errors='ignore' pro případ, že některé sloupce neexistují
    data = data.drop(columns=[
        'CLIENTNUM', 
        'Attrition_Flag', 
        'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1',
        'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2'
    ], errors='ignore')
    
    # Inicializujeme LabelEncodery pro každý kategoriální sloupec
    label_encoders = {}
    categorical_columns = data.select_dtypes(include=['object']).columns
    
    for column in categorical_columns:
        label_encoder = LabelEncoder()
        data[column] = label_encoder.fit_transform(data[column])
        label_encoders[column] = label_encoder
    
    # Standardizujeme numerická data
    scaler = StandardScaler()
    numeric_columns = data.select_dtypes(include=['int64', 'float64']).columns
    data[numeric_columns] = scaler.fit_transform(data[numeric_columns])
    
    return data, label_encoders, scaler
