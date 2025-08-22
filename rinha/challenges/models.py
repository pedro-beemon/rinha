from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Challenge(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    statement = models.TextField(verbose_name="Enunciado")
    judge_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Juiz")
    tags = models.CharField(max_length=255, help_text="Tags separadas por vírgula", verbose_name="Tags")
    criteria = models.TextField(help_text="Critérios de avaliação", verbose_name="Critérios")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    def __str__(self):
        return self.title

class ChallengeSubmission(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, verbose_name="Desafio")
    competitor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Competidor")
    code = models.TextField(verbose_name="Código")
    observations = models.TextField(blank=True, verbose_name="Observações")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        verbose_name = "Submissão"
        verbose_name_plural = "Submissões"
        ordering = ['-created_at']
        unique_together = ['challenge', 'competitor']  # Uma submissão por desafio por competidor
