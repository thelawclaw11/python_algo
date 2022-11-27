from dataclasses import dataclass
from typing import List
import shlex


@dataclass
class Command:
    command: str
    arguments: List[str]


def run_command(command: Command):
    match command:
        case Command("load", [filename]):
            print(F"Loading file: {filename}.")
        case Command("load", [filename]):
            print(f"Saving to file: {filename}.")
        case Command("quit" | "exit" | "bye", ["--force" | "-f", *rest]):
            print("Sending SIGTERM to all processes and quitting the program.")
            quit()
        case Command("quit" | "exit" | "bye", []):
            print("Quitting the program.")
            quit()
        case _:
            print(F"Unknown command: {command!r}.")


def main():
    while True:
        command, *arguments = shlex.split(input("$ "))
        run_command(Command(command, arguments))


if __name__ == "__main__":
    main()
