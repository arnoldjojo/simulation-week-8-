#!/usr/bin/env python3

import socket
import math
import numpy as np
HOST = '0.0.0.0'  # Standard loopback interface address (localhost)
PORT = 8550       # Port to listen on (non-privileged ports are > 1023)
start_time=0
end_time  =20
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(10240)
            value_recieved=data.decode()          # recieve data from client 
            split_value=value_recieved.split("-")
            omega = split_value[0]
            theta_old  = split_value[1]
            delta_time = split_value[2]
            #print(f"omega {omega} theta {theta_old} time {delta_time} ")
            time = np.arange(start_time,end_time,float(delta_time))
            theta = [float(theta_old)*math.cos(float(omega) * t) for t in time]
            print(f"Theta value calculated {theta}")
            if not data:
                break
            theta_byte = str(theta).encode()
            conn.sendall(theta_byte)
