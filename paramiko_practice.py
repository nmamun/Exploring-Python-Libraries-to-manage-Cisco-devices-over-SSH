#!/usr/bin/env python

# ==============================================================
__author__ = "Nurul Mamun"
__date__ = " 10 July, 2020"
__version__ = "1.0"
__description__ = "Paramiko Exercise - basics"
# ==============================================================

# ========== Imports ===========================================
import paramiko
import time
# ==============================================================

# ========= Functions ==========================================


# ==============================================================

# ========== Main Function =====================================
def main():
    channel = paramiko.SSHClient()
    channel.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    channel.connect(hostname="R1", username='cisco', password='cisco', look_for_keys=False, allow_agent=False)

    shell = channel.invoke_shell()

    shell.send("enable\n")
    shell.send("cisco\n")
    shell.send("terminal length 0\n")
    shell.send("show ip int b\n")
    shell.send("show arp \n")
    time.sleep(2)
    print (shell.recv(65535).decode("utf-8"))
    
    channel.close()



# ==============================================================


if __name__ == "__main__":
    main()
