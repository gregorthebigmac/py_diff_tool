import os

for root_dir, dirs, filenames in os.walk('.'):
	# add path to all subdirectories
	for filenames in dirs:
		filenames.join(dirs)
		print(filenames)