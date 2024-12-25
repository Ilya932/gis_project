from django.db import models

# Create your models here.

class Status(models.Model):
    name = models.CharField('Статус', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'



class Client(models.Model):
    email = models.CharField('Почта', max_length= 50)
    name = models.CharField('Имя', max_length= 50)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Place(models.Model):
    name = models.CharField('Название', max_length=100)
    image = models.ImageField('Картинка', upload_to='images/')
    description = models.TextField('Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Место отдыха'
        verbose_name_plural = 'Места отдыха'