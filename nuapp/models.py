from django.db import models




class President(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='candidate_pics/')
    department = models.CharField(max_length=200)
    level = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Vice_President(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='candidate_pics/')
    department = models.CharField(max_length=200)
    level = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return self.name
    
class General_Secretary(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='candidate_pics/')
    department = models.CharField(max_length=200)
    level = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return self.name
    
class Financial_Secretary(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='candidate_pics/')
    department = models.CharField(max_length=200)
    level = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Social_Director(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='candidate_pics/')
    department = models.CharField(max_length=200)
    level = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Technical_Director(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='candidate_pics/')
    department = models.CharField(max_length=200)
    level = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Sports_Director(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='candidate_pics/')
    department = models.CharField(max_length=200)
    level = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Public_Relations_Officer(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='candidate_pics/')
    department = models.CharField(max_length=200)
    level = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

class Treasurer(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='candidate_pics/')
    department = models.CharField(max_length=200)
    level = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Welfare_Director(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='candidate_pics/')
    department = models.CharField(max_length=200)
    level = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class P_R_O1(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='candidate_pics/')
    department = models.CharField(max_length=200)
    level = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class P_R_O2(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='candidate_pics/')
    department = models.CharField(max_length=200)
    level = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class assistant_general_secretary(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='candidate_pics/')
    department = models.CharField(max_length=200)
    level = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class assistant_social_director(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='candidate_pics/')
    department = models.CharField(max_length=200)
    level = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

class UserProfile(models.Model):
    matric_number = models.CharField(max_length=20, null=True)
    has_voted = models.BooleanField(default=False)

    def __str__(self):
        return self.matric_number