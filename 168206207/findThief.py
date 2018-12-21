flag=0

for thief in range(ord('A'),ord('D')+1):#挨个假设谁是小偷，当知道谁是小偷的前提下，就可以退出他们说的是真是假。
	trueWord=chr(thief)
	if thief!=ord('A'):
		print('A说的是真话')
	else:
		print('A说的是假话')
	if thief==ord('D'):
		print('B说的是真话')
	else:
		print('B说的是假话')
	if thief==ord('B'):
		print('C说的是真话')
	else:
		print('C说的是假话')
	if thief!=ord('D'):
		print('D说的是真话')
	else:
		print('D说的是假话')
	trueWord=(thief!=ord('A'))+(thief==ord('D'))+(thief==ord('B'))+(thief!=ord('D'))#计算出真话的数量。
	print('总共有',trueWord,'个人说了真话')
	if trueWord==1:#当只有一个人说了真话，刚好符合题意，对应找出小偷。
		print('假设成功，',chr(thief),'就是小偷！')
		flag=1
	else:
		print('假设失败',chr(thief),'没有偷钻石')
if (flag==0):
	print('很遗憾，没有找到小偷')
		