from django.contrib import admin
## Luego de establecer usuario y contraseña para el admin
from .models import Question


admin.site.register(Question)
