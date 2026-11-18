
from pathlib import Path
import duckdb

# Find the main project folder
project_folder = Path(__file__).resolve().parent.parent

# Locate the 12 monthly taxi files
raw_folder = project_folder / "Data" / "Raw"

# Connect to DuckDB
con = duckdb.connect()

total_trips = 0

# Count trips for January to December
for month in range(1, 13):

    file_name = f"yellow_tripdata_2025-{month:02d}.parquet"
    file_path = raw_folder / file_name

    if not file_path.exists():
        print("File missing:", file_name)
        continue

    trip_count = con.execute(
        "SELECT COUNT(*) FROM read_parquet(?)",
        [str(file_path)]
    ).fetchone()[0]

    print(file_name, ":", trip_count, "trips")

    total_trips += trip_count

# Display the total
print("Total trips across all 12 months:", total_trips)

con.close()
