from django.db import models
from rest_framework import serializers

# class DeliveryInfo(models.Model):
#   detail = models.CharField(db_column='Delivery', max_length=50, blank=True, null=False, primary_key=True)  # Field name made lowercase.
#   customer = models.CharField(db_column='Customer', max_length=250, blank=True, null=True)  # Field name made lowercase.
#   delivery_date = models.DateField(db_column='Delivery Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

#   class Meta:
#       managed = False
#       db_table = 'BI_DELIVERY_INFO'


class CRUD(models.Model):
    class Meta:
        db_table = 'APP_WQMT'

    delivery = models.PositiveIntegerField(db_column='Delivery')
    # issue_category = models.CharField(choices=issue_category, max_length=200, db_column = 'Issue Category')
    issue_category = models.CharField(max_length=200,
                                      db_column='Issue Category')
    issue = models.CharField(max_length=200, db_column='Issue')
    detail = models.TextField(db_column='Detail')
    created_at = models.DateTimeField(auto_now_add=True,
                                      db_column='Create Datetime')
    updated_at = models.DateTimeField(auto_now=True,
                                      db_column='Update Datetime')
    # score = models.CharField(max_length=50, db_column = 'Score')

    # def calc_score(self):
    #   "Returns Score as More or Less"
    #   if self.delivery < 90000:
    #     return "Less"
    #   elif self.delivery > 90000:
    #     return "More"
    #   else:
    #     return "NA"

    # def save(self, *args, **kwargs):
    #   self.score = self.calc_score()
    #   super(WQMT, self).save(*args, **kwargs)
