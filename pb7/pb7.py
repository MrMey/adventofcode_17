with open('pb7 - copie.txt','r') as f:
	dic_memory= {}
	dic_child = {}
	bottom = {}
	dic= {}
	for line in f:
		dic_memory[line.split(' ')[0]] = int(line.split(' ')[1].rstrip(' ').rstrip('\n').rstrip(')').lstrip(' ').lstrip('('))
		if line.count('>') >0:
			line = line.split('->')
			dic[line[0].split(' ')[0]] = []
			for child in line[1].split(' '):
				if child != '':
					dic_child[child.rstrip('\n').rstrip(',')] = line[0].split(' ')[0]
					dic[line[0].split(' ')[0]].append(child.rstrip('\n').rstrip(','))

result = list(dic.keys())
for key in dic.keys():
	for parent in dic[key]:
		if parent in result:
			result.remove(parent)

print(result)
tower = dic[result[0]]
tower = dic[tower[2]]
tower = dic[tower[4]]

print(tower)

def down(elem):
	if elem not in dic:
		return dic_memory[elem]
	else:
		return sum([down(el) for el in dic[elem]])+dic_memory[elem]

for tow in tower:
	print(down(tow))
	print(dic_memory[tow])