import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from itertools import cycle
import sqlite3

class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = "grey"
        self.default_fg_color = self["fg"]

        self.bind("<FocusIn>", self._on_focus_in)
        self.bind("<FocusOut>", self._on_focus_out)

        self.put_placeholder()

    def _on_focus_in(self, event):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.config(fg=self.default_fg_color)

    def _on_focus_out(self, event):
        if not self.get():
            self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self.config(fg=self.placeholder_color)

class LoginApp:
    def __init__(self, root, bg_image_path, form_image_path, icon_path):
        self.root = root
        self.root.title("Zomato Login")
        self.root.state('zoomed')
        self.root.resizable(True, True)

        # Set the application icon
        self.root.iconbitmap(icon_path)

        # Background image setup
        self.bg_image = Image.open(bg_image_path)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.canvas = tk.Canvas(root)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor='nw')
        
        self.canvas.bind("<Configure>", self.resize_bg_image)

        # Form image setup
        self.form_image = Image.open(form_image_path)
        self.form_photo = ImageTk.PhotoImage(self.form_image)

        self.create_login_form()

    def resize_bg_image(self, event):
        new_width = event.width
        new_height = event.height
        resized_bg_image = self.bg_image.resize((new_width, new_height), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(resized_bg_image)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor='nw')

    def create_login_form(self):
        form_frame = tk.Frame(self.canvas, bg='white', padx=20, pady=20, relief=tk.RIDGE, bd=5)
        form_frame.place(relx=0.5, rely=0.5, anchor='center')

        image_label = tk.Label(form_frame, image=self.form_photo, bg='white')
        image_label.grid(row=0, column=0, columnspan=2, pady=10)

        username_label = tk.Label(form_frame, text="Username", font=("Helvetica", 12, 'bold'), bg='white', fg='#e23744')
        username_label.grid(row=1, column=0, columnspan=2, sticky='w', pady=(20, 5))

        username_frame = tk.Frame(form_frame, bg='white')
        username_frame.grid(row=2, column=0, columnspan=2)

        self.username_entry = EntryWithPlaceholder(username_frame, placeholder="Username", width=30, font=("Helvetica", 12), bd=1)
        self.username_entry.grid(row=0, column=0, sticky="ew", padx=(0, 10), pady=5)

        password_label = tk.Label(form_frame, text="Password", font=("Helvetica", 12, 'bold'), bg='white', fg='#e23744')
        password_label.grid(row=3, column=0, columnspan=2, sticky='w', pady=(20, 5))

        password_frame = tk.Frame(form_frame, bg='white')
        password_frame.grid(row=4, column=0, columnspan=2)

        self.password_entry = EntryWithPlaceholder(password_frame, placeholder="Password", width=30, font=("Helvetica", 12), show="*", bd=1)
        self.password_entry.grid(row=0, column=0, sticky="ew", padx=(0, 10), pady=5)

        remember_var = tk.IntVar()
        remember_check = tk.Checkbutton(form_frame, text="Remember username", variable=remember_var, bg='white')
        remember_check.grid(row=5, column=0, columnspan=2, pady=5)

        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#e23744", foreground="white", font=("Helvetica", 12, 'bold'))
        style.map("TButton", background=[("active", "#7EC8E3")])

        login_button = ttk.Button(form_frame, text="Log in", style="TButton", command=self.check_credentials)
        login_button.grid(row=6, column=0, columnspan=2, pady=10, ipadx=100)

        signup_button = ttk.Button(form_frame, text="Sign up", style="TButton", command=self.show_signup_form)
        signup_button.grid(row=7, column=0, columnspan=2, pady=10, ipadx=100)

    def show_signup_form(self):
        signup_window = tk.Toplevel(self.root)
        signup_window.title("Sign up")
        signup_window.geometry("400x400")

        name_label = tk.Label(signup_window, text="Full Name")
        name_label.grid(row=0, column=0, padx=10, pady=10)
        name_entry = tk.Entry(signup_window)
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        username_label = tk.Label(signup_window, text="Username")
        username_label.grid(row=1, column=0, padx=10, pady=10)
        username_entry = tk.Entry(signup_window)
        username_entry.grid(row=1, column=1, padx=10, pady=10)

        email_label = tk.Label(signup_window, text="Email")
        email_label.grid(row=2, column=0, padx=10, pady=10)
        email_entry = tk.Entry(signup_window)
        email_entry.grid(row=2, column=1, padx=10, pady=10)

        password_label = tk.Label(signup_window, text="Password")
        password_label.grid(row=3, column=0, padx=10, pady=10)
        password_entry = tk.Entry(signup_window, show="*")
        password_entry.grid(row=3, column=1, padx=10, pady=10)

        confirm_password_label = tk.Label(signup_window, text="Confirm Password")
        confirm_password_label.grid(row=4, column=0, padx=10, pady=10)
        confirm_password_entry = tk.Entry(signup_window, show="*")
        confirm_password_entry.grid(row=4, column=1, padx=10, pady=10)

        phone_label = tk.Label(signup_window, text="Phone Number")
        phone_label.grid(row=5, column=0, padx=10, pady=10)
        phone_entry = tk.Entry(signup_window)
        phone_entry.grid(row=5, column=1, padx=10, pady=10)

        address_label = tk.Label(signup_window, text="Address")
        address_label.grid(row=6, column=0, padx=10, pady=10)
        address_entry = tk.Entry(signup_window)
        address_entry.grid(row=6, column=1, padx=10, pady=10)

        def register_user():
            name = name_entry.get()
            username = username_entry.get()
            email = email_entry.get()
            password = password_entry.get()
            confirm_password = confirm_password_entry.get()
            phone = phone_entry.get()
            address = address_entry.get()

            if not all([name, username, email, password, confirm_password, phone, address]):
                messagebox.showerror("Error", "All fields are required!")
                return

            if password != confirm_password:
                messagebox.showerror("Error", "Passwords do not match!")
                return

            conn = sqlite3.connect('Zomato.db')
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM User WHERE Email=?", (email,))
            if cursor.fetchone() is not None:
                messagebox.showerror("Error", "User with this email already exists!")
                conn.close()
                return

            cursor.execute("INSERT INTO User (Username, Email, Password, PhoneNumber, Address) VALUES (?, ?, ?, ?, ?)",
                           (username, email, password, phone, address))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Registration successful!")
            signup_window.destroy()

        register_button = tk.Button(signup_window, text="Register", command=register_user)
        register_button.grid(row=7, column=0, columnspan=2, pady=10)

    def check_credentials(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        conn = sqlite3.connect('Zomato.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User WHERE Username=? AND Password=?", (username, password))
        result = cursor.fetchone()
        conn.close()

        if result:
            messagebox.showinfo("Success", "Login successful!")
        else:
            messagebox.showerror("Error", "Invalid credentials. Please try again.")

def main():
    root = tk.Tk()
    bg_image_path = r"C:\Users\bhati\OneDrive\Desktop\Zomato\p3.png"
    form_image_path = r"C:\Users\bhati\OneDrive\Desktop\Zomato\logo2.png"
    icon_path = r"C:\Users\bhati\OneDrive\Desktop\Zomato\logo.ico"

    app = LoginApp(root, bg_image_path, form_image_path, icon_path)
    root.mainloop()

if __name__ == "__main__":
    main()
