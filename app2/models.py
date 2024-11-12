from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
# Create your models here.


class Products(models.Model):
  product_name = models.CharField(max_length=100, null=False, blank=False)
  selling_price = models.FloatField()
  product_image = models.ImageField(upload_to='images', null=False)
  short_description = models.TextField(null=True, blank=True ,help_text='max 30 words')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  this_product_available = models.BooleanField(default=True)

  class Meta:
    ordering = [
      '-created_at','-updated_at'
    ]
  def __str__(self):
    return self.product_name



class QuickLink(models.Model):
  platform_name = models.CharField(max_length=100)
  url = models.URLField(blank=False, null=False)

  def __str__(self) -> str:
    return self.platform_name

class UserDetail(models.Model):
  name = models.TextField()
  email = models.TextField()
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-created']
  
  def __str__(self) -> str:
    return self.name


@receiver(post_save, sender = Products)
def notifying_user(sender, instance, created, **kwargs):
  if created:
    user_emails = UserDetail.objects.values_list('email',flat=True)

    product_url = f"{settings.SITE_URL}{reverse('home-web')}"
    message = (
      f"A new product '{instance.product_name}' is now available at Angel`s store.!\n\n "
      f"Check it out here:  {product_url}\n\n"
      "Thank you for staying connected with us !!!."
    )

    send_mail(
      subject='New Product Added',
      message=message,
      from_email=settings.DEFAULT_FROM_EMAIL,
      recipient_list=list(user_emails),
      fail_silently=False,
    )
    
