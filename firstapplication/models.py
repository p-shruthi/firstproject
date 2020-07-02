from django.db import models

# Create your models here.

'''class RandomManager(models.Manager):
    def get_query_set(self):
        return super(RandomManager, self).get_query_set().order_by('?')'''

class project(models.Model):
    name=models.CharField(max_length=300)
    id=models.IntegerField(primary_key=True)
    contact=models.CharField(max_length=300)
    address=models.TextField()

    #objects= models.Manager()
    #randoms=RandomManager()

