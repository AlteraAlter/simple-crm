from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Record
from django.utils.text import slugify


@receiver(pre_save, sender=Record)
def auto_slug(sender, instance, **kwargs):
    fullname = f'{instance.first_name} {instance.last_name}'
    new_slug = slugify(fullname)

    if instance.slug != new_slug:
        instance.slug = new_slug

        original_slug = instance.slug
        counter = 1
        while Record.objects.filter(slug=instance.slug).exists():
            instance.slug = f'{original_slug}-{counter}'
            counter += 1
