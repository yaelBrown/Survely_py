from django.db import models

class Groups(models.Model):
  name = models.CharField(max_length=255, null=False)
  admin_id = models.IntegerField(null=False)

class Groups_Meta(models.Model):
  groups_id = models.IntegerField(null=False)
  created_date = models.DateField()
  