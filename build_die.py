import random
class Die:
	'''die whith one of its faces loaded'''
	def __init__(self,face,n):
		'''constructs a die with one of its faces loaded'''
		self.die=[1,2,3,4,5,6]
		self.face=face
		self.n=n
		for i in range(self.n-1):
			self.die.append(self.face)
		#to make it a fair dice just give any face a weight of 0
	def roll(self):
		return random.choice(self.die)

class Dice_Pair:
	def __init__(self,die1,die2):
		self.die1=die1
		self.die2=die2

	def roll(self):
		return (self.die1.roll()+self.die2.roll())
  
# d1=Die(2,10)
# d2=Die(4,20)
# pair= Dice_Pair(d1,d2)
# print(pair.roll())
