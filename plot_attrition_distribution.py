import pandas as pd
import matplotlib.pyplot as plt

def plot_attrition_distribution(data_cleaned):
    # Výpočet počtu zákazníků podle shluků a Attrition_Flag
    attrition_counts = data_cleaned.groupby(['Cluster', 'Attrition_Flag']).size().unstack()

    # Procentuální zastoupení
    attrition_percent = attrition_counts.div(attrition_counts.sum(axis=1), axis=0)

    # Stacked bar plot
    attrition_percent.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='viridis')

    # Nastavení názvu a popisků os
    plt.title('Procentuální rozdělení Attrition_Flag podle shluků')
    plt.xlabel('Shluk')
    plt.ylabel('Procento')

    # Zobrazení grafu
    plt.show()

# Příklad použití:
# plot_attrition_distribution(data_cleaned)