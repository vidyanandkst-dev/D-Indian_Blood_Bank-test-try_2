import streamlit as st

# Step 1: Clean, emoji-free page configuration
st.set_page_config(page_title="Calculator App", layout="centered")

# Step 2: Clean titles and text fields (No complex emojis or symbols)
st.title("Excel to Python Web Application")
st.write("Modify the inputs below to run your equation automatically.")

# Step 3: High-precision Unicode cleaner
def clean_text_input(text):
    if not isinstance(text, str):
        return text
    try:
        # Purges broken code points at positions 63-64 immediately
        return text.encode('utf-8', 'ignore').decode('utf-8')
    except Exception:
        return "Cleaned Entry"

# Step 4: Interface Input Fields
st.header("1. Input Data Fields")

# Raw text tracking input box
raw_user_text = st.text_input("Enter Label or Notes:", value="Project Reference Sheet")
clean_label = clean_text_input(raw_user_text)

# Math Variables (Safe from encoding errors)
input_val_a = st.number_input("Value A (e.g., Base Amount):", min_value=0.0, value=100.0)
input_val_b = st.number_input("Value B (e.g., Tax Rate or Multiplier):", min_value=0.0, value=1.05)

# Step 5: The Equation Logic
# Example: Basic multiplication equation
calculated_output = input_val_a * input_val_b

# Step 6: Render Outputs Safely
st.divider()
st.header("2. Processed Results")

# Display numbers and text cleanly
st.write(f"Line Item: {clean_label}")
st.metric(label="Calculated Target Total", value=f"{calculated_output:,.2f}")
