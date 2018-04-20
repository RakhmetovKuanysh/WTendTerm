from django.db import models


class BlogManager(models.Manager):
    def add_blog(self, title, content, date):
        obj = Blog(title=title, content=content, date=date)
        obj.save()
        return obj


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=500)
    date = models.DateTimeField('date published')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    objects = BlogManager()

    def full(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'date': str(self.date),
            'is_active': self.is_active,
        }