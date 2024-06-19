import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
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
        self.cart = []  # Initialize the cart

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
        signup_window.geometry("400x500")

        name_label = tk.Label(signup_window, text="Username")
        name_label.grid(row=0, column=0, padx=10, pady=10)
        name_entry = tk.Entry(signup_window)
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        email_label = tk.Label(signup_window, text="Email")
        email_label.grid(row=1, column=0, padx=10, pady=10)
        email_entry = tk.Entry(signup_window)
        email_entry.grid(row=1, column=1, padx=10, pady=10)

        password_label = tk.Label(signup_window, text="Password")
        password_label.grid(row=2, column=0, padx=10, pady=10)
        password_entry = tk.Entry(signup_window, show="*")
        password_entry.grid(row=2, column=1, padx=10, pady=10)

        confirm_password_label = tk.Label(signup_window, text="Confirm Password")
        confirm_password_label.grid(row=3, column=0, padx=10, pady=10)
        confirm_password_entry = tk.Entry(signup_window, show="*")
        confirm_password_entry.grid(row=3, column=1, padx=10, pady=10)

        phone_label = tk.Label(signup_window, text="Phone Number")
        phone_label.grid(row=4, column=0, padx=10, pady=10)
        phone_entry = tk.Entry(signup_window)
        phone_entry.grid(row=4, column=1, padx=10, pady=10)

        address_label = tk.Label(signup_window, text="Address")
        address_label.grid(row=5, column=0, padx=10, pady=10)
        address_entry = tk.Entry(signup_window)
        address_entry.grid(row=5, column=1, padx=10, pady=10)

        def register_user():
            username = name_entry.get()
            email = email_entry.get()
            password = password_entry.get()
            confirm_password = confirm_password_entry.get()
            phone = phone_entry.get()
            address = address_entry.get()

            if not all([username, email, password, confirm_password]):
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
        register_button.grid(row=6, column=0, columnspan=2, pady=10)

    def check_credentials(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        print(f"Attempting login with Username: {username} and Password: {password}")

        conn = sqlite3.connect('Zomato.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM User WHERE Username=? AND Password=?", (username, password))
        user = cursor.fetchone()

        conn.close()

        if user:
            print("Login successful!")  
            messagebox.showinfo("Success", "Login successful!")
            self.show_category_screen()
            # Implement further actions after successful login
        else:
            print("Invalid username or password")
        messagebox.showerror("Error", "Invalid username or password")


    def show_category_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill='both', expand=True)

        self.category_bg_image = Image.open('p3v1.png')
        self.category_bg_photo = ImageTk.PhotoImage(self.category_bg_image)
        self.canvas.create_image(0, 0, image=self.category_bg_photo, anchor='nw')
            
        self.canvas.bind("<Configure>", self.resize_category_bg_image)

        form_frame = tk.Frame(self.canvas, bg='white', padx=20, pady=20, relief=tk.RIDGE, bd=5)
        form_frame.place(relx=0.5, rely=0.5, anchor='center')

        veg_button = ttk.Button(form_frame, text="Vegetarian", style="TButton", command=lambda: self.show_menu_screen("Veg"))
        veg_button.grid(row=0, column=0, pady=10, ipadx=50)

        non_veg_button = ttk.Button(form_frame, text="Non-Vegetarian", style="TButton", command=lambda: self.show_menu_screen("Non-Veg"))
        non_veg_button.grid(row=1, column=0, pady=10, ipadx=50)

    def resize_category_bg_image(self, event):
        new_width = event.width
        new_height = event.height
        resized_category_bg_image = self.category_bg_image.resize((new_width, new_height), Image.LANCZOS)
        self.category_bg_photo = ImageTk.PhotoImage(resized_category_bg_image)
        self.canvas.create_image(0, 0, image=self.category_bg_photo, anchor='nw')

    def show_menu_screen(self, category):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill='both', expand=True)

        self.menu_bg_image = Image.open('p3v1.png')
        self.menu_bg_photo = ImageTk.PhotoImage(self.menu_bg_image)
        self.canvas.create_image(0, 0, image=self.menu_bg_photo, anchor='nw')
            
        self.canvas.bind("<Configure>", self.resize_menu_bg_image)

        form_frame = tk.Frame(self.canvas, bg='white', padx=20, pady=20, relief=tk.RIDGE, bd=5)
        form_frame.place(relx=0.5, rely=0.5, anchor='center')

        conn = sqlite3.connect('Zomato.db')
        cursor = conn.cursor()
        cursor.execute("SELECT Name, Price FROM Menu WHERE Category=?", (category,))
        menu_items = cursor.fetchall()
        conn.close()

        self.cart = []
        self.check_vars = []

        for i, item in enumerate(menu_items):
            name, price = item
            var = tk.IntVar()
            check_button = tk.Checkbutton(form_frame, text=f"{name} - ${price}", variable=var, bg='white')
            check_button.grid(row=i, column=0, sticky='w')
            self.check_vars.append((name, price, var))
                
            qty_label = tk.Label(form_frame, text="Qty:", bg='white')
            qty_label.grid(row=i, column=1)

            qty_combobox = ttk.Combobox(form_frame, values=list(range(1, 11)), state='readonly', width=3)
            qty_combobox.grid(row=i, column=2)
            qty_combobox.set(1)
            self.cart.append((name, price, var, qty_combobox))

        add_to_cart_button = ttk.Button(form_frame, text="Add to Cart", style="TButton", command=self.add_to_cart)
        add_to_cart_button.grid(row=len(menu_items), column=0, columnspan=3, pady=10, ipadx=100)

    def resize_menu_bg_image(self, event):
        new_width = event.width
        new_height = event.height
        resized_menu_bg_image = self.menu_bg_image.resize((new_width, new_height), Image.LANCZOS)
        self.menu_bg_photo = ImageTk.PhotoImage(resized_menu_bg_image)
        self.canvas.create_image(0, 0, image=self.menu_bg_photo, anchor='nw')

    def add_to_cart(self):
        selected_items = [(name, price, int(qty_combobox.get())) for name, price, var, qty_combobox in self.cart if var.get() == 1]

        if not selected_items:
            messagebox.showerror("Error", "No items selected!")
            return

        cart_window = tk.Toplevel(self.root)
        cart_window.title("Cart")
        cart_window.geometry("400x400")

        total_price = 0
        for i, item in enumerate(selected_items):
            name, price, qty = item
            item_total = price * qty
            total_price += item_total
            item_label = tk.Label(cart_window, text=f"{name} - ${price} x {qty} = ${item_total}")
            item_label.grid(row=i, column=0, padx=10, pady=10)

        total_label = tk.Label(cart_window, text=f"Total: ${total_price}", font=("Helvetica", 12, 'bold'))
        total_label.grid(row=len(selected_items), column=0, padx=10, pady=10)

        checkout_button = ttk.Button(cart_window, text="Checkout", style="TButton", command=lambda: messagebox.showinfo("Order", "Order placed successfully!"))
        checkout_button.grid(row=len(selected_items) + 1, column=0, padx=10, pady=10)

    # Setup the application
root = tk.Tk()
app = LoginApp(root, 'background.png', 'form_image.jpg', 'zomato_icon.ico')
root.mainloop()
