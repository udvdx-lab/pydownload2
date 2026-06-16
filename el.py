c=0

for x in range(2,1000001):
	for r in range(2,x):
		if x%r==0:
			break
	else:
		print('-----------')
		print(x)
		p=x


		for xx in range(2,1000001):
			for rr in range(2,xx):
				if xx%rr==0:
					break
			else:
				p=p-xx
				c=c+1
				if p<0:
					c=c-1
					break
				# elif p==1:
				# 	c-=1
				else:
					for rrr in range(2,p):
						if p%rrr==0:
							break
					else:
						# print('found',x)
						pass

		print('count',c)
		print('-----------')
	c=0
	
