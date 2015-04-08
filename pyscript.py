import subprocess
cmd1 = "echo hello world"
cmd2 = "ls -al"
cmds = [cmd1, cmd2]

for cmd in cmds:
	subprocess.call(cmd, shell=True)

