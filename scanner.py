import socket
import threading
import sys
import time
from queue import Queue

# 1. Command Line Argument check karna (Agar IP nahi daala toh batao kaise chalana hai)
if len(sys.argv) != 2:
    print("Usage: python3 scanner.py <Target-IP>")
    print("Example: python3 scanner.py 127.0.0.1")
    sys.exit()

# sys.argv[1] wahi IP hai jo tu command line me daalega
target = sys.argv[1] 

print("=" * 50)
print("  Pranjal's Port Scanner (V4 - pro) ")
print("=" * 50)
print(f"Scanning ALL 65,535 ports on: {target}")
print("-" * 50)

queue = Queue()
open_ports = []

# 2. Stopwatch Start
start_time = time.time() 

def scan_port():
    while not queue.empty():
        port = queue.get()
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[+] BOOM! Port {port} is OPEN 🔓")
                open_ports.append(port)
            s.close()
        except:
            pass
        queue.task_done()

for port in range(1, 65536):
    queue.put(port)

thread_list = []
for t in range(100):
    thread = threading.Thread(target=scan_port)
    thread_list.append(thread)
    thread.start()

for thread in thread_list:
    thread.join()

# 3. Stopwatch Stop aur Total Time calculate karna
end_time = time.time()
total_time = round(end_time - start_time, 2) # Round to 2 decimal places

print("-" * 50)
print(f"Scan Completed! Total open ports found: {len(open_ports)}")
print(f"Total time taken: {total_time} seconds")
print("=" * 50)
