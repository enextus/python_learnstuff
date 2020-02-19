from django.db import models

# Create your models here.
# jeder Klasse entspricht einer Tabelle in der DB
# Etnitäten: "Frage" (Frage im Forum) - text
#      "Idee" (Idee oder Antwort)  - text

class Question(models.Model):
    ''' Ein Question-Obj, entspricht einer Frage
    '''
    text = models.CharField(max_length=100)
    author=models.CharField(max_length=20)
    date=models.DateTimeField()

    def __str__(self):
        return f'{self.author} fragt: {self.text}'

class Idea(models.Model):
    ''' Ein Idea-Obj, entspricht einer Idee
    '''
    text=models.CharField(max_length=200)
    date=models.DateTimeField()
    question=models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
