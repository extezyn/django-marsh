from multiprocessing import context
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, DetailView, UpdateView
from basket.forms import BasketAddProductForm
from .models import Equipment, Category, Client, Rental, DamageReport, Payment, Employee, Maintenance, Order, Pos_order
from .forms import LoginForm, RegistrationForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

# Create your views here.
def main_view(request):
    return render(request, 'main.html')

def contact_view(request):
    return render(request, 'contact.html')

def about_view(request):
    return render(request, 'about.html')

def cart_view(request):
    return render(request, 'cart.html')

def categories_view(request):
    return render(request, 'categories.html')

def products_view(request):
    return render(request, 'products.html')

class equipmentListView(ListView):
    model = Equipment
    template_name = 'equipment/equipment_list.html'
    context_object_name = 'equipment'

class equipmentDetailView(DetailView):
    model = Equipment
    template_name = 'equipment/equipment_detail.html'
    context_object_name = 'equipment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_basket'] = BasketAddProductForm
        return context

class equipmentUpdateView(UpdateView):
    model = Equipment
    template_name = 'equipment/equipment_form.html'
    fields = '__all__'
    success_url = reverse_lazy('equipment_list')

class equipmentDeleteView(DeleteView):
    model = Equipment
    template_name = 'equipment/equipment_delete.html'
    success_url = reverse_lazy('equipment_list') 
 
class equipmentCreateView(CreateView):
    model = Equipment
    template_name = 'equipment/equipment_form.html'
    fields = '__all__'
    success_url = reverse_lazy('equipment_list')

class EmployerListView(ListView):
    model = Employee
    template_name = 'employer/employer_list.html'
    context_object_name = 'employers'
    paginate_by = 10

class EmployerDetailView(DetailView):
    model = Employee
    template_name = 'employer/employer_detail.html'
    context_object_name = 'employer'

class EmployerCreateView(CreateView):
    model = Employee
    template_name = 'employer/employer_form.html'
    fields = '__all__'
    success_url = reverse_lazy('employer_list')

class EmployerUpdateView(UpdateView):
    model = Employee
    template_name = 'employer/employer_form.html'
    fields = '__all__'
    success_url = reverse_lazy('employer_list')

class EmployerDeleteView(DeleteView):
    model = Employee
    template_name = 'employer/employer_delete.html'
    success_url = reverse_lazy('employer_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employer'] = self.get_object()  
        return context

# Client Views
class ClientListView(ListView):
    model = Client
    template_name = 'client/client_list.html'
    context_object_name = 'clients'
    paginate_by = 10

class ClientDetailView(DetailView):
    model = Client
    template_name = 'client/client_detail.html'
    context_object_name = 'client'

class ClientCreateView(CreateView):
    model = Client
    template_name = 'client/client_form.html'
    fields = '__all__'
    success_url = reverse_lazy('client_list')

class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'client/client_form.html'
    fields = '__all__'
    success_url = reverse_lazy('client_list')

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client/client_delete.html'
    success_url = reverse_lazy('client_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client'] = self.get_object()  
        return context


# Payment Views
class PaymentListView(ListView):
    model = Payment
    template_name = 'payment/payment_list.html'
    context_object_name = 'payments'
    paginate_by = 10

class PaymentDetailView(DetailView):
    model = Payment
    template_name = 'payment/payment_detail.html'
    context_object_name = 'payment'

class PaymentCreateView(CreateView):
    model = Payment
    template_name = 'payment/payment_form.html'
    fields = '__all__'
    success_url = reverse_lazy('payment_list')

class PaymentUpdateView(UpdateView):
    model = Payment
    template_name = 'payment/payment_form.html'
    fields = '__all__'
    success_url = reverse_lazy('payment_list')

class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'payment/payment_delete.html'
    success_url = reverse_lazy('payment_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['payment'] = self.get_object()  
        return context

# Rental Views
class RentalListView(ListView):
    model = Rental
    template_name = 'rental/rental_list.html'
    context_object_name = 'rentals'
    paginate_by = 10

class RentalDetailView(DetailView):
    model = Rental
    template_name = 'rental/rental_detail.html'
    context_object_name = 'rental'

class RentalCreateView(CreateView):
    model = Rental
    template_name = 'rental/rental_form.html'
    fields = '__all__'
    success_url = reverse_lazy('rental_list')

class RentalUpdateView(UpdateView):
    model = Rental
    template_name = 'rental/rental_form.html'
    fields = '__all__'
    success_url = reverse_lazy('rental_list')

class RentalDeleteView(DeleteView):
    model = Rental
    template_name = 'rental/rental_delete.html'
    success_url = reverse_lazy('rental_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rental'] = self.get_object()  
        return context

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('main_view')
    else:
        form = AuthenticationForm()
    context = {
            'form': form
        }
    return render(request, 'auth/login.html', context)

def registration_user(request):
    if request.method =="POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            login(request, form.save())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('main_view')
    else:
        form = RegistrationForm()
    context = {
            'form': form
    }
    return render(request, 'auth/registration.html', context)

def logout_user(request):
    logout(request)
    return redirect('main_view')