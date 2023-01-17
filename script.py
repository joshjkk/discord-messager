import tkinter as tk
import requests
import threading
import time


########## FILL THESE PARAMETERS IN ##########

# Channel link
# LOOKS SOMETHING LIKE THIS:
# https://discord.com/api/vNUMBER/SOME_NUMBERS/messages


########## FILL THESE PARAMETERS IN ##########


def notify_usage() -> None:
    print("\nDiscord does not allow self-bots, by using this software you are aware of possible account termination.")
    print("See https://support.discord.com/hc/en-us/articles/115002192352-Automated-user-accounts-self-bots- for info on self-bots.\n")


class App:
    def __init__(self, title: str, width: int, height: int, channel: str, message: str, authorization: str, timeout: int) -> None:
        # Set up parameters
        self.title = title
        self.width = width
        self.height = height

        # POST parameters
        self.channel = channel
        self.message = message
        self.authorization = authorization
        self.timeout = timeout

        # Create the window
        self.version = "2.0.0"
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+0+0")
        self.root.resizable(width=False, height=False)

        # Version number in the top left
        self.version_num = tk.Label(self.root, text=f"v{self.version}", font=("Arial", 11))
        self.version_num.place(relx=0.03, rely=0.02, anchor=tk.CENTER)

        # Channel link entry
        self.title_font = ("Arial", 13)
        self.entry_font = ("Arial", 12)
        
        self.channel_title = tk.Label(self.root, text="Channel Link", font=self.title_font)
        self.channel_title.place(relx=0.5, rely=0.065, anchor=tk.CENTER)

        self.channel_entry = tk.Entry(self.root, width=60, font=self.entry_font)
        self.channel_entry.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

        # Message entry
        self.message_title = tk.Label(self.root, text="Message", font=self.title_font)
        self.message_title.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

        self.message_entry = tk.Text(self.root, width=60, height=2, font=self.entry_font)
        self.message_entry.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

        # Authorization entry
        self.authorization_title = tk.Label(self.root, text="Authorization Key", font=self.title_font)
        self.authorization_title.place(relx=0.5, rely=0.475, anchor=tk.CENTER)

        self.authorization_entry = tk.Entry(self.root, width=60, font=self.entry_font)
        self.authorization_entry.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

        # Timeout entry
        self.timeout_title = tk.Label(self.root, text="Timeout Length (s)", font=self.title_font)
        self.timeout_title.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

        self.timeout_entry = tk.Entry(self.root, width=3, font=self.entry_font)
        self.timeout_entry.place(relx=0.5, rely=0.725, anchor=tk.CENTER)

        # Send message button
        self.button_font = ("Arial", 13)
        self.send_button = tk.Button(self.root, text="Send Message", font=self.button_font, command=self.send_message)
        self.send_button.place(relx=0.4, rely=0.9, anchor=tk.CENTER)

        # Loop checkbox
        self.auto = tk.BooleanVar()
        self.loop_box = tk.Checkbutton(self.root, text="Loop", font=self.button_font, variable=self.auto, command=self.toggle_loop)
        self.loop_box.place(relx=0.6, rely=0.9, anchor=tk.CENTER)

        self.root.mainloop()


    def toggle_loop(self) -> None:
        if self.auto.get() == True:
            self.loop_box.select()
        else:
            self.loop_box.deselect()


    def send_message(self) -> None:
        if self.auto.get() == False:
            thread = threading.Thread(target=self.post, daemon=False)
            thread.start()
        else:
            while self.auto.get() == True:
                thread = threading.Thread(target=self.post, daemon=True)
                thread.start()
                wait = threading.Thread(target=lambda: time.sleep(self.timeout_entry.get()), daemon=False)
                wait.start()
                wait.join()


    def post(self) -> None:
        # POST parameters
        payload = {
            'content': self.message_entry.get(1.0, tk.END)
        }

        headers = {
            'authorization': self.authorization_entry.get()
        }

        requests.post(url=self.channel_entry.get(), data=payload, headers=headers)


"""
self.channel = "CHANNEL TO SEND TO"
self.message = "MESSAGE TO SEND"
self.authorization = "AUTHORIZATION KEY"
self.timeout = 30
"""


def main() -> int:
    notify_usage()
    App("Discord Messager", 675, 400, "fdsafd", "dffdaf", "dflkjdf", 30)
    return 0


if __name__ == "__main__":
    exit(main())
