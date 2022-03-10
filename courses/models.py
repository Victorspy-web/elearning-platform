from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

User = settings.AUTH_USER_MODEL


class Subject(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Subject)
def subject_pre_save(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance=title)


class Course(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='courses_created')
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    overview = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['title']


@receiver(pre_save, sender=Course)
def course_pre_save(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance=title)


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=250)
    description = RichTextField(blank=True)
    
    
    def __str__(self):
        return self.title