from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Image

@receiver(signal=m2m_changed, sender=Image.user_like.through)
def user_like_changed(sender, instance, **kwargs):
	instance.total_likes = instance.user_like.count()
	instance.save()

# m2m_changed.connect(user_like_changed, sender=Image.user_likes.through)