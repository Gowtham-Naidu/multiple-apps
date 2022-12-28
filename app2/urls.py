from django.urls import path
from app2.views import *
app_name='something2'

urlpatterns=[
    path('onehtml/',onehtml,name='onehtml'),
    path('twohtml/',twohtml,name='twohtml'),
    
]