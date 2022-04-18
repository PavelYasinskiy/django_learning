from django.db import models
from django.contrib.auth.models import User, Group



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
    tag = models.ManyToManyField('Tag', verbose_name='Тэги', related_name='tag', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='author', null=True, blank=True)

    def __str__(self):
        return f'{self.title}, {self.public_date}, {self.active_flag}'

    class Meta:
        db_table = 'news'
        ordering = ['public_date']
        permissions = (
            ('can_publish', "Может публиковать"),
        )


class Tag(models.Model):
    name = models.CharField(max_length=300, verbose_name="Название", null=True, blank=True)
    def __str__(self):
        return f'{self.name}'


class Comments(models.Model):
    STATUS_CHOICES = [
        ('d', 'Удалено администратором')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='auth_user', null=True, blank=True)
    username = models.CharField(max_length=25,  null=True, blank=True)
    text_comment = models.CharField(max_length=1500, verbose_name="Ваш комментарий")
    article = models.ForeignKey('News', related_name="comments",
                                on_delete=models.CASCADE, verbose_name="Новость")

class Profile(models.Model):
    STATUS_CHOICES = [
        (True, 'Верифицирован'),
        (False, 'Неверифицирован')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона')
    city = models.CharField(max_length=35, verbose_name='Город')
    verification_flag = models.BooleanField(verbose_name='Верификация', choices=STATUS_CHOICES, default=False)


    class Meta:
        permissions = (
            ('can_give_add_news', "Может давать права на добавление новостей"),
        )

    @property
    def news_count(self):
        return News.objects.filter(author=self.user, active_flag=True).all().count()

    # def verify(self):
    #     verify_group = Group.objects.get(name='Верифицированный')
    #     deverify_group = Group.objects.get(name='Обычный')
    #     if self.verification_flag is True and self.groups.filter(id=verify_group.id).exists():
    #         self.user.groups.add(verify_group)
    #     else:
    #         self.user.groups.add(deverify_group)
