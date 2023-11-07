from django.db import models


class Category(models.Model):
     title = models.CharField(max_length=50)

     def __str__(self):
          return self.title


class Tag(models.Model):
     title = models.CharField(max_length=50)

     def __str__(self):
          return self.title
     

class Author(models.Model):
     full_name = models.CharField(max_length=60)
     bio = models.CharField(max_length=256)
     img = models.ImageField(upload_to='author')
     top = models.IntegerField(default=0)


     def __str__(self):
          return self.full_name

class Banner(models.Model):
     title = models.CharField(max_length=60)
     text = models.CharField(max_length=256)
     url = models.CharField(max_length=100)

     def __str__(self):
          return self.title


class Post(models.Model):
     title = models.CharField(max_length=100)
     mini_text = models.CharField(max_length=256)
     text = models.TextField()
     img = models.ImageField(upload_to='post')
     
     tag = models.ManyToManyField(Tag)
     author = models.ForeignKey(Author, on_delete=models.CASCADE)
     category = models.ForeignKey(Category, on_delete=models.CASCADE)

     fuature = models.IntegerField(default=0)
     popular = models.IntegerField(default=0)

     count = models.IntegerField(default=0)
     create_at = models.DateTimeField(auto_now_add=True)
     update_at = models.DateTimeField(auto_now=True)

     def __str__(self):
          return self.title
     



