from pathlib import Path
import csv

def main():
    repo_root = Path(__file__).resolve().parents[1]
    data_dir = repo_root / "data"
    out_path = repo_root / "main.csv"

    csv_paths = sorted(data_dir.glob("*.csv"))
    if not csv_paths:
        raise SystemExit(f"No CSV files found in {data_dir}")

    header_written = False
    out_rows = 0

    with out_path.open("w", newline="", encoding="utf-8") as out_f:
        writer = None

        for p in csv_paths:
            with p.open("r", newline="", encoding="utf-8-sig") as in_f:
                reader = csv.reader(in_f)
                try:
                    header = next(reader)
                except StopIteration:
                    # empty file
                    continue

                if not header_written:
                    writer = csv.writer(out_f)
                    writer.writerow(header)
                    header_written = True
                else:
                    # Ensure headers match exactly
                    if writer is None:
                        raise SystemExit("Internal error: writer not initialized.")
                    if header != first_header:
                        raise SystemExit(
                            f"Header mismatch in {p.name}.\n"
                            f"Expected: {first_header}\n"
                            f"Got:      {header}"
                        )

                # Track header from first non-empty file
                if 'first_header' not in locals():
                    first_header = header

                for row in reader:
                    writer.writerow(row)
                    out_rows += 1

    print(f"Wrote {out_rows} data rows to {out_path}")

if __name__ == "__main__":
    main()


