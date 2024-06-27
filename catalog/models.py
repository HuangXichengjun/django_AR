from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Remark(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='input_infos',default='root')
    #一个 User 实例想要访问与其相关联的所有 InputInfo 实例，可以使用 user.input_infos.all()。
    #用于创建两个模型之间的一对多关系。在你提供的代码片段中，user 是一个外键字段，它将当前模型与 Django 内置的 User 模型关联起来
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'"{self.title}" by {self.name}'
    class Meta:
        db_table='remark_db'
