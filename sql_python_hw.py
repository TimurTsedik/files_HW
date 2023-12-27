import psycopg2


def create_tables(conn):
    conn.cursor().execute("""
    DROP TABLE IF EXISTS client_phones;
    DROP TABLE IF EXISTS clients;
    """)
    conn.cursor().execute("""
        CREATE TABLE IF NOT EXISTS clients(
            id SERIAL PRIMARY KEY,
            name VARCHAR(40) NOT NULL,
            surname VARCHAR(40) NOT NULL,
            email VARCHAR(40) NOT NULL UNIQUE
        );
        """)
    conn.cursor().execute("""
        CREATE TABLE IF NOT EXISTS client_phones(
            phone_nr varchar(20) NOT NULL,
            client INTEGER NOT NULL REFERENCES clients(id)
        );
        """)
    conn.commit()


def add_client(conn, cur, name, surname, email, phone=None):
    try:
        cur.execute("""
        INSERT INTO clients
        (name, surname, email) 
        VALUES(%s, %s, %s) 
        RETURNING id;
        """, (name, surname, email))
        cli_id = cur.fetchone()
        if phone:
            cur.execute("""
            INSERT INTO client_phones
            (phone_nr, client) 
            VALUES(%s, %s);
            """, (phone, cli_id[0]))
        conn.commit()

    except Exception as ex:
        if ex.pgcode == '23505':
            print('Уже существует клиент с такими данными')
        # template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        # message = template.format(type(ex).__name__, ex.args)
        # print(message)


def add_phone(conn, cur, client_id, phone):
    cur.execute("""
    INSERT INTO client_phones
    (number, client) 
    VALUES(%s, %s);
    """, (phone, client_id))
    conn.commit()


def client_edit(conn, cur, name, surname, email):
    cur.execute("""
    UPDATE clients
    SET name = %s, surname = %s, email = %s
    WHERE id = %s;
    """, (name, surname, email))
    conn.cursor().commit()


def phone_delete(conn, cur, client_id, phone):
    cur.execute("""
    DELETE FROM client_phones
    WHERE client = %s AND number = %s;
    """, (client_id, phone))
    conn.cursor().commit()


def client_search(cur, name, surname, phone=None, email=None):
    try:
        if phone:
            cur.execute("""
            SELECT id from clients c
            JOIN client_phones cp ON c.id = cp.client
            WHERE cp.phone_nr = %s ;
            """, (phone,))
        elif email:
            cur.execute("""
            SELECT id FROM clients
            WHERE email = %s and clients.name = %s and clients.surname = %s;
            """, (email, name, surname))
        return cur.fetchall()[0][0]
    except:
        return "Ничего не найдено"


with psycopg2.connect(database="netology_hw", user="postgres", password="postgres") as conn:
    with conn.cursor() as cur:
        create_tables(conn)
        add_client(conn, cur, 'Ivan', 'Ivanov', 'xO25uK22z@example.com', '1234567890')
        add_client(conn, cur, 'Petr', 'Petrov', 'xOu2Kz@example.com')
        print(client_search(cur, 'Ivan', 'Ivanov', phone='1234567890'))
        print(client_search(cur, 'Petr', 'Petrov', email='xOu2Kz@example.com'))
