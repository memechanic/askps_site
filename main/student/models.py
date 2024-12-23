from django.db import models

class People(models.Model):
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

class Attendance(models.Model):

    class_id = models.IntegerField()
    student_id = models.IntegerField()
    qr_check = models.BooleanField()
    skud_check = models.BooleanField()

    class Meta:
        managed = False
        db_table = '"main"."attendance"'

class Classes(models.Model):

    group_name = models.CharField(max_length=255)
    building_id = models.IntegerField()
    class_number = models.CharField(max_length=50)
    teacher_id = models.IntegerField()
    date = models.DateTimeField()
    subject = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = '"main"."classes"'