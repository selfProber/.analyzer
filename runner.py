import subprocess
import shlex


git_command = "git -C /.analyzer pull"
subprocess.run(shlex.split(git_command))