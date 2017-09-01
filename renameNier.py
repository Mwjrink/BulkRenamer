import os
path = '/Users/Max/Music/'
files = os.listdir(path)
i = 1


# with open("list.txt") as tracklist:
# 	for file in files:
# 		if file.endswith('mp3'):
# 			os.rename(os.path.join(path, file), os.path.join(path, file.replace(file[4:], tracklist.readline().replace("\n","").strip()[2:]) +'.mp3'))
# 			i = i+1



with open("list.txt") as tracklist:
	for file in files:
		if file.endswith('mp3'):
			os.rename(os.path.join(path, file), os.path.join(path, file.replace("â€“", "-") +'.mp3'))
			i = i+1