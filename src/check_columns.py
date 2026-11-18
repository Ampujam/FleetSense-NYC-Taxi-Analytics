
from pathlib import Path
import duckdb

# Find the main project folder
project_folder = Path(__file__).resolve().parent.parent

# Locate January's taxi data
file_path = project_folder / "Data" / "Raw" / "yellow_tripdata_2025-01.parquet"

# Open DuckDB
con = duckdb.connect()

# Check column names and data types
columns = con.execute(
    "DESCRIBE SELECT * FROM read_parquet(?)",
    [str(file_path)]
).df()

# Display the results
print(columns.to_string(index=False))

# Close DuckDB
con.close()

