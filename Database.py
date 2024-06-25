import sqlite3

def create_database():
    conn = sqlite3.connect('Zomato.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS User (
        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
        Username TEXT NOT NULL,
        Email TEXT NOT NULL UNIQUE,
        Password TEXT NOT NULL,
        PhoneNumber TEXT,
        Address TEXT
    );
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Restaurants (
        RestaurantID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Address TEXT NOT NULL,
        CuisineType TEXT,
        AverageRating REAL
    );
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Menu (
        ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
        RestaurantID INTEGER,
        Name TEXT NOT NULL,
        Description TEXT,
        Price REAL NOT NULL,
        Quantity INTEGER DEFAULT 0,
        Category TEXT CHECK (Category IN ('Veg', 'Non-Veg')) DEFAULT 'Veg',
        FOREIGN KEY (RestaurantID) REFERENCES Restaurants(RestaurantID) ON DELETE CASCADE
    );
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Orders (
        OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserID INTEGER,
        RestaurantID INTEGER,
        OrderDate TEXT NOT NULL,
        FOREIGN KEY (UserID) REFERENCES User(UserID) ON DELETE CASCADE,
        FOREIGN KEY (RestaurantID) REFERENCES Restaurants(RestaurantID) ON DELETE CASCADE
    );
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Checkout (
        CheckoutID INTEGER PRIMARY KEY AUTOINCREMENT,
        OrderID INTEGER,
        PaymentMethod TEXT,
        PaymentDate TEXT,
        Status TEXT,
        TotalAmount REAL NOT NULL,
        FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE
    );
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Review (
        ReviewID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserID INTEGER,
        RestaurantID INTEGER,
        Rating INTEGER CHECK (Rating >= 1 AND Rating <= 5),
        Comment TEXT,
        ReviewDate TEXT,
        FOREIGN KEY (UserID) REFERENCES User(UserID) ON DELETE CASCADE,
        FOREIGN KEY (RestaurantID) REFERENCES Restaurants(RestaurantID) ON DELETE CASCADE
    );
    ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
