import random
import time
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


def print_pause(message):
    print(message)
    time.sleep(2)


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            ur_choice = input("Rock, Paper, Scissors?")
            if ur_choice == "rock":
                return ur_choice
            elif ur_choice == "paper":
                return ur_choice
            elif ur_choice == "scissors":
                return ur_choice


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class ReflectPlayer(Player):
    def __init__(self):
        self.op_previous_move = random.choice(moves)

    def learn(self, my_move, their_move):
        self.op_previous_move = their_move

    def move(self):
        return self.op_previous_move


class CyclePlayer(Player):
    def __init__(self):
        self.my_previous_move = random.choice(moves)

    def learn(self, my_move, their_move):
        self.my_previous_move = my_move

    def move(self):
        if self.my_previous_move == "rock":
            return "paper"
        elif self.my_previous_move == "paper":
            return "scissors"
        else:
            return "rock"


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_points = 0
        self.p2_points = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print_pause(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2) is True:
            self.p1_points += 1
        elif beats(move2, move1) is True:
            self.p2_points += 1
        else:
            print_pause("!~~IT'S A TIE!~~!")
        print_pause("-----------------------------------------------------\n"
                    f"Score:Player1:{self.p1_points},Player2:{self.p2_points}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print_pause("Lets roll the dice and see how many "
                    "games you get to play!!")
        no_of_games = random.randint(1, 7)
        print_pause(f"You rolled {no_of_games}!, Let's Begin!")
        print_pause("Game start!")
        for round in range(no_of_games):
            print_pause(f"Round {round + 1}:")
            self.play_round()
        if self.p1_points > self.p2_points:
            print_pause("Player 1 WINS!!")
        elif self.p2_points > self.p1_points:
            print_pause("Player 2 WINS!!")
        else:
            print_pause("IT'S A TIE!!")
        print_pause("Game over!")


final = [RandomPlayer(), ReflectPlayer(), CyclePlayer()]


if __name__ == '__main__':
    game = Game(random.choice(final), HumanPlayer())
    game.play_game()
