from django.shortcuts import render
from .forms import OrderForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from PyPDF2 import PdfReader

# Create your views here.

def homepage(request):
    return render(request, 'printtextpage/homepage.html')

def print(request):
    return render(request, 'printtextpage/print.html')

def orderform(request):
    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            subject = "Print Order - " + str(form.cleaned_data['email'])
            attach = request.FILES['docupload']

            if attach.name.endswith(".pdf"):
                reader = PdfReader(attach)
                totalpages = len(reader.pages)
            else:
                totalpages = form.cleaned_data['pagecount']

            body = {
                'Name': "Name: " + form.cleaned_data['name'], 
                'Mobile No. (WhatsApp No.)': "Mobile No. (WhatsApp No.): " + form.cleaned_data['mobno'], 
                'Address': "Address: " + form.cleaned_data['address'],
                'Print Colour': "Print Colour: " + form.cleaned_data['printcolour'],
                'Page Type': "Page Type: " + form.cleaned_data['pagetype'],
                'Cover Option': "Cover Option: " + form.cleaned_data['coveroption'],
                'Binding Option': "Binding Option: " + form.cleaned_data['bindingoption'],
                'Page Count': "Page Count: " + str(totalpages),
                'Number of Copies': "Number of Copies: " + str(form.cleaned_data['copies']),
                'Extra Comment': "Extra Comment: " + form.cleaned_data['extracomment'],
            }

            message = "\n".join(body.values())

            if totalpages < 1:
                messages.info(request, 'Please set page count for Non PDF file!')
            else:
                try:
                    attach.file.seek(0)
                    mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, ['print_text@yahoo.com'])
                    mail.attach(attach.name, attach.read(), attach.content_type)
                    mail.send()
                    messages.info(request, 'Order placed successfully!')
                except Exception as ex:
                    messages.info(request, ex)

    context = {'form':form}
    
    return render(request, 'printtextpage/orderform.html', context)

def aboutus(request):
    return render(request, 'printtextpage/aboutus.html')

def acadproject(request):
    return render(request, 'printtextpage/acadproject.html')

def studymaterial(request):
    return render(request, 'printtextpage/studymaterial.html')

def studyguide(request):
    return render(request, 'printtextpage/studyguide.html')

def homework(request):
    return render(request, 'printtextpage/homework.html')

def notebook(request):
    return render(request, 'printtextpage/notebook.html')

def companyproject(request):
    return render(request, 'printtextpage/companyproject.html')

def businesscard(request):
    return render(request, 'printtextpage/businesscard.html')

def resume(request):
    return render(request, 'printtextpage/resume.html')

def letterhead(request):
    return render(request, 'printtextpage/letterhead.html')

def billinvoice(request):
    return render(request, 'printtextpage/billinvoice.html')

def personaldocs(request):
    return render(request, 'printtextpage/personaldocs.html')

def certificate(request):
    return render(request, 'printtextpage/certificate.html')

def presentation(request):
    return render(request, 'printtextpage/presentation.html')

def photoglossy(request):
    return render(request, 'printtextpage/photoglossy.html')

def ebook(request):
    return render(request, 'printtextpage/ebook.html')