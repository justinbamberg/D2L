import pandas as pd

# Load the Excel file
file_path = 'd2l_fusion_schedule_with_ampm.csv'  # Adjust the path as needed
df = pd.read_csv(file_path)

# Fill NaN values in the Description column with empty strings
df['Description'] = df['Description'].fillna('')
df['Title'] = df['Title'].fillna('')

# Function to create the Outlook calendar link
def create_outlook_link(date, time, title, description):
    base_url = "https://outlook.office.com/calendar/0/deeplink/compose?subject={}&startdt={}&body={}"
    
    # Convert date to proper format (YYYY-MM-DD)
    date_str = pd.to_datetime(date).strftime('%Y-%m-%d')
    
    # Extract start and end times
    start_time, end_time = time.split(' - ')
    start_time_str = pd.to_datetime(f"{date_str} {start_time}").strftime('%Y-%m-%dT%H:%M:%S')
    
    # Trim the description to a reasonable length
    trimmed_description = (description[:97] + '...') if len(description) > 100 else description
    
    link = base_url.format(title, start_time_str, trimmed_description)
    return link

# Adding the new column with links
df['Outlook Link'] = df.apply(lambda row: create_outlook_link(row['Date'], row['Time'], row['Title'], row['Description']), axis=1)

# Save the updated DataFrame to a new Excel file with clickable links
output_file_path = 'd2l_fusion_schedule_with_links.xlsx'
writer = pd.ExcelWriter(output_file_path, engine='xlsxwriter')
df.to_excel(writer, index=False, sheet_name='Schedule')

# Get the xlsxwriter workbook and worksheet objects
workbook  = writer.book
worksheet = writer.sheets['Schedule']

# Add the hyperlinks with "Add to Calendar" text
for index, row in df.iterrows():
    worksheet.write_url(f'L{index + 2}', row['Outlook Link'], string='Add to Calendar')

# Close the writer object
writer.close()

print(f"Updated schedule with Outlook links saved to {output_file_path}")
