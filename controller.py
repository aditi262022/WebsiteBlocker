import time
from model import WebsiteBlockerModel
from view import WebsiteBlockerView

def block_websites():
    model = WebsiteBlockerModel()
    view = WebsiteBlockerView()
    log_file = "blocked_websites_log.txt"
    redirect = "127.0.0.1"

    while True:
        current_time = model.get_current_time()
        current_day = model.get_current_day()

        # List of websites to block
        site_block = ["ncert.nic.in", "www.facebook.com"]

        # Define schedule for blocking
        block_schedule = {
            "start_time": datetime.time(9, 0),  # Start blocking at 9 AM
            "end_time": datetime.time(17, 0),  # End blocking at 5 PM
            "block_days": [0, 1, 2, 3, 4]  # Weekdays (Monday to Friday)
        }

        if (block_schedule["start_time"] <= current_time <= block_schedule["end_time"]) \
                and (current_day in block_schedule["block_days"]):
            view.display_start_block_message()

            with open(model.host_path, "r+") as host_file:
                content = host_file.read()

                # Block websites not present in the hosts file
                for website in site_block:
                    if website not in content:
                        host_file.write(redirect + " " + website + "\n")
                        view.log_blocked_websites(log_file, website, "Blocked")
        else:
            with open(model.host_path, "r+") as host_file:
                content = host_file.readlines()
                host_file.seek(0)

                # Remove blocked websites if not within scheduled blocking time
                for line in content:
                    if not any(website in line for website in site_block):
                        host_file.write(line)
                        view.log_blocked_websites(log_file, line.strip(), "Unblocked")

                host_file.truncate()

        time.sleep(5)

if __name__ == "__main__":
    block_websites()

#This setup adheres to a more organized MVC pattern, where the Model handles data and logic, the View deals with user interface and output, and the Controller manages the application flow and logic execution.