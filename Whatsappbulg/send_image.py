import pywhatkit as kit
import pandas as pd
import time

# upLoad contacts
df = pd.read_excel("contacts.xlsx")

# Image path
image_path = ("Images/img.jpeg")

# GitHub link
github_link = "https://github.com/Eisha-Mushtaq9"

# Loop through contacts and send image with caption
for index, row in df.iterrows():
    phone_number = f"+{row['Contacts']}"  # Make sure it's in correct format
    caption = f"""Allah is the best of planners.\n{github_link}"""

    try:
        kit.sendwhats_image(phone_number, image_path, caption=caption, wait_time=10)
        print(f"Image sent to {phone_number}")
        time.sleep(5)
    except Exception as e:
        print(f"Failed to send image to {phone_number}: {e}")