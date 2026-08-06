import os
import random
from datetime import datetime
import time

log_file = "activity_log.txt"

# Pick a random number of commits to do today (between 1 and 5)
num_commits = random.randint(1, 5)

for i in range(num_commits):
    # Append timestamp line
    with open(log_file, "a") as f:
        f.write(f"Commit {i+1}/{num_commits} on {datetime.now()}\n")
    
    # Execute Git commands
    os.system("git add .")
    os.system(f'git commit -m "Automated update component {i+1}"')
    
    # Tiny pause to ensure timestamps are slightly spread out
    time.sleep(1)

# Push all the day's commits to GitHub at once
os.system("git push origin main")

