from django.db import models
import datetime

class Post(models.Model):
    autor = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    texto = models.CharField(max_length=100000)
    data = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.autor

class Comentario(models.Model):
    autor = models.CharField(max_length=100)
    texto = models.CharField(max_length=300)

    MUITO_MAU = '⭐'
    MAU = '⭐⭐'
    INDIFERENTE = '⭐⭐⭐'
    BOM = '⭐⭐⭐⭐'
    MUITO_BOM = '⭐⭐⭐⭐⭐'

    RATINGS_CHOICES = [
        (MUITO_MAU, '⭐'),
        (MAU, '⭐⭐'),
        (INDIFERENTE, '⭐⭐⭐'),
        (BOM, '⭐⭐⭐⭐'),
        (MUITO_BOM, '⭐⭐⭐⭐⭐'),
    ]

    rating = models.CharField(max_length=10, choices=RATINGS_CHOICES, default=MUITO_MAU, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')

    def __str__(self):
        return self.autor
