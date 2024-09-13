import seaborn as sns
import matplotlib.pyplot as plt

def plot_cluster_analysis(data_cleaned):
    # Výpočet počtu zákazníků v každém shluku
    cluster_counts = data_cleaned['Cluster'].value_counts()

    # Vykreslení boxplotu pro úvěrový limit s počtem zákazníků pod shlukem
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Cluster', y='Credit_Limit', data=data_cleaned)
    plt.title('Rozdíly v úvěrovém limitu mezi shluky')

    # Přidání počtu zákazníků pod každým shlukem
    xticks_labels = [f'Cluster {int(cluster)}\n(n={cluster_counts[cluster]})' for cluster in sorted(cluster_counts.index)]
    plt.xticks(ticks=range(len(cluster_counts)), labels=xticks_labels)

    # Zobrazení grafu
    plt.show()

    # Boxplot pro průměrnou míru využití úvěru mezi shluky
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Cluster', y='Avg_Utilization_Ratio', data=data_cleaned)
    plt.title('Rozdíly v průměrné míře využití úvěru mezi shluky')
    plt.show()

    # Boxplot pro počet transakcí mezi shluky
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Cluster', y='Total_Trans_Ct', data=data_cleaned)
    plt.title('Rozdíly v počtu transakcí mezi shluky')
    plt.show()