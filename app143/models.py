from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Book(models.Model):
	name=models.CharField(max_length=100)
	Author=models.OneToOneField(User)#,related_name='users1')
	def __str__(self):
		return self.name

class MultipleBooks(models.Model):
	name=models.CharField(max_length=100)
	author=models.ForeignKey(User)
	def  __str__(self):
		return self.name
class MultiAuthoeBooks(models.Model):
	name=models.CharField(max_length=100)
	author=models.ManyToManyField(User)
	def  __str__(self):
		return self.name
	
class Student(models.Model):
	user=models.OneToOneField(User)
	age=models.PositiveIntegerField()
	gender=models.BooleanField(choices=((True,'Male'),(False,'Female'),))
	
	address=models.TextField()
	mobileno=models.CharField(max_length=12)
	def __str__(self):
		return self.user.username


	
		