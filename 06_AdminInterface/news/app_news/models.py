from django.db import models


class News(models.Model):
    STATUS_CHOICES = [
        (True, 'Активно'),
        (False, 'Неактивно')
    ]
    title = models.CharField(max_length=300, verbose_name="Название")
    description = models.CharField(max_length=1500, verbose_name="Описание")
    public_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    edit_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    active_flag = models.BooleanField(verbose_name='Активность', choices=STATUS_CHOICES, default=False)

    def __str__(self):
        return f'{self.title}, {self.public_date}, {self.active_flag}'

    class Meta:
        db_table = 'news'
        ordering = ['public_date']


class Comments(models.Model):
    STATUS_CHOICES = [
        ('d', 'Удалено администратором')
    ]
    username = models.CharField(max_length=25, verbose_name="Имя")
    text_comment = models.CharField(max_length=1500, verbose_name="Ваш комментарий")
    article = models.ForeignKey('News', related_name="comments",
                                on_delete=models.CASCADE, verbose_name="Новость")

    # def __str__(self):
    #     return f'{self.username}, {self.text_comment[:15]}...'
    #


