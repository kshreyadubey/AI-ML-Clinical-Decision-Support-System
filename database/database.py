import sqlite3

DATABASE_NAME = "database/users.db"


# ==========================================
# CONNECT DATABASE
# ==========================================

def connect_db():
    return sqlite3.connect(DATABASE_NAME)


# ==========================================
# CREATE USERS TABLE
# ==========================================

def create_database():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT UNIQUE,

        password TEXT,

        fullname TEXT,

        mobile TEXT,

        role TEXT,

        registered INTEGER DEFAULT 0

    )
    """)

    conn.commit()
    conn.close()


# ==========================================
# INSERT OFFICIAL USERS
# ==========================================

def insert_default_users():

    users = [

        ("dr_srikant", "Doctor@2026", "", "", "Doctor", 0),
        ("deepika", "Yoga@2026", "", "", "Yoga Therapist", 0),
        ("diet01", "Diet@2026", "", "", "Dietitian", 0),
        ("acu01", "Acu@2026", "", "", "Acupuncture Specialist", 0),
        ("patient01", "Patient@2026", "", "", "Patient", 0),
        ("shreya", "Shreya@2026", "", "", "Project Developer", 0)

    ]

    conn = connect_db()
    cursor = conn.cursor()

    for user in users:

        cursor.execute("""

        INSERT OR IGNORE INTO users
        (username,password,fullname,mobile,role,registered)

        VALUES (?,?,?,?,?,?)

        """, user)

    conn.commit()
    conn.close()


# ==========================================
# CHECK USERNAME & PASSWORD
# ==========================================

def check_login(username, password):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM users

    WHERE username=? AND password=?

    """, (username, password))

    user = cursor.fetchone()

    conn.close()

    return user


# ==========================================
# GET USER
# ==========================================

def get_user(username):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM users

    WHERE username=?

    """, (username,))

    user = cursor.fetchone()

    conn.close()

    return user


# ==========================================
# CHECK REGISTRATION
# ==========================================

def is_registered(username):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT registered

    FROM users

    WHERE username=?

    """, (username,))

    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]

    return 0


# ==========================================
# COMPLETE REGISTRATION
# ==========================================

def register_user(username, fullname, mobile):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""

    UPDATE users

    SET fullname=?,
        mobile=?,
        registered=1

    WHERE username=?

    """, (fullname, mobile, username))

    conn.commit()
    conn.close()


# ==========================================
# INITIALIZE DATABASE
# ==========================================

if __name__ == "__main__":

    create_database()
    insert_default_users()

    print("✅ Database Created Successfully")