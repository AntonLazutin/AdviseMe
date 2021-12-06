from django.db import models
from django.contrib.auth.views import UserModel
from django.urls import reverse


class GenreChoices(models.TextChoices):
    MOV = "MOV", "Movie"
    BK = "BK", "Book"
    GM = "GM", "Game"


class Genre(models.Model):
    title = models.TextField(max_length=5, choices=GenreChoices.choices, default=None)

    def __str__(self):
        return self.title


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    genre = models.TextField(choices=GenreChoices.choices)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    pub_date = models.DateField("Date published", auto_now_add=True)
    subject = models.TextField(max_length=20)
    text = models.TextField(max_length=100, default="")
    rating = models.IntegerField(choices=RATING_CHOICES)
    id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return f"Review of {self.subject} by {self.author}"

    def get_absolute_url(self):
        return reverse('review_page', args=[str(self.id)])


class Comment(models.Model):
    review = models.ForeignKey(Review, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(UserModel, null=True, on_delete=models.CASCADE)
    text = models.TextField(max_length=100)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        if self.author:
            return '%s - %s' % (self.author, self.date_added)
        else:
            return '%s - %s' % ('Anon', self.date_added)
