from django.db import models
from django.db.models import Count

from account .models import Author


class AbstractPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class News(AbstractPost):
    def __str__(self):
        return f'News {self.id} by {self.author.user.username}'


    def get_status(self):
        statuses = StatusNews.objects.all(news=self).values('status_name').annotate(count=Count('status'))
        result = {}
        for i in statuses:
            result[i['status_name']] = i['count']
        return result


class Comment(AbstractPost):
    text = models.CharField(max_length=255)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def get_status(self):
        statuses = StatusComment.objects.filter(news=self).values('status_name').annotate(count=Count('status'))
        result = {}
        for i in statuses:
            result[i['status_name']] = i['count']
        return result


    def __str__(self):
        return f'Comment {self.id} by {self.author.user.username} to {self.news.id}'

class StatusType(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=50, unique=True)


    def __str__(self):
        return self.name

class StatusNews(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.SET_DEFAULT, default=1)
    status = models.ForeignKey(StatusType, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['news', 'author']


    def __str__(self):
        return f'{self.news.id} - {self.author} - {self.status}'


class StatusComment(models.Model):
    status = models.ForeignKey(StatusType, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['author', 'comment']

    def __str__(self):
        return f'{self.comment.id} - {self.author} - {self.status}'







