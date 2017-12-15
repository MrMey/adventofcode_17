

# problem 1
def steps_1():
	with open('D:\\Shared_repository\\adventofcode_17\\pb5\\pb5.txt','r') as f:
		string = []
		for line in f:
			string.append(int(line))
		step = 0
		pos = 0
		while not(pos<0 or pos>=len(string)):
			last_pos = pos
			pos = pos+string[pos]
			if string[last_pos] >= 3:
				string[last_pos] -= 1
			else:
				string[last_pos] += 1
			
			step +=1

	print(step)


# problem 2
test = [0
,3
,0
,1
,-3]
with open('D:\\Shared_repository\\adventofcode_17\\pb5\\pb5.txt','r') as f:
	string = []
	for line in f:
		string.append(int(line))

	step = 0
	pos = 0
	while not(pos<0 or pos>=len(string)):
		last_pos = pos
		pos = pos+string[pos]
		if string[last_pos] >= 3:
			string[last_pos] -= 1
		else:
			string[last_pos] += 1
		
		step +=1

		


print(step)


