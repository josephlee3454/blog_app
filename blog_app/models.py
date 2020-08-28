from django.db import models

# Create your models here.
class BlogApp(models.Model):
  name = models.CharField(max_length=64)
  author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
  topic = models.CharField(max_length=30, default=('topic'))
  date = models.DateField()
  body = models.TextField(max_length=264)
 

  def __str__(self):
    return self.name