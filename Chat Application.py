import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class ChatApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Chat Application")

        self.username_label = tk.Label(master, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack()

        self.chat_history = tk.Text(master)
        self.chat_history.pack()

        self.message_label = tk.Label(master, text="Message:")
        self.message_label.pack()
        self.message_entry = tk.Entry(master)
        self.message_entry.pack()

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack()

        self.messages = []

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Here you would implement actual authentication logic,
        # such as checking against a database of users.
        if username == "admin" and password == "admin":
            messagebox.showinfo("Login", "Login successful!")
            self.username_label.pack_forget()
            self.username_entry.pack_forget()
            self.password_label.pack_forget()
            self.password_entry.pack_forget()
            self.login_button.pack_forget()

            # Example messages
            self.messages = [
                {"sender": "admin", "message": "Hello!", "time": datetime.now()},
                {"sender": "user1", "message": "Hi there!", "time": datetime.now()}
            ]
            self.update_chat_history()
        else:
            messagebox.showerror("Login Error", "Invalid username or password")

    def send_message(self):
        message = self.message_entry.get()
        if message:
            self.messages.append({"sender": "admin", "message": message, "time": datetime.now()})
            self.message_entry.delete(0, tk.END)
            self.update_chat_history()

    def update_chat_history(self):
        self.chat_history.config(state=tk.NORMAL)
        self.chat_history.delete(1.0, tk.END)
        for msg in self.messages:
            self.chat_history.insert(tk.END, f"{msg['time'].strftime('%H:%M:%S')} - {msg['sender']}: {msg['message']}\n")
        self.chat_history.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = ChatApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()
