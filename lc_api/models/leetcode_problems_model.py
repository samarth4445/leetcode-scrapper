import logging
from typing import Any

from django.db import models

class ContestModel(models.Model):
    contest_number = models.IntegerField()
    contest_link = models.URLField()

    class Meta:
        db_table = "contest"

class TagModel(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class LeetcodeProblemsModel(models.Model):
    class Difficulty(models.TextChoices):
        EASY = "EASY", "EASY"
        MEDIUM = "MEDIUM", "MEDIUM"
        HARD = "HARD", "HARD"
    
    title = models.CharField(max_length=30)
    score = models.IntegerField()
    link = models.URLField()
    contest = models.ForeignKey(ContestModel, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=15, choices=Difficulty.choices, blank=True, null=True)
    tags = models.ManyToManyField(TagModel, related_name="leetcode_problems")

    class Meta:
        db_table = "problems"