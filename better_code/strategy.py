import string
import random
from typing import List, Callable
from abc import ABC, abstractmethod


def generate_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


def fifo_ordering(l: List[SupportTicket]) -> List[SupportTicket]:
    return l.copy()


def filo_ordering(l: List[SupportTicket]) -> List[SupportTicket]:
    return l[::-1]


def random_ordering(l: List[SupportTicket]) -> List[SupportTicket]:
    c = l[:]
    random.shuffle(c)
    return c

def black_hole_ordering(l: List[SupportTicket]) -> List[SupportTicket]:
    return []


class CustomerSupport:

    def __init__(self, processing_strategy_fn: Callable[[List[SupportTicket]], List[SupportTicket]]):
        self.tickets = []
        self.processing_strategy = processing_strategy_fn

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self):
        ticket_list = self.processing_strategy(self.tickets)

        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done!")
            return


        for ticket in ticket_list:
            self.process_ticket(ticket)

    @staticmethod
    def process_ticket(ticket: SupportTicket):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")


# create the application
app = CustomerSupport(random_ordering)

# register a few tickets
app.create_ticket("John Smith", "My computer makes strange sounds!")
app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

# process the tickets
app.process_tickets()
