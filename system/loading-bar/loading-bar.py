from tqdm import tqdm
from time import sleep

text = ""
for char in tqdm(["a", "b", "c", "d", 'e', 'f', 'g', 'h', 'i', 'd'], 'char add => '):
    sleep(0.25)
    text = text + char
print(text, '\n')
for i in tqdm(range(99), 'sleeping => '):
    sleep(0.01)
