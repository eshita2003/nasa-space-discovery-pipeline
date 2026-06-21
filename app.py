import duckdb
import streamlit as st

st.set_page_config(page_title="Space Discovery Analytics Dashboard", layout="wide")

st.title("🌌 NASA Space Discovery Analytics Dashboard")
st.markdown("This dashboard tracks automated planet discovery logs directly from a local **DuckDB** storage system.")

# Connect to the new space database
try:
    conn = duckdb.connect("space_missions.db")
    df = conn.execute("SELECT * FROM space_data ORDER BY Release_Year DESC;").fetchdf()
    conn.close()
    
    # --- Sidebar Filters ---
    st.sidebar.header("Filter Options")
    min_year = int(df["Release_Year"].min())
    max_year = int(df["Release_Year"].max())
    
    year_range = st.sidebar.slider("Select Year Range", min_year, max_year, (min_year, max_year))
    
    # Apply filters
    filtered_df = df[(df["Release_Year"] >= year_range[0]) & (df["Release_Year"] <= year_range[1])]
    
    # --- Main Metrics ---
    col1, col2 = st.columns(2)
    col1.metric("Total Planets Tracked", len(filtered_df))
    col2.metric("Average Distance Value", f"{round(filtered_df['Score'].mean(), 2)} light-years")
    
    # --- Graphs ---
    st.subheader("📊 Planet Discoveries by Year")
    year_counts = filtered_df.groupby("Release_Year").size().reset_index(name="Total Count")
    st.line_chart(data=year_counts, x="Release_Year", y="Total Count")
    
    # --- Data Table View ---
    st.subheader("📋 Clean Database Table View")
    st.dataframe(filtered_df, use_container_width=True)

except Exception as e:
    st.error("Could not load data from database. Make sure you run scraper.py and pipeline.py first!")
    st.info(f"Technical error: {e}")