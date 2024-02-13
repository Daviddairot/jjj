from django.db import models
import re  # Import regular expression module




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
    email = models.EmailField(max_length=254, null=True)
    has_voted = models.BooleanField(default=False)

    def __str__(self):
        return self.matric_number    



class UserVote(models.Model):
    user_profile = models.OneToOneField('UserProfile', on_delete=models.CASCADE)
    email = models.EmailField(default='noemail@example.com')  # or default=''
    president_voted = models.ForeignKey(President, related_name='votes_for_president', on_delete=models.CASCADE, blank=True, null=True)
    vice_president_voted = models.ForeignKey(Vice_President, related_name='votes_for_vice_president', on_delete=models.CASCADE, blank=True, null=True)
    general_secretary_voted = models.ForeignKey(General_Secretary, related_name='votes_for_general_secretary', on_delete=models.CASCADE, blank=True, null=True)
    financial_secretary_voted = models.ForeignKey(Financial_Secretary, related_name='votes_for_financial_secretary', on_delete=models.CASCADE, blank=True, null=True)
    social_director_voted = models.ForeignKey(Social_Director, related_name='votes_for_social_director', on_delete=models.CASCADE, blank=True, null=True)
    technical_director_voted = models.ForeignKey(Technical_Director, related_name='votes_for_technical_director', on_delete=models.CASCADE, blank=True, null=True)
    sports_director_voted = models.ForeignKey(Sports_Director, related_name='votes_for_sports_director', on_delete=models.CASCADE, blank=True, null=True)
    public_relations_officer_voted = models.ForeignKey(Public_Relations_Officer, related_name='votes_for_public_relations_officer', on_delete=models.CASCADE, blank=True, null=True)
    treasurer_voted = models.ForeignKey(Treasurer, related_name='votes_for_treasurer', on_delete=models.CASCADE, blank=True, null=True)
    welfare_director_voted = models.ForeignKey(Welfare_Director, related_name='votes_for_welfare_director', on_delete=models.CASCADE, blank=True, null=True)
    assistant_general_secretary_voted = models.ForeignKey(assistant_general_secretary, related_name='votes_for_assistant_general_secretary', on_delete=models.CASCADE, blank=True, null=True)
    assistant_social_director_voted = models.ForeignKey(assistant_social_director, related_name='votes_for_assistant_social_director', on_delete=models.CASCADE, blank=True, null=True)
    pro1_voted = models.ForeignKey(P_R_O1, related_name='votes_for_pro1', on_delete=models.CASCADE, blank=True, null=True)
    pro2_voted = models.ForeignKey(P_R_O2, related_name='votes_for_pro2', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.user_profile.matric_number} voted for candidates"

