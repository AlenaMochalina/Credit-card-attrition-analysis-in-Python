import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

def visualize_pca_kmeans_3d(processed_data, n_clusters=4):
    """
    Funkce pro vizualizaci K-means shlukování v 3D pomocí PCA.
    
    Parametry:
    - processed_data: pandas DataFrame nebo numpy array obsahující předzpracovaná data
    - n_clusters: počet shluků (defaultně 4)
    """
    # K-means pro vytvoření shluků
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(processed_data)

    # PCA pro snížení rozměrnosti na 3D
    pca_3d = PCA(n_components=3)
    principal_components_3d = pca_3d.fit_transform(processed_data)

    # Vytvoření DataFrame pro PCA výsledky a přiřazení shluků
    pc_df_3d = pd.DataFrame(data=principal_components_3d, columns=['PC1', 'PC2', 'PC3'])
    pc_df_3d['Cluster'] = cluster_labels

    # Vykreslení 3D grafu s barevnými shluky
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Vytvoření scatter plotu, kde každý shluk bude mít jinou barvu
    scatter = ax.scatter(pc_df_3d['PC1'], pc_df_3d['PC2'], pc_df_3d['PC3'], 
                         c=pc_df_3d['Cluster'], cmap='viridis', alpha=0.5)

    # Přidání legendy
    legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
    ax.add_artist(legend1)

    # Nastavení popisků a mřížky
    ax.set_title('PCA 3D Projection with K-means Clusters')
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    ax.set_zlabel('Principal Component 3')

    # Zobrazení grafu
    plt.show()

# Příklad použití:
# visualize_pca_kmeans_3d(processed_data, n_clusters=4)