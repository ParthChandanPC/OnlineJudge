from unittest import result
from django.db import models
from django.contrib.auth.models import AbstractUser
from froala_editor.fields import FroalaField

# Create your models here.

def check(text):
        if text.upper() != 'SOLVED' and text.upper() != 'UNSOLVED':
            raise Exception('Status must be either Solved or Unsolved')

def score_check(score):
    if score < 0 :
        raise Exception('Score must be greter than 0')

class User(AbstractUser):
    email = models.EmailField(unique=True)
    score = models.FloatField(default=0, validators=[score_check])
    solved = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Problem(models.Model):
    class Meta:
        ordering = ['-date_created']
    title = models.CharField(max_length=300)
    description = FroalaField()
    status = models.CharField(max_length=10, default='Unsolved',validators=[check,])
    time_limit = models.IntegerField(default=1)
    memory_limit = models.IntegerField(default=128)
    score = models.FloatField(default=0, validators=[score_check])
    # user = models.ManyToManyField(User)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class TestCases(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    input = FroalaField()
    output = FroalaField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.problem.title

class Submissions(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=200)
    