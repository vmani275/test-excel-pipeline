from pathlib import Path
import pandas as pd

def main():
    repo_root = Path(__file__).resolve().parents[1]
    data_dir = repo_root / "data"
    out_path = repo_root / "main.xlsx"

    csv_paths = sorted(data_dir.glob("*.csv"))
    if not csv_paths:
        raise SystemExit(f"No CSV files found in {data_dir}")

    dfs = []
    for p in csv_paths:
        df = pd.read_csv(p)
        dfs.append(df)

    combined = pd.concat(dfs, ignore_index=True)
    combined.to_excel(out_path, index=False)

    print(f"Wrote {len(combined)} rows to {out_path}")

if __name__ == "__main__":
    main()

