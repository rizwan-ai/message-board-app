from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# post1 = Post(title="First Post", body="This is my first post")
# post2 = Post(title="Second Post", body="This is my second post")
# post3 = Post(title="Third Post", body="This is my third post")

# posts = [post1, post2, post3]

# for post in posts:
#     print(f"Title: {post.title}, Body: {post.body}")
