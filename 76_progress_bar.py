
from tqdm import tqdm
import time

for i in tqdm(range(100000), desc='progress'):
    pass
    time.sleep(0.001)

