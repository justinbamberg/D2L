import pandas as pd

# Load the Excel file
file_path = 'd2l_fusion_schedule_stripped.csv'  # Update this to the correct path
df = pd.read_csv(file_path)

# Function to add AM/PM to the time strings based on specific ranges
def add_ampm(time_str):
    start_time, end_time = time_str.split(' - ')
    start_hour = int(start_time.split(':')[0])
    end_hour = int(end_time.split(':')[0])

    # Add AM/PM to the start time
    if 7 <= start_hour < 12 or (start_hour == 12 and 'AM' not in start_time):
        start_time += " AM"
    else:
        start_time += " PM"
    
    # Add AM/PM to the end time
    if 7 <= end_hour < 12 or (end_hour == 12 and 'AM' not in end_time):
        end_time += " AM"
    else:
        end_time += " PM"

    return f"{start_time} - {end_time}"

# Apply the function to the Time column
df['Time'] = df['Time'].apply(add_ampm)

# Save the updated DataFrame to a new CSV file
output_file_path = 'd2l_fusion_schedule_with_ampm.csv'  # Update this to the desired output path
df.to_csv(output_file_path, index=False)

print(f"Updated CSV file saved to {output_file_path}")
