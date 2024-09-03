import streamlit as st
import pandas as pd

# Display the processed, anonymized, masked, and classified files
st.write("### 🔎 Processed Reviews")
st.write(f"Total Reviews : 1100")
st.dataframe(pd.read_csv("reviews.csv"))
