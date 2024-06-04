import pandas as pd

# Load the Excel file
file_path = 'd2l_fusion_schedule.csv'  # Update this path to the location of your file
df = pd.read_csv(file_path)

# Function to strip AM/PM from the time strings
def strip_ampm(time_str):
    return time_str.replace('AM', '').replace('PM', '').strip()

# Apply the function to the Time column
df['Time'] = df['Time'].apply(strip_ampm)

# Save the updated DataFrame to a new Excel file
output_file_path = 'd2l_fusion_schedule_stripped.csv'
df.to_csv(output_file_path, index=False)

print(f"Updated file saved to {output_file_path}")
