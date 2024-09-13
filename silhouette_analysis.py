from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans

def calculate_silhouette_score(data, n_clusters):
    """
    Funkce pro výpočet Silhouette Score pro shlukování pomocí K-means.
    
    Parametry:
    - data: pandas DataFrame nebo numpy array obsahující předzpracovaná data
    - n_clusters: počet shluků (k) pro K-means
    
    Vrací:
    - Silhouette Score jako hodnocení kvality shlukování
    """
    # Inicializace K-means s požadovaným počtem shluků
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    
    # Fitting modelu na data
    cluster_labels = kmeans.fit_predict(data)
    
    # Výpočet Silhouette Score
    silhouette_avg = silhouette_score(data, cluster_labels)
    
    print(f"Pro {n_clusters} shluků je průměrné Silhouette Score: {silhouette_avg}")
    return silhouette_avg