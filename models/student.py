class Student:
    def __init__(self, student_id=None, first_name=None, last_name=None, email=None, password=None, class_id=None):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.class_id = class_id

    @staticmethod
    def save(mongo, student_data):
        collection = mongo.db.students
        result = collection.insert_one(student_data)
        return result.inserted_id

    @staticmethod
    def find_by_email(mongo, email):
        collection = mongo.db.students
        return collection.find_one({'email': email})

    @staticmethod
    def find_all(mongo):
        collection = mongo.db.students
        return collection.find()

    @staticmethod
    def update(mongo, student_id, student_data):
        collection = mongo.db.students
        result = collection.update_one({'_id': student_id}, {'$set': student_data})
        return result.modified_count
