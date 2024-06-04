import time  # Add this line to import the time module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import json
import re

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the URL
url = 'https://www.d2l.com/fusion/schedule/'
driver.get(url)

# Allow time for the page to load
time.sleep(10)

# Extract the script content with JSON data
script_element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//script[contains(text(), 'let jsonData = ')]"))
)
script_content = script_element.get_attribute('innerHTML')

# Extract JSON data from the script content
json_data_match = re.search(r'let jsonData = ({.*});', script_content, re.DOTALL)
json_data = json.loads(json_data_match.group(1)) if json_data_match else {}

# Parse JSON data to extract session details
sessions = []
for session_id, session_info in json_data.items():
    date = session_info.get('start_date_formatted', 'N/A')
    time_range = f"{session_info.get('start_time_formatted', 'N/A')} - {session_info.get('end_time_formatted', 'N/A')}"
    title = session_info.get('title', 'N/A')
    location = session_info.get('location', 'N/A')
    description = session_info.get('description', 'N/A')
    formats = ", ".join(session_info.get('formats', []))
    topics = ", ".join(session_info.get('topicsArray', []))
    audience = ", ".join(session_info.get('audienceArray', []))
    skill_level = ", ".join(session_info.get('skill_levelArray', []))
    speakers = session_info.get('speakers', 'N/A')

    # Append to sessions list
    sessions.append([date, time_range, title, location, description, formats, topics, audience, skill_level, speakers])

# Create a DataFrame
df = pd.DataFrame(sessions, columns=['Date', 'Time', 'Title', 'Location', 'Description', 'Formats', 'Topics', 'Audience', 'Skill Level', 'Speakers'])

# Display the organized schedule
print(df)

# Export to CSV
df.to_csv('d2l_fusion_schedule.csv', index=False)

# Close the WebDriver
driver.quit()
