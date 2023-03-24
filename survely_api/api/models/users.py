from django.db import models

class Users(models.Model):
  email = models.CharField(max_length=100)
  name = models.CharField(max_length=255)
  password = models.CharField(max_length=100)
  last_login = models.DateField()

class Users_Meta(models.Model):
  user_id = models.IntegerField()
  last_login = models.DateField()
  created_date = models.DateField()
  service_level = models.enums()
  surveys_created_count = models.IntegerField()
  groups_created_count = models.IntegerField()

class Users_Groups(models.Model):
  user_id = models.IntegerField()
  groups_id = models.IntegerField()
  can_read = models.BooleanField()
  can_created = models.BooleanField()
  can_edit = models.BooleanField()
  can_add_people = models.BooleanField()
  can_rem_people = models.BooleanField()
  can_edit_people = models.BooleanField()