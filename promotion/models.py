from django.db import  models
from django.utils.text import slugify
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Promotion(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    expires = models.DateField()
    video_url = models.URLField()

    def __str__(self):
        return self.title


class Seo(models.Model):
    url = models.URLField(blank=True)
    title = models.CharField(max_length=255, blank=True)
    seo_text = models.TextField(blank=True)
    keywords = models.CharField(max_length=500, blank=True)
    description = models.TextField(blank=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"SEO for {self.content_object}"


class Page(models.Model):
    LANGUAGES = [
        ('ru', 'Русский'),
        ('uk', 'Украинский'),
    ]
    cinema = models.ForeignKey("cinema_app.Cinema", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    language = models.CharField(max_length=2, choices=LANGUAGES, default='ru')

    logo = models.ImageField(upload_to='pages/logo/', blank=True, null=True)
    seo = GenericRelation('promotion.Seo')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class NewsLetter(models.Model):
    MESSAGE_CHOICE = [
        ('email', 'Email'),
        ('sms', 'SMS'),
    ]
    message_type = models.CharField(max_length=10, choices=MESSAGE_CHOICE)
    sms_message = models.TextField(blank=True)
    html_file = models.FileField(upload_to='mail/html/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_sent = models.BooleanField(default=False)

    all_users = models.BooleanField(default=True)
    selected_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    total_recipients = models.PositiveIntegerField(default=0)
    sent_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_at']


class Banner(models.Model):
    banner_url = models.URLField(blank=True, null=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.banner_url or "Banner"

class PageImage(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='pages/gallery/')

class BannerImage(models.Model):
    banner = models.ForeignKey(Banner, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='banners/gallery/')
    bg_image = models.ImageField(upload_to='banners/background/', blank=True, null=True)
    upper_image = models.ImageField(upload_to='banners/upper/', blank=True, null=True)

class PromotionImage(models.Model):
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='promo/gallery/')
    main_image = models.ImageField(upload_to='promo/main/', blank=True, null=True)
