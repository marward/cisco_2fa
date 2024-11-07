import pyotp
import os

# Run w32tm command to synchronize time
os.system('w32time /resync')

totp = pyotp.TOTP("")
otp = totp.now()
print("Current OTP:", totp.now())
print(f"{totp.verify(otp=otp)}")


import subprocess

def __auth_cisco_vpn__(username, password, auth, domain):

    # Assign cmd
    credentials = "printf '" + username + "\\n" + password + "\\n" + auth + "\\ny'"
    vpn_cmd = "/opt/cisco/anyconnect/bin/vpn -s connect '" + domain + "'"
    cmd = credentials + " | " + vpn_cmd

    # Command Execution
    print("Executing Command: \n" + cmd)
    subprocess.Popen(cmd,
                     shell=True,
                     executable="/bin/bash",
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE).communicate()

__auth_cisco_vpn__(username='',
                   password='',
                   auth=otp,
                   domain='')