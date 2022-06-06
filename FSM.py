# class FSM:
#     def __init__(self):
#         self.handlers = {}
#
#     def add_state(self, name, handler):
#         self.handlers[name] = handler
#
#     def run(self, startingState, cargo):
#         handler = self.handlers[startingState]
#         while True:
#             (newState, cargo) = handler(cargo)
#             if newState == "END":
#                 print("END reached")
#                 break
#             handler = self.handlers[newState]


# fsm = FSM()
# fsm.add_state("START", state_start_handler)
# fsm.add_state("RED", )