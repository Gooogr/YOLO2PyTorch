def parse_cfg(file_path):
	"""
	Takes a configuration file

	Returns a list of blocks. Each blocks describes a block in the neural
	network to be built. Block is represented as a dictionary in the list

	"""
	# Split cfg files to the lines
	cfg_file = open(file_path, 'r')
	lines = cfg_file.read().splitlines()
	lines = [x.rstrip().lstrip() for x in lines if (x != '') and ('#' not in x)]
	blocks = []
	
	for line in lines:
		if line[0] == '[':                             # [ symbols means new block announcement
			block = {}	
			block['type'] = line[1:-1]
			blocks.append(block)
		else:
			key, value = line.split('=')
			block[key.rstrip()] = value.lstrip()       # rsplit/lsplit in case user type ' = ' instead of '='	    
	return blocks
			
		
			
FILE_PATH = './cfg/yolov3.cfg'
result = parse_cfg(FILE_PATH)
# ~ print(result)

for item in result:
	print(item)
	print()
