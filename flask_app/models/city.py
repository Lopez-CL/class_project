from flask_app.config.mysqlconnection import connectToMySQL

class City:
    # db_name = "landmarks_schema" # if you want Class variable that holds the schema name
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.mayor = data['mayor']
        self.population = data['population']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        #will connect to a landmarks class
    @classmethod
    def create_city(cls,data):
        query="""
        INSERT INTO cities
        (name, mayor, population)
        VALUES (%(name)s, %(mayor)s, %(population)s);
        """
        return connectToMySQL('landmarks_schema').query_db(query,data)
        
    @classmethod
    def get_all_cities(cls):
        query="""
        SELECT * FROM cities;
        """
        results= connectToMySQL('landmarks_schema').query_db(query)
        print(results)
        all_city_objects=[]
        if len(results) == 0:
            return []
        else:
            for this_city_dictionary in results:
                print(this_city_dictionary)
                this_city_obj = cls(this_city_dictionary)
                all_city_objects.append(this_city_obj)
            return all_city_objects

    @classmethod
    def get_one_city(cls,data):
        query = "SELECT * FROM cities WHERE id = %(id)s";
        results = connectToMySQL('landmarks_schema').query_db(query,data)
        print(results)
        if len(results) == 0:
            return None
        else:
            return cls(results[0])
    
    # Edit one city
    @classmethod
    def edit_city(cls, data):
        query = """
        UPDATE cities SET
        name = %(name)s,
        mayor = %(mayor)s,
        population = %(population)s
        WHERE id = %(id)s;
        """
        return connectToMySQL('landmarks_schema').query_db(query, data)

    # Delete one city
    @classmethod
    def delete_city(cls, data):
        query = "DELETE FROM cities WHERE id = %(id)s;"
        return connectToMySQL('landmarks_schema').query_db(query, data)