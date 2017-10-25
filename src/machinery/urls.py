from django.conf.urls import url

from .views import MachineToolRequirementsList, MachineToolRequirementsDetail

urlpatterns = [
    url(r'^machine-tool-requirements/$', MachineToolRequirementsList.as_view()),
    url(r'^machine-tool-requirements/(?P<pk>\w+)/$', MachineToolRequirementsDetail.as_view(),
        name='machine-tool-requirements-detail'),
]
