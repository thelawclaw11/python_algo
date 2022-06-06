import datetime
import math


class Car:
    def __init__(self, plate_number):
        self.plate_number = plate_number

class Driver:
    def __init__(self, name, credit_card_number, car):
        self.name = name
        self.credit_card_number = credit_card_number
        self.car = car

class Payment:
    def __init__(self, amount, credit_card_number, driver_name):
        self.amount = amount
        self.credit_card_number = credit_card_number
        self.driver_name = driver_name

class Receipt:
    def __init__(self, amount, driver_name):
        self.amount = amount
        self.driver_name = driver_name


class PaymentService:
    def pay(self, payment: Payment):
        # do payment thing
        return Receipt(payment.amount, payment.driver_name)

class Ticket:
    def __init__(self, start_time, driver_name, plate_number):
        self.start_time = start_time
        self.driver_name = driver_name
        self.plate_number = plate_number

class ParkingGarage:

    def __init__(self, capacity: int, payment_service: PaymentService, cost_per_hour):
        self.payment_service = payment_service
        self.capacity = capacity
        self.used = 0
        self.cost_per_hour = cost_per_hour

    def can_park(self) -> bool:
        return self.used < self.capacity

    def park(self, driver_name, plate_number) -> Ticket:
        ticket = Ticket(datetime.datetime.now(), driver_name, plate_number)
        self.used += 1
        return ticket

    def calculate_cost(self, duration: datetime.timedelta):
        return math.ceil(duration.seconds / 60) * self.cost_per_hour

    def leave(self, ticket: Ticket, credit_card_number):
        duration = datetime.datetime.now() - ticket.start_time
        cost = self.calculate_cost(duration)

        payment = Payment(cost, credit_card_number, ticket.driver_name)
        receipt = self.payment_service.pay(payment)
        return receipt






