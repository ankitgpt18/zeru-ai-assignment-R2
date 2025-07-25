import pandas as pd
import numpy as np
import os

FEATURES_CSV = os.path.join('..', 'data', 'wallet_features.csv')
SCORES_CSV = os.path.join('..', 'output', 'wallet_scores.csv')

# Simple rule-based scoring
# Lower risk: more repays, more assets, fewer liquidations, fewer borrows

def score_row(row):
    score = 500
    score += 100 * min(row['n_repays'], 5)
    score += 50 * min(row['n_assets'], 5)
    score -= 200 * row['n_liquidations']
    score -= 20 * min(row['n_borrows'], 10)
    score = np.clip(score, 0, 1000)
    return int(score)

def main():
    df = pd.read_csv(FEATURES_CSV)
    df['score'] = df.apply(score_row, axis=1)
    df[['wallet_id', 'score']].to_csv(SCORES_CSV, index=False)

if __name__ == "__main__":
    main() 