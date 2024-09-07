def load_and_preview_data(file_path):
    try:
        # Load the data
        data = pd.read_csv(file_path)
        
        # Preview the first 5 rows of the data
        print(data.head())
        
        return data
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except pd.errors.EmptyDataError as e:
        print(f"Empty data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with the path to your CSV file
data = load_and_preview_data("BankChurners.csv")