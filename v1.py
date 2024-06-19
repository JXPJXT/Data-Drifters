import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from itertools import cycle

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

        signup_button = ttk.Button(form_frame, text="Sign up", style="TButton", command=self.show_signup_page)
        signup_button.grid(row=7, column=0, columnspan=2, pady=10, ipadx=100)

        forgotten_label = tk.Label(form_frame, text="Forgotten your username or password?", font=("Helvetica", 10, 'bold'), fg='#e23744', bg='white')
        forgotten_label.grid(row=8, column=0, columnspan=2, pady=5)

    def check_credentials(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Dummy check for credentials - replace with actual authentication logic
        if username == "admin" and password == "password":
            messagebox.showinfo("Success", "Login Successful!")
            self.show_loading_page()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def show_loading_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        loading_label = tk.Label(self.root, text="Logging in...", font=("Helvetica", 16, 'bold'), bg='white')
        loading_label.place(relx=0.5, rely=0.5, anchor='center')

        spinner = cycle(['|', '/', '-', '\\'])
        spinner_label = tk.Label(self.root, text="", font=("Helvetica", 24, 'bold'), bg='white')
        spinner_label.place(relx=0.5, rely=0.55, anchor='center')

        def animate():
            spinner_label.config(text=next(spinner))
            self.root.after(100, animate)

        animate()

    def show_signup_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        signup_frame = tk.Frame(self.canvas, bg='#e23744', padx=20, pady=20, relief=tk.RIDGE, bd=5)
        signup_frame.place(relx=0.5, rely=0.5, anchor='center')

        username_label = tk.Label(signup_frame, text="Username", font=("Helvetica", 12, 'bold'), bg='#e23744', fg='white')
        username_label.grid(row=0, column=0, pady=(20, 5))

        self.signup_username_entry = EntryWithPlaceholder(signup_frame, placeholder="Username", width=30, font=("Helvetica", 12), bd=1)
        self.signup_username_entry.grid(row=1, column=0, pady=5)

        password_label = tk.Label(signup_frame, text="Password", font=("Helvetica", 12, 'bold'), bg='#e23744', fg='white')
        password_label.grid(row=2, column=0, pady=(20, 5))

        self.signup_password_entry = EntryWithPlaceholder(signup_frame, placeholder="Password", width=30, font=("Helvetica", 12), show="*", bd=1)
        self.signup_password_entry.grid(row=3, column=0, pady=5)

        confirm_password_label = tk.Label(signup_frame, text="Confirm Password", font=("Helvetica", 12, 'bold'), bg='#e23744', fg='white')
        confirm_password_label.grid(row=4, column=0, pady=(20, 5))

        self.confirm_password_entry = EntryWithPlaceholder(signup_frame, placeholder="Confirm Password", width=30, font=("Helvetica", 12), show="*", bd=1)
        self.confirm_password_entry.grid(row=5, column=0, pady=5)

        signup_button = ttk.Button(signup_frame, text="Sign up", style="TButton", command=self.create_account)
        signup_button.grid(row=6, column=0, pady=20, ipadx=100)

    def create_account(self):
        username = self.signup_username_entry.get()
        password = self.signup_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        # Dummy account creation logic - replace with actual database insertion
        messagebox.showinfo("Success", "Account created successfully!")
        self.create_login_form()

if __name__ == "__main__":
    bg_image_path = r"C:\Users\bhati\OneDrive\Desktop\Zomato\p3.png"
    form_image_path = r"C:\Users\bhati\OneDrive\Desktop\Zomato\file.png"
    icon_path = r"C:\Users\bhati\OneDrive\Desktop\Zomato\logo.ico"
    root = tk.Tk()
    app = LoginApp(root, bg_image_path, form_image_path, icon_path)
    root.mainloop()
