import dataclasses
from enum import Enum


@dataclasses.dataclass
class Ob:
    s: str
    i: int


# class State:
#     def __init__(self, ob: Ob, func):
#         self.ob = ob
#         self.func = func
#
#     def next(self):
#         return self.func(self.ob)

# class StateMachine:
#     def __init__(self, initial_state: State):
#         self.current_state = initial_state
#         self.current_state.run()


# start
# sign1
# dec
# pre
# post
# e
# e_sign
# e_int
# error

class State(Enum):
    START = 1
    SIGN = 2
    START_DEC = 3
    MID_DEC = 10
    PRE = 4
    POST = 5
    E = 6
    E_SIGN = 7
    E_INT = 8
    ERROR = 9

def is_number(s):


    valid_end_states = {State.PRE, State.POST, State.E_INT, State.MID_DEC}

    i = 0
    current_state: State = State.START

    while i < len(s):
        c = s[i]

        if current_state == State.ERROR:
            return False

        if current_state == State.START:
            if c == "+" or c == "-":
                current_state = State.SIGN
            elif c.isnumeric():
                current_state = State.PRE
            elif c == ".":
                current_state = State.START_DEC
            else:
                current_state = State.ERROR

        elif current_state == State.SIGN:
            if c.isnumeric():
                current_state = State.PRE
            elif c == ".":
                current_state = State.START_DEC
            else:
                current_state = State.ERROR

        elif current_state == State.PRE:
            if c.isnumeric():
                current_state = State.PRE
            elif c == '.':
                current_state = State.MID_DEC
            elif c == "E" or c == "e":
                current_state = State.E
            else:
                current_state = State.ERROR

        elif current_state == State.MID_DEC:
            if c.isnumeric():
                current_state = State.POST
            elif c == "E" or c == "e":
                current_state = State.E
            else:
                current_state = State.ERROR

        elif current_state == State.START_DEC:
            if c.isnumeric():
                current_state = State.POST
            else:
                current_state = State.ERROR
        elif current_state == State.POST:
            if c.isnumeric():
                current_state = State.POST
            elif c == "E" or c == "e":
                current_state = State.E
            else:
                current_state = State.ERROR

        elif current_state == State.E:
            if c.isnumeric():
                current_state = State.E_INT
            elif c == "+" or c == "-":
                current_state = State.E_SIGN
            else:
                current_state = State.ERROR

        elif current_state == State.E_SIGN:
            if c.isnumeric():
                current_state = State.E_INT
            else:
                current_state = State.ERROR

        elif current_state == State.E_INT:
            if c.isnumeric():
                current_state = State.E_INT
            else:
                current_state = State.ERROR

        i += 1

    if current_state in valid_end_states:
        return True

    return False



print(is_number("46.e3"))




















