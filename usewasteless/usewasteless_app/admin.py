from django.contrib import admin

from .models import Recipes
from .models import FoodItems
from .models import Pantries
from .models import Synonyms

admin.site.register(Recipes)
admin.site.register(FoodItems)
admin.site.register(Pantries)
admin.site.register(Synonyms)