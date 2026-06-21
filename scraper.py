import pandas as pd
import seaborn as sns

def fetch_nasa_dataset():
    print("Connecting to official Python dataset repository...")
    
    try:
        # Automatically loads the real NASA dataset
        df = sns.load_dataset("planets")
        
        # Select exactly 3 columns: method, year, and distance
        raw_df = df[['method', 'year', 'distance']].dropna()
        
        # Give them exactly 3 clean names so there is no mismatch error
        raw_df.columns = ['discovery_method', 'release_year', 'distance_score']
        
        # Save it as our raw data file
        raw_df.to_csv("raw_imdb_data.csv", index=False)
        print(f"Success! Automatically loaded {len(raw_df)} real records!")
        
    except Exception as e:
        print(f"Failed to load dataset. Error: {e}")

if __name__ == "__main__":
    fetch_nasa_dataset()