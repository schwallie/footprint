from django.contrib import admin

from .models import Recipes
from .models import FoodItems
from .models import Pantries
from .models import Synonyms
from .models import Replacements
from .models import BrandsCostsAndStores

admin.site.register(Recipes)
admin.site.register(FoodItems)
admin.site.register(Pantries)
admin.site.register(Synonyms)
admin.site.register(Replacements)
admin.site.register(BrandsCostsAndStores)