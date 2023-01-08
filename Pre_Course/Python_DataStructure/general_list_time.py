import time

start = time.time()
just_list = []

for i in range(10000):
    for i in range(10000):
        just_list.append(i)
        just_list.pop()

print(time.time() - start, 'Second')