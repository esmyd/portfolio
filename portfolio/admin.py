# from msilib.schema import Icon
from django.contrib import admin
from .models import Project, Icon, Profile, Skill, Flag

class IconsProyect(admin.TabularInline):
    model = Icon 
    
class SkillsProfile(admin.TabularInline):
    model = Skill 

class FlagsProfile(admin.TabularInline):
    model = Flag 
    
admin.site.register(Project, inlines = [IconsProyect])
admin.site.register(Profile, inlines = [SkillsProfile,FlagsProfile]) 
