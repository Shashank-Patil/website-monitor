import requests
import hashlib
import time
import os
# from dotenv import load_dotenv
from twilio.rest import Client

# Load environment variables from .env file
# load_dotenv()

# Retrieve credentials from environment variables
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
YOUR_PHONE_NUMBER = os.getenv("YOUR_PHONE_NUMBER")
URL = os.getenv("URL")

REFERENCE_FILE = "reference_hash.txt"  # File to store the reference state

# Add headers to mimic a real browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Function to fetch website content with headers
def get_website_content(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching website: {e}")
        return None


# Function to hash content
def hash_content(content):
    return hashlib.sha256(content.encode()).hexdigest()

# Function to save the reference state
def save_reference_hash(content_hash):
    with open(REFERENCE_FILE, "w") as file:
        file.write(content_hash)

# Function to load the reference hash
def load_reference_hash():
    try:
        with open(REFERENCE_FILE, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return None


# Function to trigger a phone call using Twilio
def send_phone_call():
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        call = client.calls.create(
            to=YOUR_PHONE_NUMBER,
            from_=TWILIO_PHONE_NUMBER,
            url="http://demo.twilio.com/docs/voice.xml"
        )
        print(f"Phone call triggered! Call SID: {call.sid}")
    except Exception as e:
        print(f"Error making call: {e}")

# # --- Step 1: Initialize Reference Hash If Not Set ---
# current_content = get_website_content(URL)

# if current_content:
#     current_hash = hash_content(current_content)

#     if not load_reference_hash():
#         print("Saving initial reference state...")
#         save_reference_hash(current_hash)
#     else:
#         print("Reference state already set.")

# # --- Step 2: Start Monitoring ---
# print("Monitoring started...")

# while True:
#     content = get_website_content(URL)
    
#     if content:
#         current_hash = hash_content(content)
#         reference_hash = load_reference_hash()

#         if reference_hash and current_hash != reference_hash:
#             print("Change detected! Calling now...")
#             send_phone_call()
#             save_reference_hash(current_hash)  # Update reference state
        
#     time.sleep(60)  # Check every 60 seconds

def main():
    try:
        content = get_website_content()
        current_hash = hash_content(content)
        reference_hash = load_reference_hash()

        if reference_hash and current_hash != reference_hash:
            print("Change detected! Calling now...")
            send_phone_call()
        else:
            print("No change detected.")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

