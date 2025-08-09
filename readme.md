# 🏦 Compound V2 Wallet Risk Scoring

![repo public](https://img.shields.io/badge/repo-public-brightgreen)

---

## 📚 About This Project

This repository is my submission for the Zeru AI Engineer Internship assignment round 2.
Update : Got selected for this role.

It demonstrates my ability to design, implement, and analyze a robust, transparent risk scoring system for DeFi wallets using real Compound V2 transaction data. The solution is fully original, interpretable, and designed for extensibility.

---

## 🧠 Methodology & Approach

- **Feature Engineering:**  
  Extract wallet-level features from raw transaction data, including:  
    - Action counts (borrows, repays, liquidations, etc.)  
    - Asset diversity  
    - Behavioral ratios  
- **Scoring Model:**  
  A clear, rule-based model rewards responsible DeFi behavior and penalizes risky actions.  
  Scores are mapped to the 0-1000 range for easy interpretation.
- **Analysis:**  
  Score distributions and wallet behavior insights are provided in the output.

---

## 🗂️ Project Structure

```
.
├── data/
│   └── wallets.csv
├── src/
│   ├── fetch_compound_data.py
│   ├── feature_engineering.py
│   ├── risk_model.py
│   └── score_wallets.py
├── output/
│   └── wallet_scores.csv
├── readme.md
├── requirements.txt
├── .gitignore
```

---

## ⚡ How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Place your wallet list:**
   - Save your wallet addresses as `wallets.csv` in the `data/` folder (one column: `wallet_id`).
3. **Set your Covalent API key as an environment variable:**
   - On Windows (Command Prompt):
     ```cmd
     set COVALENT_API_KEY=ckey_your_actual_api_key_here
     ```
   - On PowerShell:
     ```powershell
     $env:COVALENT_API_KEY="ckey_your_actual_api_key_here"
     ```
   - On Linux/Mac:
     ```bash
     export COVALENT_API_KEY=ckey_your_actual_api_key_here
     ```
4. **Run the pipeline:**
   ```bash
   python src/score_wallets.py
   ```
   - The output will be saved as `output/wallet_scores.csv`.

> **Note:** Set your Covalent API key as an environment variable before running the scripts. The API key is not included in the code for security reasons.

---

## 📋 Brief Explanation

- **Data Collection:**  
  Wallet transaction data is fetched from the Compound protocol using the Covalent API for each address.
- **Feature Selection:**  
  Features include number of borrows, repays, liquidations, and unique assets interacted with.
- **Scoring Method:**  
  The model rewards wallets with more repays and asset diversity, and penalizes those with more liquidations and excessive borrowing.
- **Risk Indicators:**  
  Liquidations and high borrow counts are considered riskier, while repays and asset diversity indicate responsible behavior.

---

For any questions or suggestions, feel free to reach out or open an issue. 
