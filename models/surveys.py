from config.mysqlconnection import connectToMySQL

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
#     @classmethod
#     def get_all(cls):
#         query= "SELECT * FROM users;"
#         result= connectToMySQL('users_schema').query_db(query)
#         users=[]
#         for user in result:
#             users.append(cls(user))
#         return users
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( name , location , language , comment , created_at, updated_at ) VALUES ( %(name)s , %(location)s , %(language)s , %(comment)s , NOW() , NOW() );"
        return connectToMySQL('dojo_survey_schema').query_db( query, data )
    #     @classmethod
    #     def delete(cls, data):
    #         query = "DELETE FROM users WHERE id = (%(id)s);"
    #         return connectToMySQL('users_schema').query_db(query, data)
    #     @classmethod
    #     def lastIndex(cls):
    #         query="SELECT * FROM users WHERE id=(SELECT max(id) FROM users);"
    #         user=connectToMySQL('users_schema').query_db(query)
    #         return user
    #     @classmethod
    #     def update(cls, data):
    #         query = "UPDATE users SET email = %(email)s, first_name=%(fname)s, last_name=%(lname)s WHERE id = %(id)s;"
    #         return connectToMySQL('users_schema').query_db( query, data )