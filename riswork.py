import sqlite3

def insert_sample_data():
    conn = sqlite3.connect('Zomato.db')
    cursor = conn.cursor()

    # Insert Restaurants
    cursor.execute('INSERT INTO Restaurants (Name, Address, CuisineType, AverageRating) VALUES (?, ?, ?, ?)', ("Green Leaf", "123 Veg Lane", "Vegetarian", 4.5))
    cursor.execute('INSERT INTO Restaurants (Name, Address, CuisineType, AverageRating) VALUES (?, ?, ?, ?)', ("Carnivore's Delight", "456 Meat Street", "Non-Vegetarian", 4.7))
    
    # Get Restaurant IDs
    cursor.execute('SELECT RestaurantID FROM Restaurants WHERE Name = ?', ("Green Leaf",))
    green_leaf_id = cursor.fetchone()[0]

    cursor.execute('SELECT RestaurantID FROM Restaurants WHERE Name = ?', ("Carnivore's Delight",))
    carnivores_delight_id = cursor.fetchone()[0]

    # Insert Veg Menu Items
    cursor.execute('INSERT INTO Menu (RestaurantID, Name, Description, Price, Category) VALUES (?, ?, ?, ?, ?)', (green_leaf_id, "Paneer Butter Masala", "Creamy paneer curry", 250, "Veg"))
    cursor.execute('INSERT INTO Menu (RestaurantID, Name, Description, Price, Category) VALUES (?, ?, ?, ?, ?)', (green_leaf_id, "Veg Biryani", "Spicy mixed veg rice", 200, "Veg"))

    # Insert Non-Veg Menu Items
    cursor.execute('INSERT INTO Menu (RestaurantID, Name, Description, Price, Category) VALUES (?, ?, ?, ?, ?)', (carnivores_delight_id, "Chicken Biryani", "Spicy chicken rice", 300, "Non-Veg"))
    cursor.execute('INSERT INTO Menu (RestaurantID, Name, Description, Price, Category) VALUES (?, ?, ?, ?, ?)', (carnivores_delight_id, "Mutton Kebab", "Juicy mutton kebabs", 350, "Non-Veg"))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_sample_data()