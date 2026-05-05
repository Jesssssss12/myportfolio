import pandas as pd
from pathlib import Path

csv_path = Path(__file__).resolve().parent / "static" / "data" / "Met-database-csv.csv"
json_path = Path(__file__).resolve().parent / "static" / "data" / "met_cleaned.json"

if not csv_path.exists():
    raise FileNotFoundError(f"Data file not found: {csv_path}")

df = pd.read_csv(csv_path)

df["year"] = pd.to_numeric(df["year"], errors="coerce")
df["Classification"] = df["Classification"].fillna("Unknown")
df["Object Name"] = df["Object Name"].fillna("Unknown Object")
df["Artist Display Name"] = df["Artist Display Name"].fillna("Unidentified artist")
df["Dynasty"] = df["Dynasty"].fillna("Unknown")

df = df.dropna(subset=["year"])
df = df[(df["year"] >= 0) & (df["year"] <= 2025)]

df = df[
    [
        "year",
        "Classification",
        "Object Name",
        "Artist Display Name",
        "Dynasty",
        "AccessionYear"
    ]
]

df.to_json(json_path, orient="records", force_ascii=False, indent=2)

print(f"Saved cleaned data to: {json_path}")
print(f"Total records: {len(df)}")