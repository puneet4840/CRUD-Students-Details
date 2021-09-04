from django.shortcuts import render,HttpResponseRedirect
from . forms import Student_Form
from . models import Student

# Create your views here.

# This view function is used to add and display the data on webpage.
def add_show(request):
    if request.method=="POST":
        stu_details=Student_Form(request.POST)
        if stu_details.is_valid():
            nm=stu_details.cleaned_data['name']
            em=stu_details.cleaned_data['email']
            pw=stu_details.cleaned_data['password']

            data_base=Student(name=nm,email=em,password=pw)
            data_base.save()
            stu_details=Student_Form()
    else:
        stu_details=Student_Form()
    print_stu_details=Student.objects.all()
    
    return render(request,'enroll/addandshow.html',{'form':stu_details,'print_database':print_stu_details})


# This view function is used to delete the data from database.
def delete_data(request,id):
    if request.method=="POST":
        db_obj=Student.objects.get(pk=id)
        db_obj.delete()
        return HttpResponseRedirect('/')


# This function will update the data in database.
def update_data(request,id):
    if request.method=="POST":
        update_db_obj=Student.objects.get(pk=id)
        form_obj=Student_Form(request.POST,instance=update_db_obj)
        if form_obj.is_valid():
            form_obj.save()
    else:
        update_db_obj=Student.objects.get(pk=id)
        form_obj=Student_Form(instance=update_db_obj)

    return render(request,'enroll/updatestudents.html',{'form':form_obj})