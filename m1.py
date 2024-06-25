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
    def __init__(self, root, bg_image_path, form_image_path):
        self.root = root
        self.root.title("Zomato Login")
        self.root.state('zoomed')
        self.root.resizable(True, True)
        self.cart = []  # Initialize the cart

        # Set the application icon
        #self.root.iconbitmap(icon_path)
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
            messagebox.showinfo("Login Successful", "Welcome to Zomato!")
            self.show_category_screen()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def show_category_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor='nw')

        self.category_frame = tk.Frame(self.canvas, bg='white', padx=20, pady=20, relief=tk.RIDGE, bd=5)
        self.category_frame.place(relx=0.5, rely=0.5, anchor='center')

        conn = sqlite3.connect('Zomato.db')
        cursor = conn.cursor()

        cursor.execute("SELECT Name FROM Restaurants")
        restaurants = [row[0] for row in cursor.fetchall()]

        row_num = 0
        for restaurant in restaurants:
            restaurant_label = tk.Label(self.category_frame, text=restaurant, font=("Helvetica", 14), bg='white')
            restaurant_label.grid(row=row_num, column=0, pady=10, padx=10)

            view_button = tk.Button(self.category_frame, text="View", command=lambda rest=restaurant: self.show_item_screen(rest))
            view_button.grid(row=row_num, column=1, pady=10, padx=10)

            row_num += 1

        conn.close()

        cart_button = tk.Button(self.category_frame, text="View Cart", command=self.show_cart)
        cart_button.grid(row=row_num, column=0, columnspan=2, pady=20, ipadx=100)

    def show_item_screen(self, restaurant):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor='nw')

        self.item_frame = tk.Frame(self.canvas, bg='white', padx=20, pady=20, relief=tk.RIDGE, bd=5)
        self.item_frame.place(relx=0.5, rely=0.5, anchor='center')

        conn = sqlite3.connect('Zomato.db')
        cursor = conn.cursor()

        cursor.execute("SELECT ItemID, Name, Description, Price, Category FROM Menu WHERE RestaurantID=(SELECT RestaurantID FROM Restaurants WHERE Name=?)", (restaurant,))
        items = cursor.fetchall()

        row_num = 0
        for item in items:
            item_id, item_name, description, price, category = item
            item_label = tk.Label(self.item_frame, text=f"{item_name} - ₹{price} ({category})", font=("Helvetica", 14), bg='white')
            item_label.grid(row=row_num, column=0, pady=10, padx=10)

            add_to_cart_button = tk.Button(self.item_frame, text="Add to Cart", command=lambda id=item_id, name=item_name, price=price: self.add_to_cart(id, name, price))
            add_to_cart_button.grid(row=row_num, column=1, pady=10, padx=10)

            row_num += 1

        conn.close()

        back_button = tk.Button(self.item_frame, text="Back", command=self.show_category_screen)
        back_button.grid(row=row_num, column=0, columnspan=2, pady=20, ipadx=100)

    def add_to_cart(self, item_id, item_name, price):
        self.cart.append((item_id, item_name, price))
        messagebox.showinfo("Success", f"{item_name} added to cart!")

    def show_cart(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor='nw')

        self.cart_frame = tk.Frame(self.canvas, bg='white', padx=20, pady=20, relief=tk.RIDGE, bd=5)
        self.cart_frame.place(relx=0.5, rely=0.5, anchor='center')

        row_num = 0
        subtotal = 0
        for item in self.cart:
            item_id, item_name, price = item
            item_label = tk.Label(self.cart_frame, text=f"{item_name} - ₹{price}", font=("Helvetica", 14), bg='white')
            item_label.grid(row=row_num, column=0, pady=10, padx=10)

            row_num += 1
            subtotal += price

        tax = subtotal * 0.05  # 5% tax
        subtotal_with_tax = subtotal + tax

        subtotal_label = tk.Label(self.cart_frame, text=f"Subtotal: ₹{subtotal}", font=("Helvetica", 14), bg='white')
        subtotal_label.grid(row=row_num, column=0, pady=10, padx=10)
        
        tax_label = tk.Label(self.cart_frame, text=f"Tax (5%): ₹{tax:.2f}", font=("Helvetica", 14), bg='white')
        tax_label.grid(row=row_num + 1, column=0, pady=10, padx=10)

        discount_label = tk.Label(self.cart_frame, text=f"Discount (10%): -₹0.00", font=("Helvetica", 14), bg='white')
        discount_label.grid(row=row_num + 2, column=0, pady=10, padx=10)

        total_label = tk.Label(self.cart_frame, text=f"Total: ₹{subtotal_with_tax:.2f}", font=("Helvetica", 16, 'bold'), bg='white')
        total_label.grid(row=row_num + 3, column=0, pady=10, padx=10)

        discount_code_label = tk.Label(self.cart_frame, text="Discount Code:", font=("Helvetica", 14), bg='white')
        discount_code_label.grid(row=row_num + 4, column=0, pady=10, padx=10)

        discount_code_entry = tk.Entry(self.cart_frame, font=("Helvetica", 14))
        discount_code_entry.grid(row=row_num + 4, column=1, pady=10, padx=10)

        def apply_discount():
            discount_code = discount_code_entry.get()
            if discount_code == "SAVE10":
                discount = subtotal_with_tax * 0.10  # 10% discount on subtotal with tax
                total_with_discount = subtotal_with_tax - discount

                discount_label.config(text=f"Discount (10%): -₹{discount:.2f}")
                total_label.config(text=f"Total: ₹{total_with_discount:.2f}")
            else:
                messagebox.showerror("Invalid Code", "The discount code you entered is invalid.")

        apply_discount_button = tk.Button(self.cart_frame, text="Apply Discount", command=apply_discount)
        apply_discount_button.grid(row=row_num + 5, column=0, columnspan=2, pady=10, ipadx=100)

        place_order_button = tk.Button(self.cart_frame, text="Place Order", command=self.place_order)
        place_order_button.grid(row=row_num + 6, column=0, columnspan=2, pady=20, ipadx=100)

        back_button = tk.Button(self.cart_frame, text="Back", command=self.show_category_screen)
        back_button.grid(row=row_num + 7, column=0, columnspan=2, pady=10, ipadx=100)

    def place_order(self):
        messagebox.showinfo("Order", "Your order has been placed!")
        self.cart.clear()
        self.show_category_screen()
        self.ask_for_review()

    def ask_for_review(self):
        review_window = tk.Toplevel(self.root)
        review_window.title("Leave a Review")
        review_window.geometry("400x300")

        review_frame = tk.Frame(review_window, bg='white', padx=20, pady=20, relief=tk.RIDGE, bd=5)
        review_frame.pack(fill='both', expand=True)

        review_label = tk.Label(review_frame, text="Please leave a review for your order:", font=("Helvetica", 14), bg='white')
        review_label.grid(row=0, column=0, columnspan=2, pady=10)

        review_text = tk.Text(review_frame, height=5, width=30, font=("Helvetica", 12))
        review_text.grid(row=1, column=0, columnspan=2, pady=10)

        rating_label = tk.Label(review_frame, text="Rating:", font=("Helvetica", 14), bg='white')
        rating_label.grid(row=2, column=0, pady=10, padx=10)

        rating_var = tk.StringVar(review_frame)
        rating_var.set("1")  # Default rating

        rating_dropdown = ttk.Combobox(review_frame, textvariable=rating_var, values=["1", "2", "3", "4", "5"], state="readonly", width=5, font=("Helvetica", 12))
        rating_dropdown.grid(row=2, column=1, pady=10, padx=10)

        def submit_review():
            review = review_text.get("1.0", tk.END).strip()
            rating = rating_var.get()

            if review:
                messagebox.showinfo("Thank You", "Thank you for your review!")
                review_window.destroy()
                self.save_review_to_database(review, rating)
            else:
                messagebox.showwarning("Warning", "Review cannot be empty")

        submit_button = tk.Button(review_frame, text="Submit", command=submit_review, font=("Helvetica", 12, 'bold'))
        submit_button.grid(row=3, column=0, columnspan=2, pady=10)

    def save_review_to_database(self, review, rating):
        # Assuming a database structure is already set up with a Reviews table
        conn = sqlite3.connect('Zomato.db')
        cursor = conn.cursor()

        # Example: Inserting review into the database
        cursor.execute("INSERT INTO Reviews (ReviewText, Rating) VALUES (?, ?)", (review, rating))
        conn.commit()
        conn.close()

        print(f"Review: {review}, Rating: {rating} saved to database")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root, bg_image_path='background.png', form_image_path='form_image.jpg')
    root.mainloop()
    
