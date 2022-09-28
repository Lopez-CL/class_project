from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL

class Landmark:
    # db_name = "landmarks_schema" # if you want Class variable that holds the schema name
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.year_created = data['year_created']
        self.address = data['address']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        #will add a city link.
    
    @classmethod
    def add_city(cls, data):
        query="""
        INSERT INTO landmarks
        (name, year_created, address, city_id)
        VALUES (%(name)s, %(year_created)s, %(address)s, %(city_id)s;
        """
        return connectToMySQL('landmarks_schema').query_db(query,data)
    @classmethod
    def get_all_landmarks():
        query="""
        SELECT * landmarks FROM landmarks
        JOIN cities 
        ON landmarks.city_id = cities.id;
        """
        results = connectToMySQL('landmarks_schema').query_db(query)
        print(results)
        all_landmark_obkects = []
        if len(results) == 0:
            return None
        else:
            for this_landmark_dictionary in results:
                