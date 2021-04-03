from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class ClientProfile(models.Model):
    fullName = models.CharField(max_length=50,blank=False )
    address1 = models.CharField(max_length=100, blank=False, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=False)
    # state = models.CharField(max_length=2, blank=False)
   # zipCode = models.CharField(max_length =9, blank=False, validators=[MinLengthValidator(5)])

    

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name
