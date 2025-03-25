import time

# Function to get the current timestamp in 'YYYY-MM-DD HH:MM:SS' format
def get_timestamp():
    t = time.localtime()  # Get the current time as a tuple (year, month, day, hour, minute, second, ...)
    return "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(t[0], t[1], t[2], t[3], t[4], t[5])


# Function to log messages with the current timestamp
def log(message):
    timestamp = get_timestamp()
    print(f"{timestamp} - {message}")

""" # Example usage:
log("This is a test message.")
 """