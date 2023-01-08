from collections import deque
import time
start = time.time()
deque_list = deque()
# Stack
for i in range(10000):
    for i in range(10000):
        deque_list.append(i)
        deque_list.pop()

print(time.time()- start, 'Seconds')