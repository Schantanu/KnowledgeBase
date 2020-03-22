from django.db import models


# Create your models here.
class AppCards(models.Model):
    id = models.IntegerField(db_column='ID', blank=True,
                             primary_key=True)  # Field name made lowercase.
    project = models.CharField(db_column='Project',
                               max_length=100,
                               blank=True,
                               null=True)  # Field name made lowercase.
    page = models.CharField(db_column='Page',
                            max_length=100,
                            blank=True,
                            null=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', blank=True,
                             null=True)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True,
                              null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description',
                                   blank=True,
                                   null=True)  # Field name made lowercase.

    # class Meta:
    # managed = False
    # db_table = 'APP_CARDS'
