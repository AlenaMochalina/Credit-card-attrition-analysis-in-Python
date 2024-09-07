import pandas as pd

# Definujeme funkci pro načtení a náhled dat
def load_and_preview_data(file_path):
    # Načteme data
    data = pd.read_csv(file_path)
    
    # Zobrazíme základní informace o datech
    print("\nInfo about the dataset:")
    data.info()
    
    # Spočítáme a zobrazíme počet duplicitních řádků
    duplicated_count = data.duplicated().sum()
    print(f"\nNumber of duplicated rows: {duplicated_count}")
    
    # Spočítáme a zobrazíme chybějící hodnoty v každém sloupci
    missing_values = data.isnull().sum()
    print("\nMissing values in each column:")
    print(missing_values)
    
    # Zobrazíme rozměry dat (počet řádků a sloupců)
    print(f"\nShape of the dataset: {data.shape}")
