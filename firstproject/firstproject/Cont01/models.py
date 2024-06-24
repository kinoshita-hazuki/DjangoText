from django.db import models

class Employee(models.Model):
    no = models.IntegerField(primary_key=True)  # 社員番号
    name = models.CharField(max_length=255)  # 社員氏名
    salary = models.IntegerField()  # 給与額

    def __str__(self):
        return self.name

class Department(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Employee(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    salary = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
# Create your models here.
