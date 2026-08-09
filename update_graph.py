import os
import random
from datetime import datetime
import time

log_file = "activity_log.txt"

# Upgraded range: Pick a random number of commits between 10 and 20
num_commits = random.randint(10, 20)

for i in range(num_commits):
    # Append timestamp line
    with open(log_file, "a") as f:
        f.write(f"Commit {i+1}/{num_commits} on {datetime.now()}\n")
    
    # Execute Git commands
    os.system("git add .")
    os.system(f'git commit -m "Automated update component {i+1}"')
    
    # Fast pause to quickly process large batches
    time.sleep(0.2)

# Push all 10 to 20 commits to GitHub at once
exit_status = os.system("git push origin main")

# Trigger native notification
if exit_status == 0:
    os.system(f'termux-notification --title "GitHub Bot Success" --content "Pushed a heavy batch of {num_commits} commits for a deep green look!" --id 99')
else:
    os.system('termux-notification --title "GitHub Bot Failed" --content "Error pushing heavy batch today." --id 99')

