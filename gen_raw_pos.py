import shelve
los_self = shelve.open('st')



all_move = []

bm = [0]*9
cm = ''
def make_move(bm,cm):
	if len(cm)==9:
		all_move.append(cm)
		return
	for i in range(9):
		if bm[i]==0:
			cm += str(i)
			bm[i]=1
			make_move(bm,cm)
			bm[i]=0
			cm = cm[:-1]

make_move(bm,cm)


def ck_mv(x):
	m0 = 1
	for i in x:
		m0 *=i
	y = {
	x[0]*x[1]*x[2],
	x[3]*x[4]*x[5],
	x[6]*x[7]*x[8],
	x[0]*x[3]*x[6],
	x[1]*x[4]*x[7],
	x[2]*x[5]*x[8],
	x[0]*x[4]*x[8],
	x[2]*x[4]*x[6],
	}
	if 1 in y:
		return 1
	elif 8 in y:
		return 2
	elif m0>0:
		return -1
	else:
		return 0

pos1 = []
pos2 = []

for move in all_move:
	x = [0]*9
	for i in range(9):
		if(i%2==0):
			x[int(move[i])]=1
		else:
			x[int(move[i])]=2
		tmp = ck_mv(x)
		if tmp==1:
			pos2.append(move[:i+1])
			break
		elif tmp==2:
			pos1.append(move[:i+1])
			break
		elif tmp==-1:
			break

los_self['pos1'] = pos1
los_self['pos2'] = pos2
los_self.close()