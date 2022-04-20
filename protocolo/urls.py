from django.urls import path
from . import views



urlpatterns = [
    path('', views.protocolos_view, name="protocols"),
    path('parts/<int:protocol_id>',
         views.parts_view, name="parts"),
    path('areas/<int:protocol_id>/<int:part_id>',
         views.areas_view, name="areas"),
    path('instruments/<int:protocol_id>/<int:part_id>/<int:area_id>',
         views.instruments_view, name="instruments"),
    path('dimension/<int:protocol_id>/<int:part_id>/<int:area_id>/<int:instrument_id>',
         views.dimensions_view, name="dimensions"),
    path('section/<int:protocol_id>/<int:part_id>/<int:area_id>/<int:instrument_id>/<int:dimension_id>',
         views.sections_view, name="sections"),
    path('question/<int:protocol_id>/<int:part_id>/<int:area_id>/<int:instrument_id>/<int:dimension_id>/<int:section_id>',
         views.question_view, name="question"),
    path('question/<int:protocol_id>/<int:part_id>/<int:area_id>/<int:instrument_id>/<int:dimension_id>/<int:section_id>/<int:question_id>',
         views.post_mcq_view, name="post_mcq"),
]