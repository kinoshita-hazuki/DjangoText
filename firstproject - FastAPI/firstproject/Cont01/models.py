from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

class Employee(models.Model):
    no = models.IntegerField(primary_key=True)  # 社員番号
    name = models.CharField(max_length=255)  # 社員氏名
    salary = models.IntegerField()  # 給与額

    def __str__(self):
        return self.name
    
class EmployeeManager(models.Manager):
    def find_veteran(self):
        return self.filter(no__lt=3000)
    
    def find_by_name_like_prefix(self, name):
        return self.filter(name__icontains=name)

class Department(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Employee(models.Model):
    no = models.IntegerField(
        primary_key=True,
        validators=[
           MinValueValidator(1000, message=_("1000以上の数値で入力してください")) 
        ]
    )
    name = models.CharField(max_length=255)
    salary = models.IntegerField(validators=[MinValueValidator(0, "給与額の入力は必須です")])
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    dept_no = models.IntegerField(default=101)

    def __str__(self):
        return self.name
    
    def clean(self):
        if self.no < 1000:
            raise ValidationError("社員番号は1000以上の数値で入力してください")
        if not self.name:
            raise ValidationError("氏名の入力は必須です")
        if self.salary is None:
            raise ValidationError("給与額の入力は必須です")
    
class Department2(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

class Employee2(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    salary = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    objects = EmployeeManager()
# Create your models here.

class CustomUser(AbstractUser):
    pass  

class UserBean(models.Model):
    id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name