from django.shortcuts import render,HttpResponse
from Base.forms import UnemploymentForm
from Base.models import Unemployment
# Create your views here.
def home(request):
    if request.method=='POST':
    # to get the form Data display in a new page 
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        return HttpResponse(f'''<h1>Forms Submitted <br>
                            name:{name} <br>
                            email:{email} <br>
                            password:{password} <br>
                            cpassword:{cpassword} <br>
                            </h1>''')

        # print(request.POST)
    else:
        return render(request,'index.html')

    # return HttpResponse("Hello, Django!")
   
def emp_register(request):
    if request.method=='POST':
        form=UnemploymentForm(request.POST)
        if form.is_valid():
           return HttpResponse(" Valid Form Submitted ")
        else:
            render(request,'emp_register.html',{'form':form})
    else:
        form=UnemploymentForm()
        return render(request,'emp_register.html',{'form':form})


def register(request):
    form=UnemploymentForm()
   
    if request.method=='POST':
        #  form=UnemploymentForm() ->to display the structure alone 
        form=UnemploymentForm(request.POST) #to display structure along with values
        if form.is_valid():

            name=form.cleaned_data['name']
            designation=form.cleaned_data['designation']
            email=form.cleaned_data['email']
            phone=form.cleaned_data['phone']
            address=form.cleaned_data['address']
            experience=form.cleaned_data['experience']
            current_ctc=form.cleaned_data['current_ctc']
            # Unemployee.objects.create(columns :values) -->anoter method for creating objects 
            # no save () is needed 
            emp=Unemployment(
                name=name,
                designation=designation,
                email=email,
                phone=phone,
                address=address,
                experience=experience,
                current_ctc=current_ctc 
            )
            emp.save()
        else:
            print("Invalid form")
        form=UnemploymentForm(request.POST)

    
    context={
        'form':form #error message
    }
    return render(request,'register.html',context)
