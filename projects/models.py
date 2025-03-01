from django.db import models
from tinymce.models import HTMLField

class Project(models.Model):
    cover_image = models.ImageField(upload_to='projects/covers/', verbose_name='Capa do Projeto', default='projects/covers/default.jpg')
    title = models.CharField(max_length=200, verbose_name='Título', default='Novo Projeto')
    short_info = models.CharField(max_length=500, verbose_name='Informação Breve', default='Breve descrição do projeto')
    body = HTMLField(verbose_name='Conteúdo do Projeto', default='Conteúdo do projeto')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    def __str__(self):
        return self.title
