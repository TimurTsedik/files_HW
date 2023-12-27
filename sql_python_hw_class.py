import psycopg2


class Client:
    def __init__(self, name, surname, email, phone=None):
        """
        Initializes a new instance of the class with the specified name, surname, email, and optional phone number.

        Parameters:
            name (str): The name of the client.
            surname (str): The surname of the client.
            email (str): The email address of the client.
            phone (str, optional): The phone number of the client. Defaults to None.

        Returns:
            None

        Raises:
            Exception: If an error occurs while saving the client information to the database.

        """
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = [phone] if phone else []
        self.saved_to_db = False
        try:
            with psycopg2.connect(database="netology_hw", user="postgres", password="postgres") as conn:
                with conn.cursor() as cur:
                    cur.execute("""
                    INSERT INTO clients
                    (name, surname, email) 
                    VALUES(%s, %s, %s) 
                    RETURNING id;
                    """, (self.name, self.surname, self.email))
                    self.id = cur.fetchone()[0]
                    if self.phone:
                        cur.execute("""
                        INSERT INTO client_phones
                        (phone_nr, client) 
                        VALUES(%s, %s);
                        """, (self.phone[0], self.id))
                    conn.commit()
                    self.saved_to_db = True
        except Exception as ex:
            if ex.diag.sqlstate == '23505':
                print('Уже существует клиент с такими данными')
            elif ex.diag.sqlstate == '23501':
                print('Уже существует телефон с таким номером')
            else:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                print(message)

    def add_phone(self, phone):
        """
        Adds a phone number to the client's list of phone numbers and saves it to the database.

        Parameters:
            phone (str): The phone number to be added.

        Returns:
            None
        """
        if self.saved_to_db:
            self.phone.append(phone)
            try:
                with psycopg2.connect(database="netology_hw", user="postgres", password="postgres") as conn:
                    with conn.cursor() as cur:
                        cur.execute("""
                        INSERT INTO client_phones
                        (phone_nr, client) 
                        VALUES(%s, %s);
                        """, (phone, self.id))
                        conn.commit()
            except Exception as ex:
                # if ex.pgcode == '23505':
                #     print('Уже существует телефон с таким номером')
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                print(message)
        else:
            print('Такой клиент не сохранен в базе данных')
    def edit(self, name, surname, email):
        """
        Edits the client's name, surname, and email.

        Args:
            name (str): The new name of the client.
            surname (str): The new surname of the client.
            email (str): The new email of the client.

        Returns:
            None

        Raises:
            Exception: If an error occurs while updating the client's information in the database.

        Note:
            - If the client is already saved in the database, the function updates the client's information in the database.
            - If the client is not saved in the database, the function prints a message stating that the client is not saved in the database.
            - If an exception of type `psycopg2.IntegrityError` occurs with the error code '23505', it means that a client with the same information already exists in the database, and the function prints a message stating that a client with the same information already exists.

        """
        if self.saved_to_db:
            self.name = name
            self.surname = surname
            self.email = email
            try:
                with psycopg2.connect(database="netology_hw", user="postgres", password="postgres") as conn:
                    with conn.cursor() as cur:
                        cur.execute("""
                        UPDATE clients
                        SET name = %s, surname = %s, email = %s
                        WHERE id = %s;
                        """, (self.name, self.surname, self.email, self.id))
                        conn.commit()
            except Exception as ex:
                if ex.pgcode == '23505':
                    print('Уже существует клиент с такими данными')
                # template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                # message = template.format(type(ex).__name__, ex.args)
                # print(message)
        else:
            print('Такой клиент не сохранен в базе данных')
    def delete_phone(self, phone):
        """
        Deletes a phone number from the client's phone list and from the database.

        Args:
            phone (str): The phone number to be deleted.

        Returns:
            None

        Raises:
            None
        """
        if self.saved_to_db:
            self.phone.remove(phone)
            with psycopg2.connect(database="netology_hw", user="postgres", password="postgres") as conn:
                with conn.cursor() as cur:
                    cur.execute("""
                    DELETE FROM client_phones
                    WHERE client = %s AND number = %s;
                    """, (self.id, self.phone))
                    conn.commit()
        else:
            print('Такой клиент не сохранен в базе данных')
    def delete(self):
        if self.saved_to_db:
            """
            Deletes the client from the database if it has been saved, otherwise prints a message.
            """
            with psycopg2.connect(database="netology_hw", user="postgres", password="postgres") as conn:
                with conn.cursor() as cur:
                    cur.execute("""
                    DELETE FROM clients
                    WHERE id = %s;
                    """, (self.id,))
                    conn.commit()
        else:
            print('Такой клиент не сохранен в базе данных')
    def search(self, name, surname, email=None, phone=None):
        if self.saved_to_db:
            """
            Searches for a client in the database based on their name, surname, email, or phone number.

            Args:
                name (str): The name of the client.
                surname (str): The surname of the client.
                email (str, optional): The email of the client. Defaults to None.
                phone (str, optional): The phone number of the client. Defaults to None.

            Returns:
                int: The ID of the client found in the database.

            Raises:
                None

            Side Effects:
                - Executes SQL queries to search for the client in the database.
                - Prints a message if the client is not found in the database.
            """
            with psycopg2.connect(database="netology_hw", user="postgres", password="postgres") as conn:
                with conn.cursor() as cur:
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
        else:
            print('Такой клиент не сохранен в базе данных')

# with psycopg2.connect(database="netology_hw", user="postgres", password="postgres") as conn:
#     with conn.cursor() as cur:
#         create_tables(conn)
client1 = Client('Ivana', 'Ivanova', 'xOuK22z@example.com', phone='124567890')
client1.add_phone('12345678912')
# client1.edit('Petr', 'Petrov', 'xOu2Kz@example.com')
# client1.delete_phone()
# client1.delete()
# client1.search()
