from django.db import models

class Surveys(models.Model):
  surveyor_user_id = models.IntegerField()
  surveyor_group_id = models.IntegerField()
  survey_name = models.CharField(max_length=255, null=False)
  survey_date = models.DateField()
  survey_is_active = models.BooleanField(default=False)

class Survey_Questions(models.Model):
  survey_id = models.IntegerField(null=False)
  question = models.TextField(null=False)
  question_order = models.IntegerField(null=False)

class Survey_Responses(models.Model):
  survey_id = models.IntegerField()
  surveyee_id = models.IntegerField()
  question_id = models.IntegerField()
  response = models.CharField(max_length=255)
  responded_date = models.DateField()

class Surveyees(models.Model):
  path = models.CharField(max_length=50, null=False)
  survey_id = models.IntegerField(null=False)
  surveyee_mobile = models.IntegerField()
  surveyee_whatsapp = models.IntegerField()
  surveyee_email = models.IntegerField()

class Surveyee_Lists(models.Model):
  surveyor_user_id = models.IntegerField(null=False)
  survey_group_id = models.IntegerField()
  surveyee_text = models.JSONField()
  surveyee_whatsapp = models.JSONField()
  surveyee_email = models.JSONField()
  