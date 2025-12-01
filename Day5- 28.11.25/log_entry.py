from datetime import datetime
def logEntry(msg):
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    with open("logss.txt","w") as f:
        content = f"{timestamp} {msg}"
        f.write(content)

msg = input("Enter the logs: ")
while True:
    if msg.lower() == "quit":
        break
    logEntry(msg)

