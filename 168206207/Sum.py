def sum(list):
	if list==[]:
		return 0
	else:
		return list[0]+sum(list[1:])
list=[4,16,65,33]
print(sum(list))
