from django.conf.urls import url

from .views import MachineToolRequirementsList

urlpatterns = [
    url(r'^machine-tool-requirements/', MachineToolRequirementsList.as_view()),
]
