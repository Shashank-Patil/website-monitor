# Website Change Monitor 🚀

This project monitors a webpage for changes and notifies you when an update is detected.

## 📌 How It Works
- Runs **every 5 minutes** using GitHub Actions.
- Compares the current webpage content with a **reference hash**.
- Sends a **notification (e.g., phone call, email, using twilio)** if changes are detected.

## ⚙️ Setup
1. **Fork this repository** or use it directly.
2. **Add required secrets** in **Settings → Secrets and variables → Actions**:
   - `TWILIO_SID` 
   - `TWILIO_AUTH_TOKEN` 
   - `TWILIO_PHONE_NUMBER`
   - `YOUR_PHONE_NUMBER`
   - `URL` (webpage url)
3. **Modify the `reference_hash.txt`** with the expected webpage state.

## 🚀 Running Locally
1. Install dependencies:
   ```bash
   pip install -r requirements.txt 
2. Create a .env file (for local secrets)
3. ```bash
   python monitor_website.py 
