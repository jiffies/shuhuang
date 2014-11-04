from django.db import models

# Create your models here.
class Author(models.Model):
        def __unicode__(self):
                return self.name.decode('utf8')
        name = models.CharField(max_length=100)
        email = models.EmailField()

class Category(models.Model):
    name = models.CharField(max_length=50)
    superclass = models.ForeignKey('self',null=True,blank=True)

class Source(models.Model):
    name = models.CharField(max_length=30)

        
class Book_Source(models.Model):
    book = models.ForeignKey('Book')
    source = models.ForeignKey(Source)
    book_number = models.IntegerField()
    url = models.URLField()

class Keyword(models.Model):
    content = models.CharField(max_length=20)

class Book(models.Model):
        def __unicode__(self):
                return self.title.decode('utf8')
        category = models.ForeignKey(Category)
        sources = models.ManyToManyField(Source,through="Book_Source")
        cover = models.TextField()
        title = models.CharField(max_length=200)
        author = models.ForeignKey(Author)
        introduction = models.TextField()
        keywords = models.ManyToManyField(Keyword)
        startTime = models.DateField()
        completeTime = models.DateField(default=None) 
        wordcount = models.IntegerField(default=0)
