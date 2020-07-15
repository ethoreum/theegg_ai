class Pokemon():

	def __init__(self, attack, hp):
		self.attack = attack
		self.hp = hp


pikachu = Pokemon(55, 100)
jygglypuff = Pokemon(45, 100)
turn = 1

while pikachu.hp > 0 and jygglypuff.hp > 0:
	if turn == 1:
		jygglypuff.hp -= pikachu.attack
		turn = 0
	else:
		pikachu.hp -= jygglypuff.attack
		turn = 1

if jygglypuff.hp <= 0:
	print("Pikachu Wins!")
else:
	print("Jygglypuff Wins!")


