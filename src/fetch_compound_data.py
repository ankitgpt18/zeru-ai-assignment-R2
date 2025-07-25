import os
import csv
import json
import requests
from time import sleep

# Set your API key as an environment variable: COVALENT_API_KEY
COVALENT_API_KEY = os.getenv('COVALENT_API_KEY', 'YOUR_API_KEY')

# Input and output paths
INPUT_CSV = os.path.join('..', 'data', 'wallets.csv')
RAW_DATA_DIR = os.path.join('..', 'data', 'compound_raw')
os.makedirs(RAW_DATA_DIR, exist_ok=True)

# Covalent API endpoint for all transactions (we will filter for Compound in feature engineering)
COVALENT_URL = "https://api.covalenthq.com/v1/1/address/{address}/transactions_v2/"

# Read wallet addresses from CSV
def read_wallets(csv_path):
    wallets = []
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            wallets.append(row['wallet_id'])
    return wallets

# Fetch all transactions for a wallet
def fetch_compound_data(wallet):
    url = COVALENT_URL.format(address=wallet)
    params = {"key": COVALENT_API_KEY}
    resp = requests.get(url, params=params)
    if resp.status_code == 200:
        return resp.json()
    else:
        print(f"Error for {wallet}: {resp.status_code} {resp.text}")
    return None

if __name__ == "__main__":
    wallets = read_wallets(INPUT_CSV)
    for i, wallet in enumerate(wallets):
        print(f"Fetching: {wallet}")
        data = fetch_compound_data(wallet)
        if data:
            with open(os.path.join(RAW_DATA_DIR, f"{wallet}.json"), 'w') as f:
                json.dump(data, f)
        else:
            print(f"Failed for {wallet}")
        sleep(1)  # Be nice to the API 