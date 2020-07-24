class Pokemon():
    def __init__(self, attack, hp):
        self.attack = attack
        self.hp = hp

def main():
    pikachu = Pokemon(55, 100)
    jigglypuff = Pokemon(45, 100)
    turn = 1

    while pikachu.hp > 0 and jigglypuff.hp > 0:
        if turn == 1:
            jigglypuff.hp -= pikachu.attack
            turn = 0
        else:
            pikachu.hp -= jigglypuff.attack
            turn = 1

    if jigglypuff.hp <= 0:
        print("Pikachu Wins!")
    else:
        print("Jigglypuff Wins!")

if __name__ == "__main__":
    main()
