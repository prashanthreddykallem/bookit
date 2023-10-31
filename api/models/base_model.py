import dataclasses
import config

@dataclasses.dataclass
class BaseModel:
    __tablename__ = None
    id: int

    conn = config.get_db()

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def insert(cls, **kwargs) -> int:
        cursor = cls.conn.cursor()

        # Extracting the attributes and values provided
        attributes = list(kwargs.keys())
        values = list(kwargs.values())

        # Formulating the SQL query
        placeholders = ', '.join(['%s'] * len(values))
        columns = ', '.join(attributes)
        query = (f"INSERT INTO {cls.__tablename__} ({columns}) "
                 f"VALUES ({placeholders})")

        # Executing the query
        cursor.execute(query, tuple(values))
        cls.conn.commit()

        # Getting the last inserted ID
        last_inserted_id = cursor.lastrowid

        cursor.close()
        return last_inserted_id

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
    def select_first(cls, **conditions) -> object:
        cursor = cls.conn.cursor()

        # Formulating the SQL query
        if conditions:
            cond_str = ' AND '.join([f"{key} = %s" for key in conditions])
            query = (f"SELECT * FROM {cls.__tablename__} WHERE {cond_str} "
                     f"LIMIT 1")
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

        return None

    @classmethod
    def delete(cls, **conditions) -> None:
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

    @classmethod
    def update(cls, conditions: dict, new_values: dict) -> None:
        cursor = cls.conn.cursor()

        # Formulating the SQL query
        if not conditions:
            raise ValueError(
                "Conditions must be provided for the update operation."
            )

        # Formulating the SET part of the query
        set_str = ', '.join([f"{key} = %s" for key in new_values])

        # Formulating the WHERE part of the query
        condition_str = ' AND '.join([f"{key} = %s" for key in conditions])

        query = (
                f"UPDATE {cls.__tablename__} SET {set_str} "
                f"WHERE {condition_str}"
            )

        # Combining new values and conditions for the execute method
        values = list(new_values.values()) + list(conditions.values())

        # Executing the query
        cursor.execute(query, tuple(values))
        cls.conn.commit()
        cursor.close()

    def close_connection(self) -> None:
        if self.conn.is_connected():
            self.conn.close()
