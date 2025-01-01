import subprocess
from datetime import datetime, timedelta
from random import randint

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

# Git identity config (must match your GitHub user settings)
run('git config user.name "Kaimo Testas"')
run('git config user.email "kaimetis.lt@gmail.com"')
run('git config commit.gpgsign false')

# Range: Jan 1, 2025 to today
start_date = datetime(2025, 1, 1)
end_date = datetime.now()
file_name = "contributions_2025.txt"

current_date = start_date

while current_date.date() <= end_date.date():
    commits_today = randint(1, 5)  # Natural-looking range
    for _ in range(commits_today):
        time_hour = randint(8, 18)  # Between 8:00–18:59
        time_minute = randint(0, 59)
        commit_time = current_date.replace(hour=time_hour, minute=time_minute, second=0)
        date_str = commit_time.strftime('%Y-%m-%dT%H:%M:%S')

        with open(file_name, 'a') as f:
            f.write(f"Commit on {date_str}\n")

        run('git add .')
        run(f'git commit --date="{date_str}" -m "Contribution: {date_str}"')

    current_date += timedelta(days=1)
