from django.shortcuts import render

from base_app.models import *

# Create your views here.
def index_new(request):
   
    return render(request,'BRadmin_index_show.html')

def BRadmin_profiledash_new(request):
     Num = project.objects.count()
     project_details = project.objects.all()
    
     return render(request,'BRadmin_profile_dash.html',{'project':project_details,'num':Num})

def BRadmin_employees_new(request):
    project_details = project.objects.all()
    departments = department.objects.all()
    return render(request,'BRadmin_employees_show.html',{'project':project_details,'department':departments})

def BRadmin_python_new(request):
    project_details = project.objects.all()
    return render(request,'BRadmin_projects.html',{'project':project_details})

def BRadmin_projects_new(request, id):
    Num = project.objects.filter(status='completed').filter(department=id).count()
    project_details = project.objects.all()
    departments = department.objects.get(id=id)
    id=id
    # for i in project_details:
    #     if i.progress == "in progress":  
    #         Num = Num-1
    #         break
    return render(request,'BRadmin_projects_show.html',{'project':project_details,'num':Num, 'department':departments,'id':id})
   


def BRadmin_proj_cmpltd_new(request, id):
    project_details=project.objects.filter(department=id)
    print (project_details.count())
    return render(request,'BRadmin_proj_cmpltd_show.html',{'project': project_details})

# def BRadmin_proj_det(request):
#     return render(request,'BRadmin_proj_det.html')

def BRadmin_cmpltd_proj_det_new(request, id):
    project_details = project.objects.get(id=id)

    return render(request,'BRadmin_cmpltd_proj_det_show.html',{'project': project_details})

def BRadmin_proj_mngrs_new(request, id):
    project_details = project.objects.get(id=id)
    return render(request,'BRadmin_proj_mngrs_show.html', {'project': project_details})

def BRadmin_proj_mangrs1_new(request,id):
    project_details = project.objects.get(id=id)
    return render(request,'BRadmin_proj_mangrs1_show.html', {'project': project_details})

def BRadmin_proj_mangrs2_new(request, id):
    project_details = project.objects.get(id=id)
    project_task = project_taskassign.objects.all()
    return render(request,'BRadmin_proj_mangrs2_show.html', {'project':project_details,'project_taskassign':project_task})

def BRadmin_developers_new(request, id):
    project_details = project.objects.get(id=id)
    project_task = project_taskassign.objects.filter(tl_id = id)
    return render(request,'BRadmin_developers_show.html', {'project':project_details,'project_taskassign':project_task})

def BRadmin_daily_report_new(request, id):
    project_task = project_taskassign.objects.get(id=id)
    tester = tester_status.objects.all()
    return render(request,'BRadmin_daily_report_show.html', {'project':project_task,'tester_status':tester})