from django.db import models

# Create your models here.

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()

    # 管理画面の表示をタイトルにする
    def __str__(self):
        return self.title

