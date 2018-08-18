class Users:
    def __init__(self, first_name, last_name, username, email, password, confirm_password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password =password
        self.confirm_password = confirm_password

users = []

class Question():
    def __init__(self, question_id, username,question):
        self.question_id = question_id
        self.username = username
        self.question = question

        def get_question_id(self):
            return self.question_id


        def get_username(self):
            return self.username

        def get_question(self):
            return self.question

questions =[]