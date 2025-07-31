import mysql.connector
from datetime import datetime

# Database connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="railway_db"
    )

# Book a ticket
def book_ticket(user_id, train_id, seat_number):
    conn = connect_db()
    cursor = conn.cursor()

    # Check if seat is already booked
    cursor.execute("""
        SELECT * FROM bookings 
        WHERE train_id = %s AND seat_number = %s AND status = 'booked'
    """, (train_id, seat_number))
    if cursor.fetchone():
        print("❌ Seat already booked.")
        return

    # Insert booking
    cursor.execute("""
        INSERT INTO bookings (user_id, train_id, seat_number, status)
        VALUES (%s, %s, %s, 'booked')
    """, (user_id, train_id, seat_number))
    conn.commit()
    print("✅ Ticket booked successfully.")
    conn.close()

# Cancel a ticket
def cancel_ticket(booking_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE bookings SET status = 'cancelled' 
        WHERE booking_id = %s AND status = 'booked'
    """, (booking_id,))
    if cursor.rowcount == 0:
        print("❌ Booking not found or already cancelled.")
    else:
        conn.commit()
        print("✅ Ticket cancelled.")
    conn.close()

# View bookings for a user
def view_bookings(user_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT b.booking_id, t.train_name, b.seat_number, b.status, b.booking_time
        FROM bookings b
        JOIN trains t ON b.train_id = t.train_id
        WHERE b.user_id = %s
    """, (user_id,))
    bookings = cursor.fetchall()

    print("\n📋 Your Bookings:")
    for booking in bookings:
        print(f"ID: {booking[0]}, Train: {booking[1]}, Seat: {booking[2]}, Status: {booking[3]}, Time: {booking[4]}")
    conn.close()

# Sample usage
if __name__ == "__main__":
    # Replace with actual user_id and train_id from your database
    user_id = 1
    train_id = 101
    seat_number = 5

    book_ticket(user_id, train_id, seat_number)
    view_bookings(user_id)
    cancel_ticket(1)  # Replace with actual booking_id
