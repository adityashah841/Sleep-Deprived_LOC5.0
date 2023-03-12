from django.urls import path
from .views import test_ml_ac, test_ml_geyser, test_cv, test_cv_get, test_time_sum_motor, test_time_sum_light, dashboard

urlpatterns = [
    path('ml_ac/<str:temp>/<str:hum>', test_ml_ac, name='ml_ac'),
    path('ml_geyser/<str:temp>', test_ml_geyser, name = 'ml_geyser'),
    path('ml_cv/', test_cv, name = 'ml_cv'),
    path('ml_cv_get/', test_cv_get, name = 'ml_cv_get'),
    path('ml_light_time/<str:time>', test_time_sum_light, name='ml_light_time'),
    path('ml_motor_time/<str:time1>/<str:time2>', test_time_sum_motor, name='ml_motor_time'),
    path('dashboard/', dashboard, name='dashboard')
]