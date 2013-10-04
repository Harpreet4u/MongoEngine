from django.db import models
from mongoengine import *
from mongoengine.django.auth import User

class Users(Document):
	id = ReferenceField(User, primary_key=True)
	solved_questions = ListField(ObjectIdField())
	attempted_questions = ListField(ObjectIdField())
	score = IntField()
	

class Problems(Document):
	problem_name = StringField(max_length=100)
	problem_description = StringField()
	problem_input = StringField()
	problem_output = StringField()
	problem_sample_input = StringField()
	problem_sample_output = StringField()
	problem_input_file = FileField()
	problem_output_file = FileField()
	problem_points = IntField()
	successful_submissions = ListField(ObjectIdField())
	unsuccessful_submissions = ListField(ObjectIdField())




