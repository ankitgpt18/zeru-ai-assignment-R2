import os
import subprocess

# Run all steps in order
if __name__ == "__main__":
    # Fetch Compound data
    subprocess.run(['python', 'fetch_compound_data.py'], cwd='src')
    # Feature engineering
    subprocess.run(['python', 'feature_engineering.py'], cwd='src')
    # Scoring
    subprocess.run(['python', 'risk_model.py'], cwd='src')
    print("Done. Output at output/wallet_scores.csv") 