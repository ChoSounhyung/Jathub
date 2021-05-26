from django.db import models


class Repository(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    deadline = models.DateTimeField()   # 사용자가 입력할 수 있게
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # repo1.introduction_set.all
    class Meta:
        verbose_name_plural = 'Repositories'

    def __str__(self):
        return self.name


class Introduction(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)    # intro1.repository
    version = models.IntegerField(default=1)
    contents = models.TextField()
    access = models.IntegerField(default=1)     # 0: private, 1: public

    # intro1.comment_set


    def __str__(self):
        return f'{self.version} {self.contents}'


class Comment(models.Model):
    introduction = models.ForeignKey(Introduction, on_delete=models.CASCADE)    # comm1.introduction
    comment = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
