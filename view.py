class WebsiteBlockerView:
    @staticmethod
    def log_blocked_websites(log_file, website, action):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {action} {website}\n"
        with open(log_file, "a") as log:
            log.write(log_entry)

    @staticmethod
    def display_start_block_message():
        print("Start blocking the websites!")

    @staticmethod
    def display_end_block_message():
        print("End blocking the websites!")
