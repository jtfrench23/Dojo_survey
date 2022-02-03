from config.mysqlconnection import connectToMySQL
from flask import flash

#class model for controller
class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name=data['name']
        self.location= data['location']
        self.language=data['language']
        self.comment=data['comment']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    @classmethod
    def get_all(cls):
        query= "SELECT * FROM surveys;"
        result= connectToMySQL('dojo_survey_schema').query_db(query)
        surveys=[]
        for user in result:
            surveys.append(cls(user))
        return surveys
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( name , location , language , comment  ) VALUES ( %(name)s , %(location)s , %(language)s , %(comment)s);"
        return connectToMySQL('dojo_survey_schema').query_db( query, data )
    @staticmethod
    def validate_survey(survey):
        is_valid = True # we assume this is true
        if len(survey['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(survey['location']) < 3:
            flash("location must be at least 3 characters.")
            is_valid = False
        # if int(survey['language']) < 3:
        #     flash("language must be selected")
        #     is_valid = False
        return is_valid