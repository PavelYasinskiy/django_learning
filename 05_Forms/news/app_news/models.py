from django.db import models


class News(models.Model):
    title = models.CharField(max_length=300, verbose_name="Название")
    description = models.CharField(max_length=1500, verbose_name="Описание")
    public_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    edit_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    active_flag = models.BooleanField(verbose_name='Активность')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'news'
        ordering = ['public_date']


class Comments(models.Model):
    username = models.CharField(max_length=25, verbose_name="Имя")
    text_comment = models.CharField(max_length=1500, verbose_name="Ваш комментарий")
    article = models.ForeignKey('News', related_name="comments",
                                on_delete=models.CASCADE, verbose_name="Новость")

# Создайте новостной сайт. Он должен уметь отображать новости и поддерживать возможность их комментировать.
# Создайте модель Новость с полями:
# название, содержание, дата создания, дата редактирования, флаг активности.
# Создайте модель Комментарий с полями:
# имя пользователя, текст комментария, новость (связь с моделью новость).

# Создайте странички:
# список всех новостей (новости отсортированы по дате создания),
# страничку создания новости,
# страничку редактирования новости,
# детальная страница новости+комментарии к ней (с возможностью добавить новый комментарий).

