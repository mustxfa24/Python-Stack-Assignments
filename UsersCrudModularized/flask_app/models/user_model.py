from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL

class User:

    db = 'users_schema'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_user(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);'

        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all_users(cls, data):
        query = 'SELECT * FROM users;'
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
            
        return users
    
    @classmethod
    def get_user_id(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod
    def update_user(cls, data):
        query = 'UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;'

        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM users WHERE id = %(id)s;'
        
        return connectToMySQL(cls.db).query_db(query, data)
