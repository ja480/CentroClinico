from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Patient, Consult


class PatientCreateView(LoginRequiredMixin ,CreateView):
    
    model = Patient
    template_name = 'patients/register.html'
    fields = ['genero']
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class PatientUpdateView(LoginRequiredMixin, UpdateView):

    model = Patient
    login_url = reverse_lazy('accounts:login')
    template_name = 'accounts/update_user.html'
    fields = ['genero']
    success_url = reverse_lazy('accounts:index')

    def get_object(self):
        user = self.request.user
        try:
            return Patient.objects.get(user=user)
        except Patient.DoesNotExist:
            return None
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        

class ConsultCreateView(LoginRequiredMixin, CreateView):

    model = Consult
    login_url = 'accounts:login'
    template_name = 'patients/register.html'
    fields = ['diary']
    success_url = reverse_lazy('patients:consult_list')
    
    def form_valid(self, form):
        try:
            form.instance.patient = Patient.objects.get(user=self.request.user)
            form.save()
        except IntegrityError as e:
            if 'UNIQUE constraint failed' in e.args[0]:
                messages.warning(self.request, 'No puedes reservar esta cita')
                return HttpResponseRedirect(reverse_lazy('patients:consult_create'))
        except Patient.DoesNotExist:
            messages.warning(self.request, 'Complete su registro')
            return HttpResponseRedirect(reverse_lazy('patients:patient_register'))
        messages.info(self.request, 'Consulta reservada con exito!')
        return HttpResponseRedirect(reverse_lazy('patients:consult_list'))
    
class ConsultUpdateView(LoginRequiredMixin, UpdateView):

    model = Consult
    login_url = 'accounts:login'
    template_name = 'patients/register.html'
    fields = ['diary']
    success_url = reverse_lazy('doctors:consult_list')
    
    def form_valid(self, form):
        form.instance.patient = Patient.objects.get(user=self.request.user)
        return super().form_valid(form)
    
class ConsultDeleteView(LoginRequiredMixin, DeleteView):
    model = Consult
    success_url = reverse_lazy('patients:consult_list')
    template_name = 'form_delete.html'

    def get_success_url(self):
        messages.success(self.request, "Consulta reservada con exito!")
        return reverse_lazy('patients:consult_list')


class ConsultListView(LoginRequiredMixin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'patients/consult_list.html'

    def get_queryset(self):
        user=self.request.user
        try:
            patient = Patient.objects.get(user=user)
        except Patient.DoesNotExist:
            messages.warning(self.request, 'Crea una Consulta')
            return None
        try:
            consults = Consult.objects.filter(patient=patient).order_by('-pk')
        except Consult.DoesNotExist:
            messages.warning(self.request, 'Crea una Consulta')
            return None
        return consults


patient_register = PatientCreateView.as_view()
patient_update = PatientUpdateView.as_view()
consult_list = ConsultListView.as_view()
consult_register = ConsultCreateView.as_view()
consult_update = ConsultUpdateView.as_view()
consult_delete = ConsultDeleteView.as_view()