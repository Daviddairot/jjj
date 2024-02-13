from django.contrib import admin
from .models import President, UserProfile, Vice_President, General_Secretary, Financial_Secretary, Social_Director, Technical_Director, Sports_Director, Public_Relations_Officer, Treasurer, Welfare_Director, P_R_O1, P_R_O2, assistant_general_secretary, assistant_social_director, from .models import President, UserProfile, Vice_President, General_Secretary, Financial_Secretary, Social_Director, Technical_Director, Sports_Director, Public_Relations_Officer, Treasurer, Welfare_Director, P_R_O1, P_R_O2, assistant_general_secretary, assistant_social_director, UserVote




@admin.register(President)
class PresidentAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'level')
    search_fields = ('name', 'department', 'level')

@admin.register(Vice_President)
class vice_PresidentAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'level')
    search_fields = ('name', 'department', 'level')

@admin.register(General_Secretary)
class General_SecretaryAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'level')
    search_fields = ('name', 'department', 'level')

@admin.register(Financial_Secretary)
class Financial_SecretaryAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'level')
    search_fields = ('name', 'department', 'level')

@admin.register(Social_Director)
class Social_DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'level')
    search_fields = ('name', 'department', 'level')

@admin.register(Technical_Director)
class Technical_DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'level')
    search_fields = ('name', 'department', 'level')

@admin.register(Sports_Director)
class Sports_DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'level')
    search_fields = ('name', 'department', 'level')

@admin.register(Public_Relations_Officer)
class Public_Relations_OfficerAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'level')
    search_fields = ('name', 'department', 'level')

@admin.register(Treasurer)
class TreasurerAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'level')
    search_fields = ('name', 'department', 'level')

@admin.register(Welfare_Director)
class Welfare_DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'level')
    search_fields = ('name', 'department', 'level')

@admin.register(P_R_O1)
class Welfare_DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'level')
    search_fields = ('name', 'department', 'level')

@admin.register(P_R_O2)
class Welfare_DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'level')
    search_fields = ('name', 'department', 'level')


@admin.register(assistant_general_secretary)
class AssistantGeneralSecretaryAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'level')
    search_fields = ('name', 'department', 'level')

@admin.register(assistant_social_director)
class assistant_social_directoraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'level')
    search_fields = ('name', 'department', 'level')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('matric_number', 'has_voted')
    search_fields = ('matric_number',)

class UserVoteAdmin(admin.ModelAdmin):
    list_display = ['user_profile', 'president_voted', 'vice_president_voted', 'general_secretary_voted', 
                    'financial_secretary_voted', 'social_director_voted', 'technical_director_voted',
                    'sports_director_voted', 'public_relations_officer_voted', 'treasurer_voted',
                    'welfare_director_voted', 'assistant_general_secretary_voted', 'assistant_social_director_voted',
                    'pro1_voted', 'pro2_voted', 'email']  
    list_filter = ['president_voted', 'vice_president_voted', 'general_secretary_voted', 
                   'financial_secretary_voted', 'social_director_voted', 'technical_director_voted',
                   'sports_director_voted', 'public_relations_officer_voted', 'treasurer_voted',
                   'welfare_director_voted', 'assistant_general_secretary_voted', 'assistant_social_director_voted',
                   'pro1_voted', 'pro2_voted', 'email']  

admin.site.register(UserVote, UserVoteAdmin)

