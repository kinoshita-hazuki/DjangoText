from django.db import models

class EmployeeManager(models.Manager):
    def find_veteran(self):
        return self.filter(no__lt=3000)

    def find_by_name_like_prefix(self, name):
        return self.filter(name__icontains=name)
