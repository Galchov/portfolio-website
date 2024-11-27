from django.db import models


class Profile(models.Model):
    name = models.CharField(
        max_length=100,
    )
    bio = models.TextField()
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Skill(models.Model):

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    proficiency = models.IntegerField(
        default=0,
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True,
    )
    is_key_skill = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.name


class Education(models.Model):
    certificate = models.ImageField(
        upload_to='certificates/',
        blank=True,
        null=True,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )


class SocialMedia(models.Model):
    social_media_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    social_media_link = models.URLField(
        blank=True,
        null=True,
    )
    icon_path = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
