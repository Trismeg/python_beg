import os
import subprocess

# Define a function for running commands and capturing stdout line by line
# (Modified from Vartec's solution because it wasn't printing all lines)
def runProcess(exe):    
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')

# Get all filenames in working directory
for filename in os.listdir('./'):
    # This command will be run on each file
    cmd = 'nm ' + filename

    # Run the command and capture the output line by line.
    for line in runProcess(cmd.split()):
        # Eliminate leading and trailing whitespace
        line.strip()
        # Split the output 
        output = line.split()

        # Filter the output and print relevant lines
        if len(output) > 2:
            if ((output[2] == 'set_program_name')):
                print filename
                print line
