import tkinter as tk
import gm_ai

#main class
class Board(tk.Tk):
	def __init__(self):
		super().__init__()
		# dict of 9 buttons(cells)
		self.title('Tic tac toe')
		self.cell = {}
		#current move, it will store moved sell number according to move made by players
		self.move = ''
		#cell width
		self.c_x = 10
		#cell height
		self.c_y = 5
		#cell background
		self.bg_color = '#444444'
		#cell font color
		self.fg_color = '#ffffff'
		#color of cells after pressing
		self.pressed_bg = '#393939'
		#making buttons
		for i in range(3):
			for j in range(3):
				self.mk_cell(i,j)
		#tracking whose trurn is now
		self.turn = True
		#tracking game progress with label at the top
		self.gm_lbl(0)
		#drawing reset button
		self.reset_btn()
		#game ai
		#tells game is going on or not
		self.gm_state = True

		self.ai_role = 2
		self.if_ai(self.ai_role) ##################
	#making cell/buttons
	def mk_cell(self,x,y):
		num = y*3+x
		self.cell[num] = tk.Button(self,width=self.c_x,height=self.c_y,text=' ',bg = self.bg_color,fg = self.fg_color)
		self.cell[num].grid(column=y,row=x+1)
		self.cell[num]['command'] = self.ch_sign(num)

	#it will return callback function
	def ch_sign(self,num):
		def f():
			btn = self.cell[num]
			st = self.ck_state()
			if st == 0 and btn['text'] == ' ' and self.turn == True:
				btn['bg'] = self.pressed_bg
				btn['text'] = 'X'
				self.turn = not self.turn
				self.move += str(num)
			elif st == 0 and btn['text'] == ' ' and self.turn == False:
				btn['bg'] = self.pressed_bg
				btn['text'] = 'O'
				self.turn = not self.turn
				self.move += str(num)
			st = self.ck_state()
			self.gm_lbl(st)
			if len(self.move)<9:
				self.if_ai(self.ai_role) ######################
		return f
	
	#makes or changes game situation label
	def gm_lbl(self,st):
		red = '#440000'
		green = '#004400'
		blue = '#000044'
		black = '#000000'
		if not hasattr(Board, 'lbl'):
			self.lbl = tk.Label(self,text = ' ',bg=green,fg=self.fg_color)
			self.lbl.grid(row= 0, column= 0, columnspan=3,sticky="ew")
		if st == 0 and self.turn:
			self.lbl['text'] = "Player 1's turn"
			self.lbl['bg'] = green
		elif st ==0:
			self.lbl['text'] = "Player 2's turn"
			self.lbl['bg'] = red
		elif st ==1:
			self.lbl['text'] = "Player 1 won"
			self.lbl['bg'] = blue
		elif st ==2:
			self.lbl['text'] = "Player 2 won"
			self.lbl['bg'] = blue
		else:
			self.lbl['text'] = "Match draw"
			self.lbl['bg'] = black

	#checks game current state, 0 means not ended, 1 player 1 won, 2 player 2 won, -1 draw.
	def ck_state(self):
		x = self.get_state()
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
		self.gm_state = False
		if 1 in y:
			return 1
		elif 8 in y:
			return 2
		elif m0>0:
			return -1
		else:
			self.gm_state = True
			return 0

	#makes the list which represents game state with 0,1,2. 0= not moved, 1= X, 2=O
	def get_state(self):
		x = []
		for i in self.cell:
			x.append(self.cell[i]['text'])
		for i in range(9):
			if x[i] == ' ':
				x[i] = 0
			elif x[i] == 'X':
				x[i]=1
			else:
				x[i]=2
		return x

	# callback function to resest the board
	def reset(self):
		for i in self.cell:
			self.cell[i]['text']= ' '
			self.cell[i]['bg']= self.bg_color
		self.turn = True
		self.move = ''
		del self.lbl
		self.gm_lbl(0)
		self.gm_state = True

	# adds button to the board to reset
	def reset_btn(self):
		tk.Button(self,width=32,padx=4,text='Reset',command=self.reset,bg = self.pressed_bg,fg=self.fg_color).grid(row=5,column=0,columnspan=3)

	# tell if ai should be used or not
	def if_ai(self,role):
		if role==1 and self.gm_state:
			if self.turn:
				self.ch_sign(gm_ai.t3_ai(role,self.move))()
		if role==2 and self.gm_state:
			if not self.turn:
				self.ch_sign(gm_ai.t3_ai(role,self.move))()

if __name__ == '__main__':
	root = Board()
	root.mainloop()