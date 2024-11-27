from django.contrib import admin
from .models import Profile, Skill, Education, SocialMedia


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "is_key_skill", "proficiency")


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("social_media_name", "icon_path")
