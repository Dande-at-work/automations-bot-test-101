import os
from datetime import datetime

# Path to the file we will modify
log_file = "activity_log.txt"

# Append current timestamp to create a file change
with open(log_file, "a") as f:
    f.write(f"Commit on {datetime.now()}\n")

# Execute Git commands
os.system("git add .")
os.system('git commit -m "Automated daily update"')
os.system("git push origin main")

