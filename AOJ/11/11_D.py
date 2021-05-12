class Dice():
    def __init__(self, sequence):
        self.sequence = sequence
    def move(self, code):
        return [self.sequence[int(idx)] for idx in str(code)]
    def roll(self, eye):
        for op in eye:
            if op == 'N': self.sequence = self.move(152304)
            elif op == 'E': self.sequence = self.move(310542)
            elif op == 'S': self.sequence = self.move(402351)
            elif op == 'W': self.sequence = self.move(215043)

class NewDice(Dice):
    def __init__(self, sequence):
        super().__init__(sequence)
        self.candidates = []
        for eye in ('', 'N', 'W', 'E', 'S', 'NN'):
            dice = Dice(self.sequence)
            dice.roll(eye)
            for _ in range(4):
                dice.roll('NES')
                self.candidates.append(dice.sequence)
    def __eq__(self, other):
        return min(self.candidates) == min(other.candidates)

prv = []
for _ in range(int(input())):
    tmp = min(NewDice(list(map(int, input().split()))).candidates)
    if tmp in prv:
        print('No')
        break
    prv.append(tmp)
else:
    print('Yes')
