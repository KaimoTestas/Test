import subprocess
from datetime import datetime, timedelta
from random import randint

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

# Git identity
run('git config user.name "Kaimo Testas"')
run('git config user.email "kaimetis.lt@gmail.com"')
run('git config commit.gpgsign false')

# Settings
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
file_name = "contributions.txt"

current_date = start_date

while current_date <= end_date:
    commits_today = randint(1, 5)  # fewer commits/day = more natural
    for _ in range(commits_today):
        timestamp = current_date.replace(hour=12, minute=randint(0, 59))  # randomize time a bit
        date_str = timestamp.strftime('%Y-%m-%dT%H:%M:%S')

        with open(file_name, 'a') as f:
            f.write(f"Commit on {date_str}\n")

        run('git add .')
        run(f'git commit --date="{date_str}" -m "Contribution: {date_str}"')
    
    current_date += timedelta(days=1)
