from django.db import models

# Create your models here.

CHOICE = (('danger', 'high'), ('warning','normal'), ('primary','low'))

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices=CHOICE
    )
    duedate = models.DateField()

    # 管理画面の表示をタイトルにする
    def __str__(self):
        return self.title

