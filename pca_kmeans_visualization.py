import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import pandas as pd

def visualize_pca_kmeans(processed_data, n_clusters=4):
    """
    Funkce pro vizualizaci K-means shlukování v 2D pomocí PCA.
    
    Parametry:
    - processed_data: pandas DataFrame nebo numpy array obsahující předzpracovaná data
    - n_clusters: počet shluků (defaultně 4)
    """
    # Použití K-means pro vytvoření shluků
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(processed_data)

    # PCA pro snížení rozměrnosti na 2D
    pca_2d = PCA(n_components=2)
    principal_components_2d = pca_2d.fit_transform(processed_data)

    # Vytvoření DataFrame pro PCA výsledky a přiřazení shluků
    pc_df_2d = pd.DataFrame(data=principal_components_2d, columns=['PC1', 'PC2'])
    pc_df_2d['Cluster'] = cluster_labels

    # Vykreslení 2D grafu s barevnými shluky
    plt.figure(figsize=(10, 6))

    # Vytvoření scatter plotu, kde každý shluk bude mít jinou barvu
    scatter = plt.scatter(pc_df_2d['PC1'], pc_df_2d['PC2'], c=pc_df_2d['Cluster'], cmap='viridis', alpha=0.5)

    # Přidání legendy
    legend1 = plt.legend(*scatter.legend_elements(), title="Clusters")
    plt.gca().add_artist(legend1)

    # Popisky a mřížka
    plt.title('PCA 2D Projection with K-means Clusters')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.grid(True)
    plt.show()