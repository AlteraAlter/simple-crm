from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Record
from django.utils.text import slugify


@receiver(post_save, sender=Record)
def auto_slug(sender, instance, **kwargs):
    if not instance.slug:
        fullname = f'{instance.first_name} {instance.last_name}'
        instance.slug = slugify(fullname)

        current_slug = instance.slug
        count = 1
        while Record.objects.filter(slug=instance.slug).exists():
            instance.slug = f'{current_slug}-{count}'
            count += 1
