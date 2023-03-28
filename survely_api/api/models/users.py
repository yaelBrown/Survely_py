from django.db import models

SERVICE_LEVEL = (
  ("ZERO", "zero")
  ("ONE", "one")
  ("TWO", "two")
  ("ADMIN", "admin")
)
class Users(models.Model):
  email = models.CharField(max_length=255, null=False, unique=True)
  name = models.CharField(max_length=255)
  password = models.CharField(max_length=100, null=False)
  last_login = models.DateField()

class Users_Meta(models.Model):
  user_id = models.IntegerField(null=False)
  last_login = models.DateField()
  created_date = models.DateField()
  service_level = models.enums(SERVICE_LEVEL, null=False)
  surveys_created_count = models.IntegerField(default=0)
  groups_created_count = models.IntegerField(default=0)

class Users_Groups(models.Model):
  user_id = models.IntegerField(null=False)
  groups_id = models.IntegerField(null=False)
  can_read = models.BooleanField(null=False)
  can_create = models.BooleanField(null=False)
  can_delete = models.BooleanField(null=False)
  can_edit = models.BooleanField(null=False)
  can_add_people = models.BooleanField(null=False)
  can_rem_people = models.BooleanField(null=False)
  can_edit_people = models.BooleanField(null=False)