from abc import ABC, abstractmethod
from typing import Union


class Dimmable(ABC):
    @abstractmethod
    def dim(self):
        pass


class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable, Dimmable):
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")

    def dim(self):
        print("Dimming to 50%...")


class Fan(Switchable):
    def turn_on(self):
        print("Fan: turned on...")

    def turn_off(self):
        print("Fan: turned on...")


class ElectricPowerSwitch:

    def __init__(self, client: Switchable):
        self.client = client
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True


l = LightBulb()
f = Fan()
switch = ElectricPowerSwitch(f)
switch.press()
switch.press()
