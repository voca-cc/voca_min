import uuid

from django.db import models
from ckeditor.fields import RichTextField
from uuslug import slugify
from phonenumber_field.modelfields import PhoneNumberField


class Trip(models.Model):
    owner = models.ForeignKey('TourAuthor', on_delete=models.PROTECT, verbose_name='Автор тура', related_name='tour_author', null=True)
    img_trip = models.ImageField(upload_to='img_trip/', verbose_name='Изображение тура', blank=False)
    title = models.TextField(max_length=1000, verbose_name='Наименование тура', blank=False)
    description = RichTextField(max_length=3000, verbose_name='Описание тура', blank=False)
    date_start = models.DateField(verbose_name='Дата начала тура', blank=False)
    date_end = models.DateField(verbose_name='Дата окончания тура')
    price = models.PositiveIntegerField(verbose_name='Стоимость', null=True)
    included_coast = RichTextField(verbose_name='В стоимость включено')
    not_included_coast = RichTextField(verbose_name='В стоимость не включено')
    number_party = models.PositiveIntegerField(verbose_name='Количество участников', null=True)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = '{}'.format(slugify(self.title + str(self.owner)))
        super(Trip, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Путешествие'
        verbose_name_plural = 'Путешествия'


class RoadMap(models.Model):
    img_day = models.ImageField(upload_to='days', verbose_name='Изображение дня', null=True)
    trip = models.ForeignKey(Trip, on_delete=models.PROTECT, related_name='roadmap_trip', verbose_name='Дорожная карта путешествия')
    day = models.CharField(verbose_name='День №', max_length=50)
    description = models.TextField(verbose_name='Описание дня', max_length=1000)

    # todo Добавить фото и картинки

    def __str__(self):
        return self.day

    def save(self, *args, **kwargs):
        self.slug = '{}'.format(slugify(self.day))
        super(RoadMap, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Дорожная карта'
        verbose_name_plural = 'Дорожные карты'


class TourAuthor(models.Model):
    avatar = models.ImageField(upload_to='avatars', verbose_name='Аватар', null=True)
    name = models.CharField(max_length=300, verbose_name='Имя автора тура')
    phone = PhoneNumberField(blank=True, null=True, verbose_name='Телефон')
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    vk_link = models.URLField(blank=True, null=True, verbose_name='Vk')
    instagram_link = models.URLField(blank=True, null=True, verbose_name='Instagram')
    facebook_link = models.URLField(blank=True, null=True, verbose_name='Facebook')
    telegram_link = models.URLField(blank=True, null=True, verbose_name='Telegram')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор тура'
        verbose_name_plural = 'Авторы туров'


class Registration(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    trip = models.ForeignKey(Trip, on_delete=models.PROTECT, related_name='registration_trip')
    name = models.CharField(max_length=300, verbose_name='Имя')
    email = models.EmailField(max_length=300, verbose_name='E-mail')
    phone = PhoneNumberField(verbose_name='Телефон', null=False, blank=True)
    link = models.URLField(blank=True, null=True, verbose_name='Соц.сети')

    def __str__(self):
        return self.name + ' ' + str(self.phone)


    class Meta:
        verbose_name = 'Регистрация'
        verbose_name_plural = 'Регистрации на туры'