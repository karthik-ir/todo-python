from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class task(models.Model):
    title = models.CharField('title', max_length=200)
    description = models.CharField('description', max_length=200)
    create_date = models.DateTimeField('create_date')
    due_date = models.DateTimeField('due_date')
    status = models.BooleanField('done')
    #user_name = models.ForeignKey(User)
   
    def __unicode__(self):
        return self.title
