import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import silhouette_samples
from sklearn.cluster import KMeans

def visualize_silhouette(data, n_clusters):
    """
    Funkce pro vizualizaci Silhouette Score pro jednotlivé shluky.
    
    Parametry:
    - data: pandas DataFrame nebo numpy array obsahující předzpracovaná data
    - n_clusters: počet shluků (k) pro K-means
    """
    # Inicializace K-means
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(data)
    
    # Výpočet Silhouette Score pro každý vzorek
    silhouette_vals = silhouette_samples(data, cluster_labels)
    
    # Nastavení plátna pro vizualizaci
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Vykreslení grafu Silhouette pro každý shluk
    y_lower, y_upper = 0, 0
    yticks = []
    for i in range(n_clusters):
        ith_cluster_silhouette_vals = silhouette_vals[cluster_labels == i]
        ith_cluster_silhouette_vals.sort()
        y_upper += len(ith_cluster_silhouette_vals)
        ax.barh(range(y_lower, y_upper), ith_cluster_silhouette_vals, height=1.0)
        yticks.append((y_lower + y_upper) / 2)
        y_lower += len(ith_cluster_silhouette_vals)

    # Vykreslení průměrné hodnoty Silhouette Score
    silhouette_avg = np.mean(silhouette_vals)
    ax.axvline(silhouette_avg, color="red", linestyle="--")
    
    ax.set_yticks(yticks)
    ax.set_yticklabels([f'Cluster {i}' for i in range(n_clusters)])
    ax.set_xlabel('Silhouette Coefficient')
    ax.set_ylabel('Cluster')
    ax.set_title(f'Silhouette Plot for {n_clusters} Clusters')
    plt.show()