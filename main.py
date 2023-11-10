import streamlit as st
import psycopg2


def pq_connect(field1, field2, field3):
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host="your_host",
        database="your_database",
        user="your_user",
        password="your_password",
    )
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS data (
            id SERIAL PRIMARY KEY,
            field1 TEXT,
            field2 TEXT,
            field3 TEXT
        )
    """
    )

    # Insert data into the table
    cursor.execute(
        """
        INSERT INTO data (field1, field2, field3)
        VALUES (%s, %s, %s)
    """,
        (field1, field2, field3),
    )
    conn.commit()

    # Close the database connection
    cursor.close()
    conn.close()
    return True


def main():
    st.title("Testing streamlit")

    # Get user input
    field1 = st.text_input("Field 1")
    field2 = st.text_input("Field 2")
    field3 = st.text_input("Field 3")
    if st.button("print fields"):
        st.write(field1, field2, field3)


if __name__ == "__main__":
    main()
