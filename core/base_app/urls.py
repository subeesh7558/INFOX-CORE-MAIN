from django.urls import re_path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$', views.index_new, name='index'),
    re_path(r'^BRadmin_profiledash_new$', views.BRadmin_profiledash_new,name='BRadmin_profiledash_new'),
    re_path(r'^BRadmin_employees_new$', views.BRadmin_employees_new, name='BRadmin_employees_new'),
    re_path(r'^BRadmin_python_new$', views.BRadmin_python_new, name='BRadmin_python_new'),
    re_path(r'^BRadmin_projects_new/(?P<id>\d+)$', views.BRadmin_projects_new, name='BRadmin_projects_new'),
    re_path(r'^BRadmin_proj_cmpltd_new/(?P<id>\d+)$', views.BRadmin_proj_cmpltd_new, name='BRadmin_proj_cmpltd_new'),
    # re_path(r'^BRadmin_proj_det$', views.BRadmin_proj_det, name='BRadmin_proj_det'),
    re_path(r'^BRadmin_cmpltd_proj_det_new/(?P<id>\d+)/$', views.BRadmin_cmpltd_proj_det_new, name='BRadmin_cmpltd_proj_det_new'),
    re_path(r'^BRadmin_proj_mngrs_new/(?P<id>\d+)/$', views.BRadmin_proj_mngrs_new, name='BRadmin_proj_mngrs_new'),
    re_path(r'^BRadmin_proj_mangrs1_new/(?P<id>\d+)/$', views.BRadmin_proj_mangrs1_new, name='BRadmin_proj_mangrs1_new'),
    re_path(r'^BRadmin_proj_mangrs2_new/(?P<id>\d+)/$', views.BRadmin_proj_mangrs2_new, name='BRadmin_proj_mangrs2_new'),
    re_path(r'^BRadmin_developers_new/(?P<id>\d+)/$', views.BRadmin_developers_new, name='BRadmin_developers_new'),
    re_path(r'^BRadmin_daily_report_new/(?P<id>\d+)/$', views.BRadmin_daily_report_new, name='BRadmin_daily_report_new'),


]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)