# import the function that will return an instance of a connection
from flask_app.config.mysqlconnections import connectToMySQL
from flask import flash
from flask_app import DATABASE

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_user(cls,data):
        query= """
            INSERT INTO dojos (name, location, language, comment)
            VALUES (%(name)s,%(location)s,%(language)s,%(comment)s)
            """
        results = connectToMySQL(DATABASE).query_db(query,data)
        return results
    
    @classmethod
    def show_dojo(cls,data):
        query = """
            SELECT * FROM dojos
            WHERE id = %(id)s
            """
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            dojo_instance = cls(results[0])
            return dojo_instance
        return results
    @staticmethod
    def validate_user(data):
        is_valid = True
        if len(data['name']) < 1:
            flash("Please enter a name")
            is_valid = False
        if len(data['location']) < 2:
            flash("Please select a location")
            is_valid = False
        if len(data['language']) < 2:
            flash("Please select a favorite language")
            is_valid = False    
        if len(data['comment']) < 1:
            flash("Please enter a comment about yourself")
            is_valid = False
        return is_valid