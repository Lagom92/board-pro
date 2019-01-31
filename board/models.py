from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=100)
    content1 = models.TextField()
    content2 = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    
class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    checkValue = models.IntegerField()
    content = models.CharField(max_length=300)
    
    