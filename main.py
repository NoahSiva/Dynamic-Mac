import random
import subprocess
import sys
import time


class MacChanging():
    def __init__(self):
        print("Make sure you are in the root mode....")
        self.count = int(input("Enter a time limit (in secs) to change your mac address[*](60 to 1000)"))
        self.interface = input("Enter your interface within double quotes(""):")
        print("For stop changing your mac address press 'ctrl+C'")
        self.start_changing()

    def create_new_mac(self):
        mac = random.randint(10, 99)
        return str(mac)

    def changing_mac(self):
        self.newMac = "00"
        for i in range(5):
            mac = ":" + str(self.create_new_mac())
            self.newMac += mac
            continue
        subprocess.call(["ifconfig", self.interface, "down"])
        subprocess.call(["ifconfig", self.interface, "hw", "ether", self.newMac])
        subprocess.call(["ifconfig", self.interface, "up"])
        print("Mac address is successfully changed to [@]", self.newMac)

    def start_changing(self):
        while True:
            try:
                self.changing_mac()
                time.sleep(self.count)
            except KeyboardInterrupt:
                sys.exit()


change = MacChanging()
