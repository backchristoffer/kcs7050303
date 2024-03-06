import os
import time

def check_logs(log_file):
    error_messages = []
    with open(log_file, 'r') as f:
        for line in f:
            if 'ERROR: could not find ovs-if-br-ex conn file after cloning' in line:
                error_messages.append(line.strip())
    return error_messages

def fix_issue():
    os.system("mv /etc/NetworkManager/system-connections/ovs-if-br-ex* /root")
    os.system("systemctl reboot") 

def main():
    log_file = '/var/log/ovs-configuration.log'
    while True:
        errors = check_logs(log_file)
        if errors:
            print("Errors found in ovs-configuration.service logs:")
            for error in errors:
                print(error)
            print("Attempting to fix the issue...")
            fix_issue()
            print("Issue fixed. Configuration files moved to /root. Node rebooting...")
            break 
        else:
            print("No errors found in ovs-configuration.service logs.")
        # Wait for a specified interval before checking the logs again
        time.sleep(60)  

if __name__ == "__main__":
    main()