import os
path = '/Users/Max/Music/BOTW OST'
files = os.listdir(path)
i = 1

for file in files:
	if file.endswith('wav'):
		os.rename(os.path.join(path, file), os.path.join(path, file.replace('Zelda - Breath of the Wild OST - ', "") +'.wav'))
		i = i+1