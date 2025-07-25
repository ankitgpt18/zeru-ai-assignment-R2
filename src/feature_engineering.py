import os
import json
import pandas as pd

RAW_DATA_DIR = os.path.join('..', 'data', 'compound_raw')
FEATURES_CSV = os.path.join('..', 'data', 'wallet_features.csv')

# Mainnet Compound V2 contract addresses (cTokens, Comptroller, etc.)
COMPOUND_CONTRACTS = set([
    # Comptroller
    '0x3d9819210a31b4961b30ef54be2aed79b9c9cd3b',
    # cTokens (partial list, add more as needed)
    '0x5d3a536e4d6dbd6114cc1ead35777bab948e3643', # cDAI
    '0x39aa39c021dfbae8fac545936693ac917d5e7563', # cUSDC
    '0x6c8c6b02e7b2be14d4fa6022dfd6dbe6bdfb9e2d', # cBAT
    '0x158079ee67fce2f58472a96584a73c7ab9ac95c1', # cREP
    '0x4ddc2d193948926d02f9b1fe9e1daa0718270ed5', # cETH
    '0xf5dce57282a584d2746faf1593d3121fcac444dc', # cWBTC
    '0x95b4ef2869ebd94beb4eee400a99824bf5dc325b', # cSAI
    '0x35a18000230da775cac24873d00ff85bccded550', # cUNI
    '0xface851a4921ce59e912d19329929ce6da6eb0c7', # cCOMP
    # ... add more as needed
])

# Extract features for a single wallet
def extract_features(wallet, data):
    txs = data.get('data', {}).get('items', [])
    compound_txs = [tx for tx in txs if tx.get('to_address', '').lower() in COMPOUND_CONTRACTS or tx.get('from_address', '').lower() in COMPOUND_CONTRACTS]
    # Count unique Compound contracts interacted with (proxy for asset diversity)
    assets = set(tx.get('to_address', '').lower() for tx in compound_txs if tx.get('to_address', '').lower() in COMPOUND_CONTRACTS)
    # Count method signatures for borrow/repay (simplified, real parsing would use input data)
    n_borrows = sum(1 for tx in compound_txs if 'borrow' in (tx.get('decoded', {}).get('name', '') or '').lower())
    n_repays = sum(1 for tx in compound_txs if 'repay' in (tx.get('decoded', {}).get('name', '') or '').lower())
    n_liquidations = sum(1 for tx in compound_txs if 'liquidat' in (tx.get('decoded', {}).get('name', '') or '').lower())
    return {
        'wallet_id': wallet,
        'n_borrows': n_borrows,
        'n_repays': n_repays,
        'n_liquidations': n_liquidations,
        'n_assets': len(assets),
    }

def main():
    features = []
    for fname in os.listdir(RAW_DATA_DIR):
        if fname.endswith('.json'):
            wallet = fname.replace('.json', '')
            with open(os.path.join(RAW_DATA_DIR, fname), 'r') as f:
                data = json.load(f)
            feats = extract_features(wallet, data)
            features.append(feats)
    df = pd.DataFrame(features)
    df.to_csv(FEATURES_CSV, index=False)

if __name__ == "__main__":
    main() 