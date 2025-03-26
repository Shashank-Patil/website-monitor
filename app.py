from flask import Flask, jsonify
import monitor_website  # This is your monitor.py file containing the main monitoring function

app = Flask(__name__)

@app.route('/run-monitor', methods=['GET'])
def run_monitor():
    try:
        monitor_website.main()  # Run your monitoring logic
        return jsonify({"status": "success", "message": "Monitor executed successfully"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
