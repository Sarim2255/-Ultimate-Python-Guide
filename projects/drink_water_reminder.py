import time
from plyer import notification

while True:
    print("Please drink some water!...")
    notification.notify(title = "Please drink a glass of water...", message = "You need to drink some water...")
    time.sleep(2)