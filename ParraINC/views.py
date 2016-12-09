from .models import Empleado_Jefe, Empleado_Almacen, Empleado_Calidad, Empleado_Produccion, Inventario, Pedido
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, FormView
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse_lazy
from .forms import OrderForm, User_Form

# Create your views here.
def home(request):
    return render(request, 'ParraINC/home.html')

def quality(request):
    orders = Pedido.objects.all
    return render(request, 'ParraINC/quality.html',{'orders': orders})

def Delete_Order(request, pk):
    order = get_object_or_404(Pedido, pk=pk)
    order_ipk = order.pk
    order.delete()
    return render(request, "ParraINC/quality.html")

def Order_detail(request, pk):
    order = get_object_or_404(Pedido, pk=pk)
    return render(request, 'ParraINC/order_detail.html', {'order': order})

class Reports(ListView):
    template_name = 'ParraINC/reports.html'
    model = Pedido

    def get_context_data(self, **kwargs):
        ctx = super(Reports, self).get_context_data(**kwargs)
        ctx['Empleado_Almacen'] = Empleado_Almacen.objects.all()
        ctx['Empleado_Jefe'] = Empleado_Jefe.objects.all()
        ctx['Empleado_Calidad'] = Empleado_Calidad.objects.all()
        ctx['Empleado_Produccion'] = Empleado_Produccion.objects.all()
        ctx['Inventario'] = Inventario.objects.all()
        return ctx

def Order_new(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            return redirect('ParraINC.views.Order_Edit', pk=order.pk)
    else:
        form = OrderForm()
    return render(request, 'ParraINC/order_edit.html', {'form': form})

def Order_edit(request, pk):
    order = get_object_or_404(Pedido, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            return redirect('ParraINC.views.Order_detail', pk=order.pk)
    else:
        form = OrderForm(instance=order)
    return render(request, 'ParraINC/order_edit.html', {'form': form})

class SignUp(FormView):
    template_name = 'ParraINC/SingUp.html'
    form_class = User_Form
    success_url = reverse_lazy('home_view')

    def form_valid(self, form):
        p = form.save()
        p.puesto = form.cleaned_data['puesto']
        p.save()
        return super(SignUp, self).form_valid(form)
