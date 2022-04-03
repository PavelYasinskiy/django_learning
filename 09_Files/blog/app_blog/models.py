from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return f"avatar/user_{instance.user.id}/{filename}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=500,
                                   verbose_name="О себе", null=True, blank=True)
    second_name = models.CharField(max_length=40,
                                   verbose_name="Фамилия", null=True, blank=True)
    avatar = models.ImageField(upload_to=user_directory_path,
                               verbose_name="Аватар пользователя", null=True, blank=True)


def blog_directory_path(BlogImage, filename):
    return f"blog/blog_{BlogImage.to_blog.id}/{filename}"

class Blog(models.Model):
    blog_text = models.CharField(max_length=2000, verbose_name="Рассказ")
    public_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author', null=True, blank=True)

    class Meta:
        ordering = ['-public_date']


class BlogImage(models.Model):
    blog_photo = models.ImageField(upload_to=blog_directory_path,
                               verbose_name="Фото блога", null=True, blank=True)
    to_blog = models.ForeignKey('Blog', on_delete=models.CASCADE, verbose_name='Для блога',
                                related_name='blog', null=True, blank=True, )






# у каждой записи отобразите имя пользователя и первые 100 символов текста записи.


# реализуйте возможность загрузить несколько записей блога одним файлом csv.
# В нем должно быть две колонки: текст и дата публикации
