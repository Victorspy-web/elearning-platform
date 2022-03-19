from ckeditor.fields import RichTextField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from .fields import OrderField

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
    instance.slug = slugify(instance.title)

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
def subject_pre_save(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)

class Module(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=250)
    description = RichTextField(blank=True)
    order = OrderField(blank=True, for_fields=['course'])

    def __str__(self):
        return f"{self.title}. {self.title}"
    
    class Meta:
        ordering = ['order']


class Content(models.Model):
    module = models.ForeignKey(
        Module, on_delete=models.CASCADE, related_name='contents')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={
        'model__in': ('text', 'video', 'image', 'file')
    })
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])
    
    class Meta:
        ordering = ['order']


class ItemBase(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="%(class)s_related")
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Text(ItemBase):
    content = models.TextField()


class File(ItemBase):
    file = models.FileField(upload_to="files")


class Image(ItemBase):
    file = models.FileField(upload_to='img')


class Video(ItemBase):
    url = models.URLField()
