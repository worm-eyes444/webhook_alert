#simple script to reamind me when my stuff has finished running
import sys
import requests
import subprocess
#TODOs
# - make this open a program (either pipe or write idk), send result
# - poll the tail of the stdout to editing a running message
# - if webhookurl not exists then ask user for it

# - different profiles!

with open(sys.argv[0][:-7] + "url.txt", "r+") as hookurl:
    hook = hookurl.read().strip()

#subprocess.run(sys.argv[1:])
working = ""
#out = subprocess.run(args=sys.argv[1:], capture_output=True).stdout.decode('utf-8')


process = subprocess.Popen(sys.argv[1:], stdout=subprocess.PIPE, text=True)
output_lines = []

for line in process.stdout:
    print(line, end='')  # Print to terminal
    output_lines.append(line)

process.wait()
out = ''.join(output_lines)



headers = {
        'Accept': 'application/json',
        'User-Agent': 'slimeWrld'
    }
data = {
    'content':out[-2000:]
}
r = requests.post(url=hook, headers=headers, data=data)
print(out)
print(r.status_code)

