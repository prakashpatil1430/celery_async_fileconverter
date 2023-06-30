from django.urls import path
from .views import ( disp_celery_call,
                    disp_normal_call,
                    file_converter_with_celery,
                    file_converter_without_celery
)

urlpatterns = [
    path('a/',disp_normal_call),
    path('b/',disp_celery_call),
    path('pddocx/',file_converter_without_celery),
    path('pddocxcelery/',file_converter_with_celery),
    path('pddocxcelery/<task_id>/',file_converter_with_celery, name='check_status')
   
]
