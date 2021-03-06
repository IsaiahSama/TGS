# File to handle EVERYTHING

import keyboard
from all_commands import commands, headlines
from os import system
import pynput
from time import sleep


class Main:
    def __init__(self, commands:dict) -> None:
        self.com = commands
        self.pressed = ""

    def run(self):
        while True:
            system("CLS")
            print("Waiting for you to press V:")
            self.listen_for_prompt()
            valid = self.track_input()
            if valid:
                self.send_message()
            self.pressed = ""

    def listen_for_prompt(self):
        keyboard.wait("v")

    def track_input(self):
        self.pressed += "V"
        print("\n".join(headlines))
        while True:
            with pynput.keyboard.Listener(on_press=self.on_press) as listener:
                listener.join()
            
            print(self.pressed)
            valid = [{command: text} for command, text in self.com.items() if command.startswith(self.pressed.upper())]

            if not valid: return False
            if len(valid) == 1: return True

            for pair in valid:
                for k, v in pair.items():
                    print(f"{k}: {v}")

    def send_message(self):
        message = self.com[self.pressed.upper()]
        keyboard.press_and_release("ctrl+a, backspace")
        sleep(0.3)
        keyboard.write(message.strip("\""))
        sleep(0.5)
        keyboard.press_and_release("enter")

    def on_press(self, key):
        self.pressed += key.__str__().upper().strip("'")
        return False


main = Main(commands)
if __name__ == "__main__":
    main.run()