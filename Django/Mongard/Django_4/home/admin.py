from django.contrib import admin
from .models import Person, Car, Answer, Question

admin.site.register(Person)
admin.site.register(Question)
admin.site.register(Car)
admin.site.register(Answer)