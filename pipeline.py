import duckdb
import pandas as pd

def run_transformation_pipeline():
    print("Starting data transformation pipeline...")
    
    try:
        df = pd.read_csv("raw_imdb_data.csv")
    except FileNotFoundError:
        print("Error: raw_imdb_data.csv not found! Run scraper.py first.")
        return

    print("Cleaning and loading data into DuckDB...")
    
    # CONNECT TO A CLEAN NEW SPACE DATABASE FILE
    conn = duckdb.connect("space_missions.db")
    
    # Drop old table and create a fresh clean scientific table
    conn.execute("DROP TABLE IF EXISTS space_data;")
    conn.execute("""
        CREATE TABLE space_data AS 
        SELECT 
            discovery_method AS Title, 
            release_year AS Release_Year, 
            distance_score AS Score 
        FROM df;
    """)
    
    print("\n--- Sample Database Query Results (Top 5 Records) ---")
    print(conn.execute("SELECT * FROM space_data LIMIT 5;").fetchdf())
    conn.close()
    print("\nPipeline complete! Database updated successfully.")

if __name__ == "__main__":
    run_transformation_pipeline()