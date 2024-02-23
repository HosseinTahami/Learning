from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    age = models.SmallIntegerField()

    def __str__(self):
        return f"{self.id} || {self.name}"

class Car(models.Model):
    brand = models.CharField(max_length=40)
    built_year = models.SmallIntegerField()
    name = models.name = models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.brand} || {self.name}"
    

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user} - {self.title[:20]}'

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    
    def __str__(self):
        return f'{self.user} - {self.question.title[:30]}'