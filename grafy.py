import matplotlib.pyplot as plt
import seaborn as sns
def plot_histograms(data):
    plt.figure(figsize=(20, 15))
    
    # Number of features
    n_features = len(data.columns)

    # Plot each feature as a histogram
    for i, column in enumerate(data.columns, 1):
        plt.subplot((n_features // 4) + 1, 4, i)  # Adjust the grid size based on the number of features
        sns.histplot(data[column], kde=False, bins=30)
        plt.title(column)

    plt.tight_layout()
    plt.show()

    