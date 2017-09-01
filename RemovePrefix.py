import os
path = '/Users/Max/Music/'
files = os.listdir(path)
i = 1

for file in files:
	if file.endswith('wav'):
		os.rename(os.path.join(path, file), os.path.join(path, file.replace('Prefix of file that you would like removed', "") +'.wav'))
		i = i+1