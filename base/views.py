from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Customer,Order,B_models,Types,Engine,Staff
from .forms import OrderForm,CreateUserForm,CustomerForm,BikeForm,EngineForm
from django.contrib import messages
from .filters import OrderFilter

from .decorators import unauthenticated_user,allowed_users,admin_only

# Create your views here.

from django.contrib.auth.models import Group
def landing(request):
    return render(request,'base/landing.html')

# Singin & Singup
@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method=='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user=form.save()
                username=form.cleaned_data.get('username')

                group =Group.objects.get(name='staff')
                user.groups.add(group)
                
                Staff.objects.create(user=user,name=user.username)

                messages.success(request,'Account was created for '+ username)
                return redirect('base:login')
    context={'form':form}
    return render(request,'base/register.html',context)
             
@unauthenticated_user
def loginpage(request):
    if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('base:dashboard')
            else:
                messages.info(request,'Email or Password is incorrect! ')
    context={}
    return render(request,'base/login.html') 
                     
def logoutpage(request):
    logout(request)
    return redirect('base:login')


# dashboard
@login_required(login_url='base:login')
@allowed_users(allowed_roles=['admin','staff'])
def dashboard(request):
    total_order=Order.objects.all().order_by('-date_created')
    customers=Customer.objects.all()
    delivered=Order.objects.filter(status='Delivered').count()
    pending=Order.objects.filter(status='Pending').count()
    context={'total_order':total_order,'delivered':delivered,'pending':pending,'customers':customers}
    return render(request,'base/dashboard.html',context)    

@login_required(login_url='base:login')
@allowed_users(allowed_roles=['admin','staff'])
def bikes(request):

    q = request.GET.get('q') if request.GET.get('q') != None else '1'
    types=Types.objects.all()
    bike_models=B_models.objects.filter(type_id=q)
    context={'types':types,'bike_models':bike_models}
    return render(request,'base/bikes.html',context) 



# Customer
@login_required(login_url='base:login')
@allowed_users(allowed_roles=['admin','staff'])
def customer(request,pk):
    
    customer=Customer.objects.get(id=pk)
    models=B_models.objects.all()
    orders=customer.order_set.all()
    number_of_order=orders.count()
    
    myfilter=OrderFilter(request.GET,queryset=orders)
    orders=myfilter.qs

    context={'customer':customer,'orders':orders,'numbers':number_of_order,'models':models,'myfilter':myfilter}
    return render(request,'base/customer.html',context)    

@login_required(login_url='base:login')
@allowed_users(allowed_roles=['admin'])
def update_customer(request,pk):
    customer=Customer.objects.get(id=pk)
    form=CustomerForm(instance=customer)

    if request.method=='POST':
        form=CustomerForm(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request,'base/update.html',context)
    


# Order
@login_required(login_url='base:login')
@allowed_users(allowed_roles=['admin'])
def create_order(request,pk):
    # OrderFormSet=inlineformset_factory(Customer,Order,fields=('model_id','status'),extra=3)
   
    customer=Customer.objects.get(id=pk)
    # formset=OrderFormSet(queryset=Order.objects.none(),instance=customer)
    form = OrderForm(initial={'customer':customer})

    if request.method=='POST':
        form=OrderForm(request.POST)
        # formset=OrderFormSet(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('base:dashboard')

    context={'form':form}
    return render(request,'base/order_form.html',context)

@login_required(login_url='base:login')
@allowed_users(allowed_roles=['admin','staff'])
def update_order(request,pk):
    order=Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method=='POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('base:dashboard')
    context={'form':form}
    return render(request,'base/order_form.html',context)

@login_required(login_url='base:login')
@allowed_users(allowed_roles=['admin','staff'])
def delete_order(request,pk):
    order=Order.objects.get(id=pk)

    if request.method=='POST':
        order.delete()
        return redirect('base:dashboard')
    context={'obj':order}
    return render(request,'base/delete.html',context)        


# Bikes
@login_required(login_url='base:login')
@allowed_users(allowed_roles=['admin','staff'])
def details(request,pk):
    model=B_models.objects.get(id=pk)
    data=Engine.objects.get(model_id=pk)
    context={'data':data,'model':model}
    return render(request,'base/bike_details.html',context)  


@login_required(login_url='base:login')
@allowed_users(allowed_roles=['admin','staff'])
def update(request,pk):
    model=B_models.objects.get(id=pk)
    form=BikeForm(instance=model)

    if request.method == 'POST':
        form = BikeForm(request.POST,request.FILES,instance=model)
        if form.is_valid():
            form.save()
            return redirect('base:bikes')

    context={'form':form}
    return render(request,'base/update.html',context)


@login_required(login_url='base:login')
@allowed_users(allowed_roles=['admin','staff'])
def delete_bike(request,pk):
    model=B_models.objects.get(id=pk)

    if request.method=='POST':
        model.delete()
        return redirect('base:dashboard')
    context={'obj':model}
    return render(request,'base/delete.html',context)   

@login_required(login_url='base:login')
@allowed_users(allowed_roles=['admin','staff'])
def update_details(request,pk):
    detail=Engine.objects.get(id=pk)
    form=EngineForm(instance=detail)

    if request.method == 'POST':
        form = EngineForm(request.POST,request.FILES,instance=detail)
        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request,'base/update.html',context)    