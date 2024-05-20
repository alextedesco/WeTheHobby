#!/usr/bin/env python3

import requests	
import os
import time
from win10toast import ToastNotifier
url = "http://192.168.201.242:631/printing"  

toast = ToastNotifier()

while True:	
    os.system ("ping -n 1 192.168.201.242")
    print ("success")
    response = requests.get(url)
    if response.status_code == 200:
        toast.show_toast(
            "Rollo Printer",
            "SUCCESS",
            duration = 20,
            threaded = True,
        )
    else:
        print ("Shit is broken AHHHH!")
        toast.show_toast(
            "Rollo Printer",
            "FAIL!!!",
            duration = 20,
            threaded = True,
        )
    time.sleep (300)