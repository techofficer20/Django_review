from django.db import models

# Create your models here.
# 이 부분은 admin 사이트에 보여지는 것임. (단, admin.py와 연결)
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]