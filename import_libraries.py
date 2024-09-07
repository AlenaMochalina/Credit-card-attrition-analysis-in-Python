def import_libraries():
    try:
        # Data manipulation libraries
        import pandas as pd
        import numpy as np

        # Plotting libraries
        import matplotlib.pyplot as plt
        import seaborn as sns
        from matplotlib.ticker import FixedLocator

        # Preprocessing libraries
        from sklearn.preprocessing import MinMaxScaler, LabelEncoder, StandardScaler
        from sklearn.model_selection import train_test_split

        # Modeling libraries
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.model_selection import GridSearchCV
        from sklearn.cluster import KMeans
        import pickle

        # Evaluation libraries  
        from sklearn.metrics import classification_report, confusion_matrix

        print("All specified libraries have been imported successfully.")
    except ImportError as e:
        print(f"Error importing libraries: {e}")

# Call the function to import the libraries
import_libraries()