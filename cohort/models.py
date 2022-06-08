from django.db import models

# Create your models here.

class cohort(models.Model):
    ids = models.CharField(max_length=50, verbose_name='ID')
    count = models.IntegerField(verbose_name='Sample')
    tissue = models.CharField(max_length=256, verbose_name='Tissue')
    annotation = models.CharField(max_length=256, verbose_name='Annotation')
    array = models.CharField(max_length=20, verbose_name='Array')

    def __str__(self):
        return "{}-{}-{}".format(self.id, self.sample, self.array)

    class Meta:
        verbose_name = 'Cohorts'
        
        
class GsmInfo(models.Model):
    ids = models.CharField(max_length=256, verbose_name='ID')
    age = models.FloatField(verbose_name='Age')
    gender = models.CharField(max_length=20, verbose_name='Gender')
    source_date = models.CharField(max_length=15, verbose_name='Sourcedate')
    race = models.CharField(max_length=20, verbose_name='Race')
    source = models.CharField(max_length=40, verbose_name='Source')
    group = models.CharField(max_length=40, verbose_name='Group')
    disease = models.CharField(max_length=20, verbose_name='Disease')
    series = models.CharField(max_length=30, verbose_name='Series')

    add_date = models.DateTimeField(auto_now_add=True, verbose_name='Add_date')
    mod_date = models.DateTimeField(auto_now=True, verbose_name="Update_date")

    def __str__(self):
        return "{}-{}-{}".format(self.age, self.gender, self.ids)

    class Meta:
        verbose_name = 'GSM Info'        