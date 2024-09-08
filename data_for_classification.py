from sklearn.preprocessing import LabelEncoder, StandardScaler
import pandas as pd

def preprocess_for_classification(data):
    """
    Funkce pro preprocessing dat pro klasifikaci.
    - Kategoriální data se zakódují pomocí LabelEncoder.
    - Numerická data se standardizují pomocí StandardScaler.
    - Nepotřebné sloupce se odstraní.
    
    Parametry:
    - data: pandas DataFrame obsahující data, která mají být zpracována.
    
    Vrací:
    - zpracovaná data vhodná pro klasifikaci.
    """
    
    # Odstraníme nepotřebné sloupce
    data = data.drop(columns=[
        'CLIENTNUM', 
        'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_WalkIn_Delta_2',
        'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_WalkIn_Delta_1'
    ])
    
    # Inicializujeme LabelEncodery pro každý kategoriální sloupec
    label_encoders = {}
    
    # Identifikujeme kategoriální sloupce - mohou být textové nebo objektového typu
    categorical_columns = data.select_dtypes(include=['object']).columns
    
    # Převedeme kategoriální data pomocí LabelEncoder
    for column in categorical_columns:
        label_encoder = LabelEncoder()
        data[column] = label_encoder.fit_transform(data[column])
        label_encoders[column] = label_encoder
    
    # Standardizujeme numerická data
    scaler = StandardScaler()
    
    # Identifikujeme numerické sloupce
    numeric_columns = data.select_dtypes(include=['int64', 'float64']).columns
    
    # Aplikujeme standardizaci
    data[numeric_columns] = scaler.fit_transform(data[numeric_columns])
    
    return data, label_encoders, scaler


data= pd.read_csv("BankChurners.csv") 
processed_data, label_encoders, scaler = preprocess_for_classification(data)

print(processed_data.head())  