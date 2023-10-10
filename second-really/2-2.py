import time
def dex(n):
    count = 2**n
    print(count)
    return
start_time = time.time()
n = 100
dex(n)
end_time = time.time()
print(".1%f" % (end_time-start_time))