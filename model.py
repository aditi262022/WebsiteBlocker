import platform
import datetime

class WebsiteBlockerModel:
    def __init__(self):
        self.host_path = self.get_host_path()

    def get_host_path(self):
        system_platform = platform.system()
        if system_platform == 'Windows':
            return "C:/Windows/System32/drivers/etc/hosts"
        elif system_platform == 'Darwin':
            return "/private/etc/hosts"
        else:
            return "/etc/hosts"

    def get_current_time(self):
        return datetime.datetime.now().time()

    def get_current_day(self):
        return datetime.datetime.now().weekday()
