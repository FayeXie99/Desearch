from django.shortcuts import render,redirect
from .models import Project
from django.http import HttpResponse


from django.contrib.auth.decorators import login_required

from .form import ProjectForm
# projectList=[
#     {
#         'id':'1',
#         'title': 'Ecommerce Website',
#         'description':'Fully functional ecommerce website'
#     },
#     {
#         'id':'2',
#         'title': 'Portfolio Website',
#         'description':'This was a project where I built out my portfolio'
#     },
#     {
#         'id':'3',
#         'title': 'Social Network',
#         'description':'Awesome open source project I am still working on'
#     }
# ]




def projects(request):
    projects= Project.objects.all()
    context = {'projects':projects}
    return render(request,'projects/projects.html',context)

def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    return render(request,'projects/single-project.html',{'projectObj':projectObj})
    #return HttpResponse("Single project"+" "+str(pk))

@login_required(login_url="login")
def createProject(request):
    form = ProjectForm()
    if request.method=='POST':
        #print(request.POST)
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save() #add new object in database
            return redirect('projects')
        
    context = {'form': form}
    return render(request,"projects/project_form.html",context)

@login_required(login_url="login")
def updateProject(request,pk):
    project=Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method=='POST':
        #print(request.POST)
        form = ProjectForm(request.POST,request.FILES, instance=project)
        if form.is_valid():
            form.save() #add new object in database
            return redirect('projects')
        
    context = {'form': form}
    return render(request,"projects/project_form.html",context)
    
@login_required(login_url="login")
def deleteProject(request,pk):
    project=Project.objects.get(id=pk)
    if request.method=="POST":
        project.delete()
        return redirect("projects")
    context = {'object': project}
    return render(request,"projects/delete_template.html",context)