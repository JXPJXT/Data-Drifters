import sqlite3
import pandas as pd

def export_to_excel():
    try:
        # Connect to SQLite database
        conn = sqlite3.connect('Zomato.db')

        # Read data from SQLite into DataFrames
        df_users = pd.read_sql_query("SELECT * FROM User", conn)
        df_restaurants = pd.read_sql_query("SELECT * FROM Restaurants", conn)
        df_menu = pd.read_sql_query("SELECT * FROM Menu", conn)
        df_orders = pd.read_sql_query("SELECT * FROM Orders", conn)
        df_checkout = pd.read_sql_query("SELECT * FROM Checkout", conn)
        df_review = pd.read_sql_query("SELECT * FROM Review", conn)

        # Close database connection
        conn.close()

        # Export each DataFrame to Excel sheets
        with pd.ExcelWriter('Zomato_Data.xlsx') as writer:
            df_users.to_excel(writer, sheet_name='Users', index=False)
            df_restaurants.to_excel(writer, sheet_name='Restaurants', index=False)
            df_menu.to_excel(writer, sheet_name='Menu', index=False)
            df_orders.to_excel(writer, sheet_name='Orders', index=False)
            df_checkout.to_excel(writer, sheet_name='Checkout', index=False)
            df_review.to_excel(writer, sheet_name='Review', index=False)

        print("Data exported successfully to Zomato_Data.xlsx")
    
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    export_to_excel()
