string = [11,11,13,7,0,15,5,5,4,4,1,1,7,1,15,11]

memory = []
cnt = 0
while string not in memory:
	memory += [string.copy()]
	pos = string.index(max(string))
	
	amount = string[pos]
	string[pos] = 0
	i = 1
	while amount>0:
		string[(pos+i)%len(string)] += 1
		amount -= 1
		i +=1
	cnt+=1

print(cnt)

memory = []
cnt = 0
while string not in memory:
	memory += [string.copy()]
	pos = string.index(max(string))
	
	amount = string[pos]
	string[pos] = 0
	i = 1
	while amount>0:
		string[(pos+i)%len(string)] += 1
		amount -= 1
		i +=1
	cnt+=1
print(cnt)