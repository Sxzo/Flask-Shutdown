from flask import Flask
import os
import requests
import time
import psutil
import signal

# (Port #s)
ports = [
    5001, 
    5002, 
    5003,  
    5004, 
    5005, 
    5006,
    5007,
    5008,
    5009,
    5010,
    5011,
    5012,
    5013,
    5050
]

shutdown_ct = 0

# Safety Block - Delete if not needed
t_input = input(f"Enter SHUTDOWN to close all active flask servers:")
while(t_input != "SHUTDOWN"):
    t_input = input(f"Enter SHUTDOWN to close all active flask servers:")


for proc in psutil.process_iter():
    try:
        for conn in proc.connections():
            if conn.status == psutil.CONN_LISTEN and conn.laddr.port in ports:
                os.kill(proc.pid, signal.SIGTERM)
                print(f"Process '{proc.name()}' with PID: {proc.pid} has been killed.")
                shutdown_ct += 1
    except (psutil.AccessDenied, psutil.NoSuchProcess):
        pass

print(f"Shutdown {shutdown_ct} server(s).")
