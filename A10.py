import sqlite3

def execute_task_a10():
    # Connect to the SQLite database
    conn = sqlite3.connect("/data/ticket-sales.db")
    cursor = conn.cursor()

    # Query the total sales for "Gold" tickets
    cursor.execute("SELECT SUM(units * price) FROM tickets WHERE type = 'Gold'")
    total_sales = cursor.fetchone()[0]

    # Write the total sales to a new file
    with open("/data/ticket-sales-gold.txt", "w") as file:
        file.write(str(total_sales))

    # Close the database connection
    conn.close()
