import pandas as pd

# Load the CSV file
file_path = "model_data/DATA.csv"  # Replace with your file path if necessary
df = pd.read_csv(file_path)

# Step 1: Delete the first column (Patient_ID)
df = df.drop(columns=['Patient_ID'])


# Step 2: One-hot encode the 'Systemic Illness' column
# Define the order for the systemic illness columns
systemic_illness_order = ['systemic_illness_none', 
                          'systemic_illness_fever', 
                          'systemic_illness_lymphadenopathy', 
                          'systemic_illness_myalgia']

# Create the mapping for the systemic illness categories
systemic_illness_mapping = {
    'No systemic Illness': 'systemic_illness_none',
    'Fever': 'systemic_illness_fever',
    'Swollen Lymph Nodes': 'systemic_illness_lymphadenopathy',
    'Myalgia': 'systemic_illness_myalgia'
}

# Replace the original 'Systemic Illness' values with mapped categories
df['Systemic Illness'] = df['Systemic Illness'].map(systemic_illness_mapping)

# Create dummy variables with ordered columns
dummies = pd.get_dummies(df['Systemic Illness'])

# Ensure the correct order of columns by reindexing
dummies = dummies.reindex(columns=systemic_illness_order, fill_value=0)

# Drop the original 'Systemic Illness' column and concatenate the new OHE columns
df = pd.concat([df.drop(columns=['Systemic Illness']), dummies], axis=1)

# Step 3: Convert True/False columns to 1/0
boolean_columns = ['Rectal Pain', 'Sore Throat', 'Penile Oedema', 'Oral Lesions', 
                   'Solitary Lesion', 'Swollen Tonsils', 'HIV Infection', 
                   'Sexually Transmitted Infection', 'systemic_illness_none', 
                          'systemic_illness_fever', 
                          'systemic_illness_lymphadenopathy', 
                          'systemic_illness_myalgia']

# Convert True/False to 1/0 for the selected columns
df[boolean_columns] = df[boolean_columns].astype(int)

# Step 4: Transform the 'MonkeyPox' column correctly
df['MonkeyPox'] = df['MonkeyPox'].apply(lambda x: 1 if x == 'Positive' else 0)

df = df[[col for col in df.columns if col != 'MonkeyPox'] + ['MonkeyPox']]


print(df)
print(df.columns.tolist())

# Step 5: Write the processed data to 'processed_data.txt' without including column names
output_path = "processed_data.txt"
df.to_csv(output_path, index=False)

print("Processing complete. Data saved to processed_data.txt")
