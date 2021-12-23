from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
from django.core.mail import send_mail

# Create your views here.


def index(request):

    return render(request, 'pages/home.html ')
def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name'],
        from_email = request.POST['message-email'],
        message_type = request.POST['message_type'],

        #send an email
        send_mail( 'ha tran', 'Complaint', 'from_email', ['mienmien192@gmail.com'],
                   fail_silently=False)

        return render(request, 'pages/contact.html', {'message_name': message_name},)
    else:
        return render(request, 'pages/contact.html')
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST) #dua dlieu nguoi nhap reg vao form
        if form.is_valid(): # khi call valid thi ktra dc cac rang buoc
            form.save()
            return HttpResponseRedirect('/') # khi dki thanh cong thi quay ve trang chu.
    return render(request, 'pages/register.html', {'form':form})

def bookTicket(request):
    if request.method == 'POST':
        displayName = request.POST['nameDisplay'],
        dispNum = request.POST['NumberDisplay'],
        dispSeat = request.POST['seatsDisplay'],

        send_mail('ha tran', 'dispNum','dispSeat', 'from_email', ['mienmien192@gmail.com'],
                  fail_silently=False)
        return render(request, 'pages/bookTicket.html', {'displayName':displayName})
    else:
        return render(request, 'pages/bookTicket.html')

def aboutUs(request):
    return render(request, 'pages/aboutUs.html')
def detailproduct(request):
    return render(request, 'pages/detailproduct.html')
def profile(request):
    return render(request, 'pages/profile.html')
def dashboard(request):
    return render(request, 'pages/dashboard.html')
def artist(request):
    return render(request, 'pages/artist.html')
def art1(request):
    return render(request, 'pages/bichphuong.html')
def art2(request):
    return render(request, 'pages/taylorswift.html')
def art3(request):
    return render(request, 'pages/maroon5.html')
def art4(request):
    return render(request, 'pages/taeyeon.html')
def art5(request):
    return render(request, 'pages/blackpink.html')
def art6(request):
    return render(request, 'pages/highlight.html')
def art7(request):
    return render(request, 'pages/chillies.html')
def event1(request):
    return render(request, 'pages/TTTP.html')
def event2(request):
    return render(request, 'pages/BlackPink1.html')

