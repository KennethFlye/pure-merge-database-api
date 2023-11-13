import json

import psycopg2


class DBConnection:

    @classmethod
    def from_json(cls):  # Am using json here so we can easily replace it later, if needed
        # Parse the JSON data
        json_data = ('{"dbname": "the name of the db, i cant remember",'
                     ' "user": "some user name", '
                     '"password": "password1", '
                     '"host": "localhost", '
                     '"port": "5432"}')

        data = json.loads(json_data)

        # Create an instance of the class from the values above
        return cls(
            dbname=data.get('dbname', ''),
            user=data.get('user', ''),
            password=data.get('password', ''),
            host=data.get('host', ''),
            port=data.get('port', '')
        )

    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print("Connected to the database.")
        except psycopg2.Error as e:
            print(f"Error: {e}")

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            print("Disconnected from the database.")

    def execute_query(self, query, params=None):  # Executes query safely (i hope)
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            result = cursor.fetchall()
            cursor.close()
            return result
        except psycopg2.Error as e:
            print(f"Error executing query: {e} \n \"{query}\"")
        finally:
            if cursor is not None:
                cursor.close()
