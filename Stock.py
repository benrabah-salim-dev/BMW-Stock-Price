import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def get_bmw_stock_data(start_year, end_date):
    ticker = "BMW.DE"
    start_date = f"{start_year}-01-01"

    bmw_data = yf.download(ticker, start=start_date, end=end_date)

    if bmw_data.empty:
        print(f"No data found for the specified date range")
        return None

    # Ajouter une nouvelle colonne "ID" avec un identifiant unique pour chaque ligne
    bmw_data['ID'] = range(1, len(bmw_data) + 1)

    return bmw_data

def main():
    start_year = 2000
    end_date = datetime.now().strftime('%Y-%m-%d')

    # Créer un DataFrame vide pour stocker toutes les données
    all_data = pd.DataFrame()

    for year in range(start_year, int(end_date[:4]) + 1):
        stock_data = get_bmw_stock_data(year, end_date)

        if stock_data is not None:
            # Agréger les données par mois et tracer la courbe d'évolution du volume des ventes
            monthly_data = stock_data.resample('M').sum()
            plt.plot(monthly_data.index, monthly_data['Volume'], label=f'{year}')

            # Ajouter les données agrégées au DataFrame global
            all_data = pd.concat([all_data, monthly_data])

    # Sauvegarder le DataFrame agrégé dans un fichier CSV avec la nouvelle colonne "ID"
    all_data.to_csv('bmw_stock_data_aggregated_monthly.csv', index=True)

    # Afficher le graphique
    plt.title('Évolution Mensuelle du Volume des Ventes des Actions de BMW')
    plt.xlabel('Date')
    plt.ylabel('Volume des Ventes des Actions')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
