import shelve
import random
los_self = shelve.open('st')

def t3_ai(role,move):
	pos = None
	npos = None
	if role == 1:
		pos = los_self['pos1']
		npos = los_self['pos2']
	else:
		pos = los_self['pos2']
		npos = los_self['pos1']

	nxt_lose_move = []
	for s in pos:
		if len(move)==len(s)-2 and move == s[:len(move)]:
			nxt_lose_move.append(s[len(move)])
	nxt_lose_move = list(set(nxt_lose_move))

	nxt_win_move = []
	for s in npos:
		if len(move)==len(s)-1 and move == s[:len(move)]:
			nxt_win_move.append(s[len(move)])
	nxt_win_move = list(set(nxt_win_move))

	nxt_move = []
	for i in range(9):
		if (not str(i) in nxt_lose_move) and (not str(i) in move):
			nxt_move.append(i)
	if len(nxt_win_move)>0:
		return int(random.choice(nxt_win_move))
	elif len(nxt_move)>0: 
		return random.choice(nxt_move)
	elif len(move)<9:
		return int(random.choice(nxt_lose_move))