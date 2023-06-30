from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .tasks import sleepy, send_mail_task_with_celery, convert_doc_to_pdf
from .helpers import send_mail_without_celery
from datetime import datetime

from django.core.files.storage import FileSystemStorage
import os
from docx2pdf import convert
from celery.result import AsyncResult
# Create your views here.



def index(request):
    sleepy.delay(30)
    return HttpResponse('<h1> Hello Celery from patil</h1>')

# without celery task assigning calling from django based

def disp_normal_call(request):
    start_time = datetime.now()
    for i in range(5):
        send_mail_without_celery()
    return HttpResponse(f"sent mail without celery time taken :{datetime.now()-start_time}")

# using celery task of sendong mail

def disp_celery_call(request):
    start_time = datetime.now()
    for i in range(5):
        
        send_mail_task_with_celery.delay()
        print(f'{i}')
    return HttpResponse(f"sent mail using celery,time taken :{datetime.now()-start_time}")

# without celery
def file_converter_without_celery(request):
    if request.method == 'POST':
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        file_name = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(file_name)
        convert('hotels/static/' + myfile.name)

    return render(request,'converter.html')



# with celery
def file_converter_with_celery(request):
    if request.method == 'POST':
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        file_name = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(file_name)
        task = convert_doc_to_pdf.delay(myfile.name)
        return HttpResponseRedirect('pddocxcelery/'+task.id)
        
    return render(request,'converter.html')

def check_status(request, task_id):
    res = AsyncResult(task_id)
    print(res.ready())
    context = {'task_status':res.ready()}
    return render(request, 'progress.html', context)