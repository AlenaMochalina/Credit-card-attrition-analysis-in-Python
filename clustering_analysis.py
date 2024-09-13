import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def elbow_and_silhouette(data, max_clusters=10):
    """
    Funkce pro zobrazení Elbow Method a výpočet Silhouette Score pro určení optimálního počtu shluků.

    Parametry:
    - data: pandas DataFrame nebo numpy array obsahující předzpracovaná data
    - max_clusters: maximální počet shluků pro testování (default je 10)
    """
    # Seznamy pro ukládání hodnot SSE a Silhouette Scores
    sse = []
    silhouette_scores = []

    # Testování počtu shluků od 2 do max_clusters
    for k in range(2, max_clusters + 1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data)
        sse.append(kmeans.inertia_)  # SSE (Sum of Squared Errors)

        # Výpočet Silhouette Score
        cluster_labels = kmeans.predict(data)
        silhouette_avg = silhouette_score(data, cluster_labels)
        silhouette_scores.append(silhouette_avg)

    # Vykreslení Elbow Method (SSE)
    plt.figure(figsize=(14, 6))

    plt.subplot(1, 2, 1)
    plt.plot(range(2, max_clusters + 1), sse, marker='o')
    plt.title('Elbow Method for Optimal k')
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('SSE (Sum of Squared Errors)')

    # Vykreslení Silhouette Score
    plt.subplot(1, 2, 2)
    plt.plot(range(2, max_clusters + 1), silhouette_scores, marker='o', color='green')
    plt.title('Silhouette Score for Different k')
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('Silhouette Score')

    plt.tight_layout()
    plt.show()