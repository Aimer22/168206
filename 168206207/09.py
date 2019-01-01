def findThief(thief):
	if thief!='A':
		print('A说的是真话')
	else:
		print('A说的是假话')
	if thief=='D':
		print('B说的是真话')
	else:
		print('B说的是假话')
	if thief=='C':
		print('C说的是真话')
	else:
		print('C说的是假话')
	if thief!='D':
		print('D说的是真话')
	else:
		print('D说的是假话')
	trueWord=(thief!='A')+(thief=='D')+(thief=='C')+(thief!='D')#计算出真话的数量。
	print('总共有',trueWord,'个人说了真话')
	if trueWord==2:#当只有一个人说了真话，刚好符合题意，对应找出小偷。
		print('假设成功，',thief,'就是小偷！')
		flag=1
	else:
		print('假设失败',thief,'没有偷钻石')
		return 
	if (flag==0):
		print('很遗憾，没有找到小偷')
		
if __name__ == '__main__':
	flag=0
	thief=input('请假设谁是小偷(输入字母A--D)：')
	findThief(thief)		
		