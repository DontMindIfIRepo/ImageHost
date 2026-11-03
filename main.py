import random
import time

for i in range(100):
    
    current_num = random.randint(1, 100)
    
    print(f"\r{current_num:<3}", end="", flush=True)
    time.sleep(0.025)

