from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Partner(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    slug = models.SlugField(max_length=100, verbose_name=_('Slug'), unique=True, blank=True, null=True)
    discription = models.TextField(verbose_name=_('Discription'), blank=True, null=True)
    website = models.URLField(verbose_name=_('Website'))
    image = models.ImageField(upload_to='partner', verbose_name=_('Image'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    class Meta:
        verbose_name = _('Partner')
        verbose_name_plural = _('Partners')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Partner, self).save(*args, **kwargs)


class FAQCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    slug = models.SlugField(max_length=100, verbose_name=_('Slug'), unique=True, blank=True, null=True)

    class Meta:
        verbose_name = _('FAQ category')
        verbose_name_plural = _('FAQ categories')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(FAQCategory, self).save(*args, **kwargs)


class FAQ(models.Model):
    category = models.ForeignKey(FAQCategory, on_delete=models.CASCADE, verbose_name=_('Category'))
    question = models.CharField(max_length=100, verbose_name=_('Question'))
    slug = models.SlugField(max_length=100, verbose_name=_('Slug'), unique=True, blank=True, null=True)
    answer = models.TextField(verbose_name=_('Answer'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    class Meta:
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQs')

    def __str__(self):
        return self.question

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.question)
        super(FAQ, self).save(*args, **kwargs)


class TrainingType(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    slug = models.SlugField(max_length=100, verbose_name=_('Slug'), unique=True, blank=True, null=True)

    class Meta:
        verbose_name = _('Training type')
        verbose_name_plural = _('Training types')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(TrainingType, self).save(*args, **kwargs)


class Training(models.Model):
    type = models.ForeignKey(TrainingType, on_delete=models.CASCADE, verbose_name=_('Type'))
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    slug = models.SlugField(max_length=100, verbose_name=_('Slug'), unique=True, blank=True, null=True)
    discription = models.TextField(verbose_name=_('Discription'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    video = models.URLField(verbose_name=_('Video link'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    class Meta:
        verbose_name = _('Training')
        verbose_name_plural = _('Trainings')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Training, self).save(*args, **kwargs)


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    email = models.EmailField(verbose_name=_('Email'))
    phone = models.CharField(max_length=100, verbose_name=_('Phone'), blank=True, null=True)
    message = models.TextField(verbose_name=_('Message'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __str__(self):
        return self.name


SOCIAL_PLATFORMS = (
    ('facebook', 'Facebook'),
    ('instagram', 'Instagram'),
    ('linkedin', 'LinkedIn'),
    ('youtube', 'Youtube'),
)


class SocialMedia(models.Model):
    platform = models.CharField(max_length=100, verbose_name=_('Platform'), choices=SOCIAL_PLATFORMS, unique=True)
    url = models.URLField(verbose_name=_('Link'))
    icon = models.CharField(max_length=100, verbose_name=_('Icon'), blank=True, null=True)

    class Meta:
        verbose_name = _('Social Media')
        verbose_name_plural = _('Social Medias')

    def __str__(self):
        return self.platform
