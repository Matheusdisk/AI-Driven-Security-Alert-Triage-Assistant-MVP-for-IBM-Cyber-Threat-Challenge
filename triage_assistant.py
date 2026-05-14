import json
import os
def load_alert(alert_path):
    with open(alert_path, "r") as f:
        return json.load(f)
def display_alert(alert_data):
    print("\n================ ALERT LOADED ================\n")
    print(json.dumps(alert_data, indent=4))
    print("\n==============================================\n")
def main():
    print("AI-Driven Security Alert Triage Assistant")
    print("=========================================")
    alerts_folder = "alerts"
    alerts = os.listdir(alerts_folder)
    print("\nAvailable alerts:")
    for i, alert in enumerate(alerts):
        print(f"{i+1}. {alert}")
    choice = int(input("\nChoose an alert to view (1-3): "))
    alert_file = alerts[choice - 1]
    alert_path = os.path.join(alerts_folder, alert_file)
    alert_data = load_alert(alert_path)
    display_alert(alert_data)
    print("Next step: Send this alert to Bob for analysis.")
    print("Copy the displayed JSON and paste it into Bob using your triage prompt.")
    print("\n====================================================")
if __name__ == "__main__":
    main()