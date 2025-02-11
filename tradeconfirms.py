import pandas as pd

# Step 1: Read the .sec file content
file_path = str(r"C:\Users\Tony Endress\OneDrive - Foguth Financial Group\Documents\Sch\CRS20240910.TCF")
with open(file_path, 'r') as file:
    lines = file.readlines()

# Step 2: Parse the content
data = [line.strip().split('|') for line in lines]

# Step 3: Create a DataFrame
df = pd.DataFrame(data)
print(df)

# Step 4: Save to Excel
output_file = r'Outputs\Schwab\crs20240910.xlsx'
df.to_excel(output_file, index=False, header=True)

print(f"File saved as {output_file}")