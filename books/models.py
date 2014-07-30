from django.db import models

# Create your models here.
class Author(models.Model):
	def __unicode__(self):
		return self.name.decode('utf8')
	name = models.CharField(max_length=100)
	email = models.EmailField()
class Book(models.Model):
	def __unicode__(self):
		return self.title.decode('utf8')
	title = models.CharField(max_length=200)
	author = models.ForeignKey(Author)
	introduction = models.TextField()
