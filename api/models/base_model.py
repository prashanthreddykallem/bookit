import config

class BaseModel:
    __tablename__ = None
    conn = config.get_db()

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def insert(self) -> int:
        cursor = self.conn.cursor()

        # Extracting the attributes and values of the instance
        attributes = [attr for attr in self.__dict__ if not attr.startswith('_')]
        values = [getattr(self, attr) for attr in attributes]

        # Formulating the SQL query
        placeholders = ', '.join(['%s'] * len(values))
        columns = ', '.join(attributes)
        query = f"INSERT INTO {self.__tablename__} ({columns}) VALUES ({placeholders})"

        # Executing the query
        cursor.execute(query, tuple(values))
        self.conn.commit()

        # if your table has an auto-incrementing primary key.
        self.id = cursor.lastrowid

        cursor.close()
        return self.id

    @classmethod
    def select(cls, **conditions) -> list:
        cursor = cls.conn.cursor()

        # Formulating the SQL query
        if conditions:
            condition_str = ' AND '.join([f"{key} = %s" for key in conditions])
            query = f"SELECT * FROM {cls.__tablename__} WHERE {condition_str}"
            cursor.execute(query, tuple(conditions.values()))
        else:
            query = f"SELECT * FROM {cls.__tablename__}"
            cursor.execute(query)

        # Fetching the results
        results = cursor.fetchall()

        # mapping the results into class instances
        instances = []
        columns = [desc[0] for desc in cursor.description]
        for row in results:
            instance = cls()
            for attr, value in zip(columns, row):
                setattr(instance, attr, value)
            instances.append(instance)

        return instances
    
    @classmethod
    def select_first(cls, **conditions):
        cursor = cls.conn.cursor()

        # Formulating the SQL query
        if conditions:
            condition_str = ' AND '.join([f"{key} = %s" for key in conditions])
            query = f"SELECT * FROM {cls.__tablename__} WHERE {condition_str} LIMIT 1"
            cursor.execute(query, tuple(conditions.values()))
        else:
            query = f"SELECT * FROM {cls.__tablename__} LIMIT 1"
            cursor.execute(query)

        # Fetching the result and mapping it to a class instance
        row = cursor.fetchone()
        if row:
            instance = cls()
            columns = [desc[0] for desc in cursor.description]
            for attr, value in zip(columns, row):
                setattr(instance, attr, value)
            return instance
        else:
            return None
    
    @classmethod
    def delete(cls, **conditions):
        cursor = cls.conn.cursor()

        # Formulating the SQL query
        if conditions:
            condition_str = ' AND '.join([f"{key} = %s" for key in conditions])
            query = f"DELETE FROM {cls.__tablename__} WHERE {condition_str}"
            cursor.execute(query, tuple(conditions.values()))
        else:
            # If no conditions are provided, delete all records
            query = f"DELETE FROM {cls.__tablename__}"
            cursor.execute(query)

        cls.conn.commit()
        cursor.close()

    def close_connection(self) -> None:
        if self.conn.is_connected():
            self.conn.close()