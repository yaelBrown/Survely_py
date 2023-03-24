from django.db import models

class Surveys(models.Model):
  surveyor_user_id = models.IntegerField()
  surveyor_group_id = models.IntegerField()
  survey_name = models.CharField(max_length=255)
  survey_date = models.DateField()
  survey_questions = models.JSONField()
  survey_is_active = models.BooleanField()
  surveyees_text = models.JSONField()
  surveyees_whatsapp = models.JSONField()
  surveyees_email = models.JSONField()

class Survey_Responses(models.Model):
  survey_id = models.IntegerField()
  surveyee_id = models.IntegerField()
  question_id = models.IntegerField()
  response = models.CharField(max_length=255)
  responded_date = models.DateField()
  