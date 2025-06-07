from django.db import models

class Story(models.Model):
    """ Representa una entrada de blog en Tienda de Historias.
    Puede ser la reseña de un libr, una recomendación o una historia o curiosidad publicada por un autor.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    author_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

