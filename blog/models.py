from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): #defines our models  Class indicates defining an object 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()  #Note that every line of code is indented
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): # Method to publish the post
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title  #return a string with the post title