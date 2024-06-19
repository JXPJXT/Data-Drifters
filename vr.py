import tkinter as tk
from tkinter import ttk
import sqlite3

class ZomatoApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Zomato App")
        self.root.geometry("400x300")
        self.cart = {}

        self.show_veg_nonveg_selection()

    def show_veg_nonveg_selection(self):
        selection_window = tk.Toplevel(self.root)
        selection_window.title("Select Category")
        selection_window.geometry("300x200")

        veg_button = tk.Button(selection_window, text="Veg", command=lambda: self.show_restaurants("Veg"))
        veg_button.pack(pady=20)

        non_veg_button = tk.Button(selection_window, text="Non-Veg", command=lambda: self.show_restaurants("Non-Veg"))
        non_veg_button.pack(pady=20)

    def show_restaurants(self, category):
        restaurant_window = tk.Toplevel(self.root)
        restaurant_window.title(f"{category} Restaurants")
        restaurant_window.geometry("600x400")

        conn = sqlite3.connect('Zomato.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT DISTINCT Restaurants.Name, Restaurants.RestaurantID
            FROM Restaurants 
            JOIN Menu ON Restaurants.RestaurantID = Menu.RestaurantID 
            WHERE Menu.Category = ?;
        ''', (category,))
        restaurants = cursor.fetchall()
        conn.close()

        for restaurant in restaurants:
            restaurant_button = tk.Button(restaurant_window, text=restaurant[0], command=lambda r=restaurant[1]: self.show_menu(r))
            restaurant_button.pack(pady=5)

    def show_menu(self, restaurant_id):
        menu_window = tk.Toplevel(self.root)
        menu_window.title("Menu")
        menu_window.geometry("600x400")

        conn = sqlite3.connect('Zomato.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT ItemID, Name, Description, Price 
            FROM Menu 
            WHERE RestaurantID = ?;
        ''', (restaurant_id,))
        menu_items = cursor.fetchall()
        conn.close()

        for item in menu_items:
            item_frame = tk.Frame(menu_window)
            item_frame.pack(pady=5)

            item_label = tk.Label(item_frame, text=f"{item[1]} - {item[2]} - ₹{item[3]}")
            item_label.pack(side=tk.LEFT, padx=10)

            quantity_label = tk.Label(item_frame, text="Qty:")
            quantity_label.pack(side=tk.LEFT, padx=5)

            quantity_var = tk.StringVar(value="1")
            quantity_dropdown = ttk.Combobox(item_frame, textvariable=quantity_var, values=[str(i) for i in range(1, 11)])
            quantity_dropdown.pack(side=tk.LEFT, padx=5)

            add_to_cart_button = tk.Button(item_frame, text="Add to Cart", command=lambda i=item[0], q=quantity_var: self.add_to_cart(i, q.get()))
            add_to_cart_button.pack(side=tk.LEFT, padx=10)

        view_cart_button = tk.Button(menu_window, text="View Cart", command=self.show_cart)
        view_cart_button.pack(pady=20)

    def add_to_cart(self, item_id, quantity):
        if item_id in self.cart:
            self.cart[item_id] += int(quantity)
        else:
            self.cart[item_id] = int(quantity)

    def show_cart(self):
        cart_window = tk.Toplevel(self.root)
        cart_window.title("Cart")
        cart_window.geometry("600x400")

        conn = sqlite3.connect('Zomato.db')
        cursor = conn.cursor()

        cart_items = []
        total_amount = 0

        for item_id, quantity in self.cart.items():
            cursor.execute('SELECT Name, Price FROM Menu WHERE ItemID = ?', (item_id,))
            item = cursor.fetchone()
            cart_items.append((item[0], item[1], quantity))
            total_amount += item[1] * quantity

        conn.close()

        for item in cart_items:
            item_label = tk.Label(cart_window, text=f"{item[0]} - ₹{item[1]} x {item[2]} = ₹{item[1] * item[2]}")
            item_label.pack(pady=5)

        total_label = tk.Label(cart_window, text=f"Total Amount: ₹{total_amount}")
        total_label.pack(pady=20)

        checkout_button = tk.Button(cart_window, text="Checkout", command=self.checkout)
        checkout_button.pack(pady=20)

    def checkout(self):
        # Implement checkout functionality here
        pass

if __name__ == "__main_":
    root = tk.Tk()
    app = ZomatoApp(root)
    root.mainloop()