import subprocess
import shlex


git_command = "git pull"
subprocess.run(shlex.split(git_command))
print()