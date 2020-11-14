from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserBaseModel(BaseModel):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Author(UserBaseModel):

    def __str__(self) -> str:
        return " ".join([x for x in [self.first_name, self.last_name] if x])


class Article(BaseModel):

    title = models.CharField(max_length=100)
    context = models.TextField()

    # author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.context

    class Meta:
        ordering = ['title']
