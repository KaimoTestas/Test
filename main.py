import os
from random import randint

# Set repo-specific Git identity
os.system('git config user.name "Kaimo Testas"')
os.system('git config user.email "kaimetis.lt@gmail.com"')
os.system('git config commit.gpgsign false')  # disable GPG signing

# Generate 1 year of commits
for i in range(1, 365):
    for j in range(0, randint(1, 10)):
        d = str(i) + ' days ago'
        with open('file.txt', 'a') as file:
            file.write(d + "\n")
        os.system(f'git add .')
        os.system(f'git commit --date="{d}" -m "Contribution: {d}"')