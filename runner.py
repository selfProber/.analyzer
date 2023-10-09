import subprocess
import shlex


git_command = "git -C /.analyzer pull"
print('Fetching newest updates...')
subprocess.run(shlex.split(git_command))