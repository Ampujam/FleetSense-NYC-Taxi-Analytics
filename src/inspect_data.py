
from pathlib import Path
import duckdb

project_folder = Path(__file__).resolve().parent.parent

file_path = project_folder / "Data" / "Raw" / "yellow_tripdata_2025-01.parquet"

con = duckdb.connect()

result = con.execute(
    "SELECT * FROM read_parquet(?) LIMIT 5",
    [str(file_path)]
).df()

print(result.to_string(index=False))

con.close()
trip_count = con.execute(
    "SELECT COUNT(*) FROM read_parquet(?)",
    [str(file_path)]
).fetchone()[0]

print("Total January 2025 taxi trips:", trip_count)
