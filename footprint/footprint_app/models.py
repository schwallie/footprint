from django.db import models
from django.contrib.postgres.fields import JSONField
from django.conf import settings

"""
Need to figure out cost. How do I want to do it?

# Food Items
# Synonyms
# Replacements
# Cost table?
"""


class FoodItems(models.Model):
    class Meta:
        verbose_name_plural = "food items"

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
    class Meta:
        verbose_name_plural = "recipes"
    food_item_ids = models.ManyToManyField(FoodItems)
    recipe_name = models.TextField()
    steps = JSONField()
    added_date = models.DateTimeField('date added', auto_now_add=True)
    updated_date = models.DateTimeField('date last updated', auto_now=True)


class Pantries(models.Model):
    class Meta:
        verbose_name_plural = "pantries"
    food_item_id = models.ForeignKey(FoodItems, on_delete=models.CASCADE)
    cost_cents_per_unit = models.FloatField(default=0)
    cost_cents = models.IntegerField(default=0)
    best_by_date = models.DateField('best by date')
    units_bought = models.FloatField(default=0)
    amount_left = models.FloatField(default=0)
    pantry_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    added_date = models.DateTimeField('date added', auto_now_add=True)
    updated_date = models.DateTimeField('date last updated', auto_now=True)

    @property
    def calc_cost_per_unit(self):
        return self.cost_cents / self.units_bought

    def save(self, *args, **kwarg):
        self.cost_cents_per_unit = self.calc_cost_per_unit
        super(Pantries, self).save(*args, **kwarg)

    def __str__(self):
        return "{} - {}".format(self.food_item_id, self.pantry_user)


class Synonyms(models.Model):
    class Meta:
        verbose_name_plural = "synonyms"
    food_item_id = models.ForeignKey(FoodItems, on_delete=models.CASCADE,)
    synonym = models.CharField(max_length=200)
    added_date = models.DateTimeField('date added', auto_now_add=True)
    updated_date = models.DateTimeField('date last updated', auto_now=True)


class Replacements(models.Model):
    class Meta:
        verbose_name_plural = "replacements"
    food_item_id = models.ForeignKey(FoodItems, on_delete=models.CASCADE,)
    replacement_food_item_ids = models.ManyToManyField(FoodItems, related_name="replacement_ids")
    replacement_steps = JSONField()
    added_date = models.DateTimeField('date added', auto_now_add=True)
    updated_date = models.DateTimeField('date last updated', auto_now=True)


class BrandsCostsAndStores(models.Model):
    class Meta:
        verbose_name_plural = "food costs"
    food_item_id = models.ForeignKey(FoodItems, on_delete=models.CASCADE,)
    pantry_added_to = models.ForeignKey(Pantries, on_delete=models.CASCADE,)
    cost_cents_per_unit = models.IntegerField(default=0)
    cost_cents = models.IntegerField(default=0)
    amount_bought = models.FloatField(default=0)
    added_date = models.DateTimeField('date added', auto_now_add=True)
    updated_date = models.DateTimeField('date last updated', auto_now=True)
