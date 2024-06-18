import sqlite3
def insert_data():
    conn = sqlite3.connect('Zomato.db')
    cursor = conn.cursor()

    cursor.execute('''
    -- Insert Users
    INSERT INTO User (Username, Email, Password, PhoneNumber, Address) VALUES 
    ('RahulSharma', 'rahul.sharma@example.com', 'rahul123', '9123456780', '21, MG Road, Delhi'),
    ('PriyaVerma', 'priya.verma@example.com', 'priya456', '9123456781', '44, Park Avenue, Mumbai'),
    ('AmitKumar', 'amit.kumar@example.com', 'amit789', '9123456782', '78, Sector 22, Noida'),
    ('SnehaPatil', 'sneha.patil@example.com', 'sneha101', '9123456783', '32, Shivaji Park, Pune'),
    ('AnilMehta', 'anil.mehta@example.com', 'anil202', '9123456784', '12, Andheri West, Mumbai'),
    ('RaviJain', 'ravi.jain@example.com', 'ravi303', '9123456785', '56, Lajpat Nagar, Delhi'),
    ('SunitaRao', 'sunita.rao@example.com', 'sunita404', '9123456786', '89, Indiranagar, Bangalore'),
    ('VikramSingh', 'vikram.singh@example.com', 'vikram505', '9123456787', '23, Vasant Vihar, Delhi'),
    ('NishaYadav', 'nisha.yadav@example.com', 'nisha606', '9123456788', '67, Banjara Hills, Hyderabad'),
    ('KaranSinha', 'karan.sinha@example.com', 'karan707', '9123456789', '34, Malabar Hill, Mumbai'),
    ('PoojaDesai', 'pooja.desai@example.com', 'pooja808', '9123456790', '78, Koregaon Park, Pune'),
    ('ArjunKapoor', 'arjun.kapoor@example.com', 'arjun909', '9123456791', '45, DLF Phase 3, Gurgaon'),
    ('KavitaGupta', 'kavita.gupta@example.com', 'kavita010', '9123456792', '98, Jubilee Hills, Hyderabad'),
    ('SandeepReddy', 'sandeep.reddy@example.com', 'sandeep111', '9123456793', '55, Gachibowli, Hyderabad'),
    ('RekhaNair', 'rekha.nair@example.com', 'rekha212', '9123456794', '21, Jayanagar, Bangalore'),
    ('ManishShukla', 'manish.shukla@example.com', 'manish313', '9123456795', '88, Hazratganj, Lucknow'),
    ('AartiPandey', 'aarti.pandey@example.com', 'aarti414', '9123456796', '33, Salt Lake, Kolkata'),
    ('RajeshIyer', 'rajesh.iyer@example.com', 'rajesh515', '9123456797', '45, Anna Nagar, Chennai'),
    ('NehaMalhotra', 'neha.malhotra@example.com', 'neha616', '9123456798', '67, Sushant Lok, Gurgaon'),
    ('AkashSaxena', 'akash.saxena@example.com', 'akash717', '9123456799', '22, Rajouri Garden, Delhi'),
    ('MayaSen', 'maya.sen@example.com', 'maya818', '9123456700', '11, Alipore, Kolkata'),
    ('SahilBhatia', 'sahil.bhatia@example.com', 'sahil919', '9123456701', '88, Sion, Mumbai'),
    ('GeetaSharma', 'geeta.sharma@example.com', 'geeta020', '9123456702', '44, Sadashiv Peth, Pune'),
    ('HarshAggarwal', 'harsh.aggarwal@example.com', 'harsh121', '9123456703', '77, Model Town, Delhi'),
    ('LataJoshi', 'lata.joshi@example.com', 'lata222', '9123456704', '55, Jubilee Hills, Hyderabad'),
    ('NikhilPatel', 'nikhil.patel@example.com', 'nikhil323', '9123456705', '33, Vashi, Mumbai'),
    ('PallaviChopra', 'pallavi.chopra@example.com', 'pallavi424', '9123456706', '66, Gachibowli, Hyderabad'),
    ('RohitKhanna', 'rohit.khanna@example.com', 'rohit525', '9123456707', '77, Whitefield, Bangalore'),
    ('AnjaliDas', 'anjali.das@example.com', 'anjali626', '9123456708', '21, Ballygunge, Kolkata'),
    ('TarunGhosh', 'tarun.ghosh@example.com', 'tarun727', '9123456709', '99, Sector 15, Noida');

    ''')

    cursor.execute('''
-- Insert Restaurants
INSERT INTO Restaurants (Name, Address, CuisineType, AverageRating) VALUES 
('Punjabi Dhaba', '12, Connaught Place, Delhi', 'North Indian', 4.2),
('Mumbai Masala', '56, Marine Drive, Mumbai', 'Maharashtrian', 4.5),
('Hyderabadi Biryani House', '78, HITEC City, Hyderabad', 'Hyderabadi', 4.8),
('Chennai Express', '34, T. Nagar, Chennai', 'South Indian', 4.3),
('Kolkata Kathi Rolls', '45, Park Street, Kolkata', 'Bengali', 4.6),
('Bangalore Cafe', '89, MG Road, Bangalore', 'Cafe', 4.4);

''')

    cursor.execute('''
-- Insert Menu Items
INSERT INTO Menu (RestaurantID, Name, Description, Price, Quantity, Category) VALUES 
(1, 'Butter Chicken', 'Creamy butter chicken', 350.00, 50, 'Non-Veg'),
(1, 'Paneer Butter Masala', 'Delicious paneer in creamy gravy', 300.00, 40, 'Veg'),
(1, 'Naan', 'Soft Indian bread', 50.00, 100, 'Veg'),
(2, 'Vada Pav', 'Spicy potato fritter in a bun', 40.00, 150, 'Veg'),
(2, 'Chicken Malvani', 'Spicy chicken curry', 400.00, 60, 'Non-Veg'),
(2, 'Poha', 'Flattened rice dish', 60.00, 100, 'Veg'),
(3, 'Hyderabadi Biryani', 'Flavorful biryani with tender meat', 250.00, 80, 'Non-Veg'),
(3, 'Veg Biryani', 'Spiced vegetable biryani', 200.00, 70, 'Veg'),
(3, 'Double Ka Meetha', 'Sweet bread pudding', 150.00, 50, 'Veg'),
(4, 'Masala Dosa', 'Rice crepe with spicy potato filling', 80.00, 100, 'Veg'),
(4, 'Chicken Chettinad', 'Spicy Chettinad chicken curry', 300.00, 40, 'Non-Veg'),
(4, 'Idli Sambhar', 'Steamed rice cakes with lentil soup', 60.00, 120, 'Veg'),
(5, 'Kathi Roll', 'Flatbread roll with filling', 120.00, 90, 'Non-Veg'),
(5, 'Aloo Posto', 'Potato with poppy seeds', 200.00, 60, 'Veg'),
(5, 'Fish Curry', 'Bengali style fish curry', 350.00, 50, 'Non-Veg'),
(6, 'Filter Coffee', 'South Indian filter coffee', 50.00, 200, 'Veg'),
(6, 'Veg Sandwich', 'Grilled vegetable sandwich', 80.00, 100, 'Veg'),
(6, 'Chicken Sandwich', 'Grilled chicken sandwich', 120.00, 80, 'Non-Veg');

''')

    cursor.execute('''
               
INSERT INTO Orders (UserID, RestaurantID, OrderDate) VALUES 
(1, 1, '2024-06-01'),
(2, 2, '2024-06-02'),
(3, 3, '2024-06-03'),
(4, 4, '2024-06-04'),
(5, 5, '2024-06-05'),
(6, 6, '2024-06-06'),
(1, 3, '2024-06-07'),
(2, 1, '2024-06-08'),
(3, 2, '2024-06-09'),
(4, 5, '2024-06-10'),
(5, 6, '2024-06-11'),
(6, 4, '2024-06-12'),
(1, 5, '2024-06-13'),
(2, 3, '2024-06-14'),
(3, 4, '2024-06-15'),
(4, 2, '2024-06-16'),
(5, 1, '2024-06-17'),
(6, 5, '2024-06-18'),
(1, 6, '2024-06-19'),
(2, 4, '2024-06-20'),
(3, 5, '2024-06-21'),
(4, 3, '2024-06-22'),
(5, 2, '2024-06-23'),
(6, 1, '2024-06-24');
''')

    cursor.execute('''
-- Insert Checkout
INSERT INTO Checkout (OrderID, PaymentMethod, PaymentDate, Status, TotalAmount) VALUES 
(1, 'Credit Card', '2024-06-01', 'Completed', 700.00),
(2, 'Debit Card', '2024-06-02', 'Completed', 480.00),
(3, 'UPI', '2024-06-03', 'Completed', 250.00),
(4, 'PayPal', '2024-06-04', 'Completed', 380.00),
(5, 'Credit Card', '2024-06-05', 'Completed', 350.00),
(6, 'Debit Card', '2024-06-06', 'Completed', 170.00),
(7, 'UPI', '2024-06-07', 'Completed', 450.00),
(8, 'Credit Card', '2024-06-08', 'Completed', 300.00),
(9, 'PayPal', '2024-06-09', 'Completed', 440.00),
(10, 'Debit Card', '2024-06-10', 'Completed', 320.00),
(11, 'UPI', '2024-06-11', 'Completed', 250.00),
(12, 'Credit Card', '2024-06-12', 'Completed', 150.00),
(13, 'Debit Card', '2024-06-13', 'Completed', 380.00),
(14, 'PayPal', '2024-06-14', 'Completed', 300.00),
(15, 'UPI', '2024-06-15', 'Completed', 170.00),
(16, 'Credit Card', '2024-06-16', 'Completed', 420.00),
(17, 'Debit Card', '2024-06-17', 'Completed', 250.00),
(18, 'PayPal', '2024-06-18', 'Completed', 300.00),
(19, 'UPI', '2024-06-19', 'Completed', 400.00),
(20, 'Credit Card', '2024-06-20', 'Completed', 220.00),
(21, 'Debit Card', '2024-06-21', 'Completed', 290.00),
(22, 'PayPal', '2024-06-22', 'Completed', 230.00),
(23, 'UPI', '2024-06-23', 'Completed', 380.00),
(24, 'Credit Card', '2024-06-24', 'Completed', 450.00);

''')
    
    cursor.execute('''
-- Insert Reviews
INSERT INTO Review (UserID, RestaurantID, Rating, Comment, ReviewDate) VALUES 
(1, 1, 5, 'Excellent butter chicken!', '2024-06-02'),
(2, 2, 4, 'Vada Pav was tasty but a bit spicy.', '2024-06-03'),
(3, 3, 5, 'The Hyderabadi Biryani is a must-try!', '2024-06-04'),
(4, 4, 3, 'Masala Dosa was good but the service was slow.', '2024-06-05'),
(5, 5, 4, 'Loved the Kathi Roll!', '2024-06-06'),
(6, 6, 5, 'Best filter coffee in town.', '2024-06-07'),
(1, 3, 4, 'Double Ka Meetha was delicious.', '2024-06-08'),
(2, 1, 3, 'Paneer Butter Masala could have been better.', '2024-06-09'),
(3, 2, 5, 'Chicken Malvani was amazing!', '2024-06-10'),
(4, 5, 4, 'Fish Curry was good.', '2024-06-11'),
(5, 6, 5, 'The Chicken Sandwich was perfect.', '2024-06-12'),
(6, 4, 4, 'Idli Sambhar was tasty.', '2024-06-13'),
(1, 5, 5, 'Aloo Posto was delightful.', '2024-06-14'),
(2, 3, 4, 'Veg Biryani was good.', '2024-06-15'),
(3, 4, 3, 'Chicken Chettinad was okay.', '2024-06-16'),
(4, 2, 5, 'Poha was refreshing.', '2024-06-17'),
(5, 1, 4, 'Naan was soft and fluffy.', '2024-06-18'),
(6, 5, 5, 'Best Kathi Roll ever!', '2024-06-19'),
(1, 6, 4, 'Veg Sandwich was tasty.', '2024-06-20'),
(2, 4, 5, 'Masala Dosa was crispy and delicious.', '2024-06-21'),
(3, 5, 4, 'Aloo Posto was great.', '2024-06-22'),
(4, 3, 5, 'Hyderabadi Biryani is always a delight.', '2024-06-23'),
(5, 2, 3, 'Vada Pav was okay.', '2024-06-24'),
(6, 1, 4, 'Butter Chicken was good.', '2024-06-25');

''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_data()
