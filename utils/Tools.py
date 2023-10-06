from datetime import datetime


class Tools:
    def getCurrentTime():
        # Get the current timestamp as a datetime object
        now = datetime.now()
        # If you want it in a specific format as a string
        timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")
        return timestamp_str
