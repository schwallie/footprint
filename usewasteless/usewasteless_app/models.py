from django.db import models
from django.contrib.postgres.fields import JSONField
from django.conf import settings


class FoodItems(models.Model):
    food_item_name = models.CharField(max_length=200)
    added_date = models.DateTimeField('date added', auto_now_add=True)
    updated_date = models.DateTimeField('date last updated', auto_now=True)
    contains_soy = models.BooleanField()
    contains_nuts = models.BooleanField()
    unit_type = models.CharField(max_length=40, default="")
    estimated_calories_per_unit = models.IntegerField(default=0)
    estimated_cost_cents_per_unit = models.FloatField(default=0)

    def __str__(self):
        return self.food_item_name


class Recipes(models.Model):
    food_item_ids = models.ManyToManyField(FoodItems)
    recipe_name = models.TextField()
    steps = JSONField()
    added_date = models.DateTimeField('date added', auto_now_add=True)
    updated_date = models.DateTimeField('date last updated', auto_now=True)


class Pantries(models.Model):
    food_item_id = models.ManyToManyField(FoodItems)
    cost_cents_per_unit = models.IntegerField(default=0)
    best_by_date = models.DateTimeField('best by date')
    amount_bought = models.FloatField(default=0)
    amount_left = models.FloatField(default=0)
    pantry_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    added_date = models.DateTimeField('date added', auto_now_add=True)
    updated_date = models.DateTimeField('date last updated', auto_now=True)


class Synonyms(models.Model):
    food_item_id = models.ManyToManyField(FoodItems)
    synonym = models.CharField(max_length=200)
    added_date = models.DateTimeField('date added', auto_now_add=True)
    updated_date = models.DateTimeField('date last updated', auto_now=True)


class Replacements(models.Model):
    food_item_id = models.ManyToManyField(FoodItems)
    replacement_food_item_ids = models.ManyToManyField(FoodItems)
    replacement_steps = JSONField()
    added_date = models.DateTimeField('date added', auto_now_add=True)
    updated_date = models.DateTimeField('date last updated', auto_now=True)
