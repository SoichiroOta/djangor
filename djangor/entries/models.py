from django.db import models


class Entry(models.Model):
    title = models.TextField()
    text = models.TextField()

    def __str__(self):
        return '<Entry id={id} title={title!r}>'.format(
            id=self.id, title=self.title
        )
