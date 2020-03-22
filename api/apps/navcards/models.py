from django.db import models
# Create your models here.


class NavCards(models.Model):
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
    #     managed = False
    #     db_table = 'APP_CARDS'


# class Recipe(models.Model):
#     DIFFICULTY_LEVELS = (
#         ('Easy', 'Easy'),
#         ('Medium', 'Medium'),
#         ('Hard', 'Hard'),
#     )
#     name = models.CharField(max_length=120)
#     ingredients = models.CharField(max_length=400)
#     picture = models.FileField()
#     difficulty = models.CharField(choices=DIFFICULTY_LEVELS, max_length=10)
#     prep_time = models.PositiveIntegerField()
#     prep_guide = models.TextField()

#     def __str_(self):
#         return "Recipe for {}".format(self.name)