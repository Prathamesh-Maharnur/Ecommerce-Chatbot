from re import L
from tkinter import *

from numpy import delete
from chat import get_response, bot_name

BG_GRAY = "#ABB2B9"
BG_GREEN = "#57f542"
BG_YELLOW = "#f5ef42"
BG_COLOR = "#17202A"
TEXT_COLOR = "#000000"

FONT = "Helvetica 12 bold"
FONT_BOLD = "Helvetica 13 bold"

class ChatApplication:
    
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("E-Commerce ChatBot")
        self.window.resizable(width=False, height=True)
        self.window.configure(width=500, height=600, bg = BG_COLOR)

        # Head label
        head_label = Label(self.window, bg=BG_COLOR, fg="white", text="Welcome!!!", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # Divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # Text widget
        self.text_widget = Text(self.window, width=20, height=2, bg="#ffccff", fg=TEXT_COLOR, 
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # Scroll bar
        scroll_bar = Scrollbar(self.text_widget)
        scroll_bar.place(relheight=1, relx=0.974)
        scroll_bar.configure(command=self.text_widget.yview)

        # Bottom label
        bottom_label = Label(self.window, bg="#00ccff", height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # Message entry box
        self.msg_entry = Entry(bottom_label, bg="#f2f2f2", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.58, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # Send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GREEN, 
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.60, rely=0.008, relheight=0.06, relwidth=0.18)

        # Clear chats button
        clear_button = Button(bottom_label, text="Clear Chats", font=FONT_BOLD, width=20, bg=BG_YELLOW, 
                              command=self._clear_chat)
        clear_button.place(relx=0.79, rely=0.008, relheight=0.06, relwidth=0.21)
        

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        if not msg:
            return
    
        self.msg_entry.delete(0, END)
        msg1 = f'{sender}: {msg}\n\n'
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f'{bot_name}: {get_response(msg)}\n\n'
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)

    def _clear_chat(self):
        self.text_widget.configure(state=NORMAL)
        self.text_widget.delete(1.0, END)
        self.text_widget.configure(state=DISABLED)

if __name__ == "__main__":
    app = ChatApplication()
    app.run()
