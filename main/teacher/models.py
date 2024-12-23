from django.db import models

class People(models.Model):
    id = models.IntegerField(primary_key=True)
    fio = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    group_name = models.CharField(max_length=255)
    isstudent = models.BooleanField()
    isteacher = models.BooleanField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = '"main"."people"'