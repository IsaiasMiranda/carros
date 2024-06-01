from cars.models import Car
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

class ShowCar(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        ListarCars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')

        if search:
            ListarCars = ListarCars.filter(MODEL__icontains=search)
        return ListarCars

class CarDetail(DetailView):
    model = Car
    template_name = 'car_detail.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCar(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'
    
@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdate(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})
@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDelete(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'