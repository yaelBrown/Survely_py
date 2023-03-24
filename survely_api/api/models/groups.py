from django.db import models

class Groups(models.Model):
  name = models.CharField(max_length=100)
  admin_id = models.IntegerField()

class Groups_Meta(models.Model):
  groups_id = models.IntegerField()
  created_date = models.DateField()
  