import os
import requests
from pathlib import Path

# Define the base URL and target directory
base_url = "https://prezydent2000.pkw.gov.pl/gminy/gm-okr"
target_dir = "/Users/kuchta/PycharmProjects/elections-notebook/datasets/2000"

# Create the target directory if it doesn't exist
Path(target_dir).mkdir(parents=True, exist_ok=True)

# Loop through districts 1 to 68
for i in range(1, 69):
    # Format the file number with leading zero if needed (e.g., 01, 02, ..., 68)
    file_number = f"{i:02d}"
    file_url = f"{base_url}{file_number}.xls"
    file_path = os.path.join(target_dir, f"gm-okr{file_number}.xls")

    try:
        # Send GET request to download the file
        response = requests.get(file_url, timeout=10)

        # Check if the request was successful
        if response.status_code == 200:
            # Save the file to the target directory
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: gm-okr{file_number}.xls")
        else:
            print(f"Failed to download gm-okr{file_number}.xls - Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading gm-okr{file_number}.xls: {e}")

print("Download process completed.")