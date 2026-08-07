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
exit_status = os.system("git push origin main")

# If the push was successful (exit status 0), send a notification alert!
if exit_status == 0:
    os.system(f'termux-notification --title "GitHub Bot Success" --content "Successfully pushed {num_commits} random commits to your graph!" --id 99')
else:
    os.system('termux-notification --title "GitHub Bot Failed" --content "There was an error pushing your commits today." --id 99')

