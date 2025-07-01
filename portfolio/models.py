from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=False)
    description = models.TextField()
    image = CloudinaryField('image')
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # タイトルからslugを自動生成
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['order'] 

