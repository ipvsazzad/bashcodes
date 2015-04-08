import subprocess
commitMessage ="git commit -m \"" + raw_input("your commit message \n") + "\""

commands =[
    "git add .",
    commitMessage,
    "git push"
]

for cmd in commands:
    subprocess.call(cmd, shell=True)
