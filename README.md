## cisco_2fa
# Automate Cisco Anyconnect VPN connection

## installation 
```
pip install --upgrade pip

pip install pyotp
```

## usage 

# replace **login**, **password** and **domain** with your values
```
alias cisco='python3 /Users/user/otp_util/get_otp.py'
alias disc='/opt/cisco/anyconnect/bin/vpn disconnect'
alias vpn_state='/opt/cisco/anyconnect/bin/vpn -s'
source ~/.zsh (bashrc)
```
