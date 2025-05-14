from django.db import modelscd

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth = models.DateField()
    def __str__(self):
        return f"Musician(id={self.id}, last_name={self.last_name})"
