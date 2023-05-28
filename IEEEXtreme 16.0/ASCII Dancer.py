class Dancer:

    def __init__(self):
        self.top = [' ', 'o', ' ']
        self.mid = ['/', '|', '\\']
        self.bot = ['/', ' ', '\\']

    def main(self, nmoves):

        for i in range(nmoves):
            move = input()
            self.action(move)
            if move[:3] != "say":
                self.dance()

    def action(self, move):

        if move == "left hand to head":
            self.left_hand_to_head()

        elif move == "left hand to hip":
            self.left_hand_to_hip()

        elif move == "left hand to start":
            self.left_hand_to_start()

        elif move == "left leg in":
            self.left_leg_in()

        elif move == "left leg out":
            self.left_leg_out()

        elif move == "right hand to head":
            self.right_hand_to_head()

        elif move == "right hand to hip":
            self.right_hand_to_hip()

        elif move == "right hand to start":
            self.right_hand_to_start()

        elif move == "right leg in":
            self.right_leg_in()

        elif move == "right leg out":
            self.right_leg_out()

        elif move == "turn":
            self.turn()

        elif move[:3] == "say":
            self.say(move)

    def say(self, words):
        print(words[4:])

    def dance(self):
        head = ''
        for side in self.top:
            head += side
        print(head)

        body = ''
        for side in self.mid:
            body += side
        print(body)

        legs = ''
        for side in self.bot:
            legs += side
        print(legs)

    def left_hand_to_head(self):
        self.top[2] = ')'
        self.mid[2] = ' '

    def right_hand_to_head(self):
        self.top[0] = '('
        self.mid[0] = ' '

    def left_hand_to_hip(self):
        self.top[2] = ' '
        self.mid[2] = '>'

    def right_hand_to_hip(self):
        self.top[0] = ' '
        self.mid[0] = '<'

    def left_hand_to_start(self):
        self.top[2] = ' '
        self.mid[2] = '\\'

    def right_hand_to_start(self):
        self.top[0] = ' '
        self.mid[0] = '/'

    def left_leg_in(self):
        self.bot[2] = '>'
        self.bot[0] = '/'

    def right_leg_in(self):
        self.bot[0] = '<'
        self.bot[2] = '\\'

    def left_leg_out(self):
        self.bot[2] = '\\'

    def right_leg_out(self):
        self.bot[0] = '/'

    def turn(self):

        temp_side = [self.top[0], self.mid[0], self.bot[0]]

        self.top[0] = self.top[2]
        self.mid[0] = self.mid[2]
        self.bot[0] = self.bot[2]

        self._fix0()

        self.top[2] = temp_side[0]
        self.mid[2] = temp_side[1]
        self.bot[2] = temp_side[2]

        self._fix1()

    def _fix0(self):

        if self.top[0] == ')':
            self.top[0] = '('

        if self.mid[0] == '>':
            self.mid[0] = '<'
        if self.mid[0] == '\\':
            self.mid[0] = '/'

        if self.bot[0] == '\\':
            self.bot[0] = '/'
        if self.bot[0] == '>':
            self.bot[0] = '<'

    def _fix1(self):

        if self.top[2] == '(':
            self.top[2] = ')'

        if self.mid[2] == '<':
            self.mid[2] = '>'
        if self.mid[2] == '/':
            self.mid[2] = '\\'

        if self.bot[2] == '/':
            self.bot[2] = '\\'
        if self.bot[2] == '<':
            self.bot[2] = '>'


t = int(input())
for i in range(t):
    d = int(input())
    dancer = Dancer()
    dancer.main(d)
