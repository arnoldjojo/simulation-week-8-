
import socket
import math  
from matplotlib import pyplot as plt
import numpy as np

HOST       = '0.0.0.0'  # The server's hostname or IP address
PORT       = 8550       # The port used by the server

g          = 9.81        # acceleration due to gravity
l          = 1          # pendulum length 
theta_old  = 0.2
delta_time = 0.1
start_time=0.0
end_time=20.0
time = np.arange(start_time, end_time, delta_time)
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # creating socket connection 
    s.connect((HOST, PORT))
    
    omega               = math.sqrt(g/l)
    omega_in_bytes      = str.encode(str(omega))    # calculate omega 
    theta_old_in_bytes  = str.encode(str(theta_old))     
    delta_time_in_bytes = str.encode(str(delta_time))    
    s.sendall(omega_in_bytes+b'-'+theta_old_in_bytes+b'-'+delta_time_in_bytes) # request
    data = s.recv(10240)
    print(omega)
print('Received', repr(data))

plt.plot(time, data)
plt.title('Pendulum Motion ')
plt.xlabel('time (s)')
plt.ylabel('angle (rad)')
plt.grid(True)
plt.legend(['nonlinear', 'linear'], loc='lower right')
plt.show()
