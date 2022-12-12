from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Doctor, Diary


class TestMixinIsAdmin(UserPassesTestMixin):
    def test_func(self):
        is_admin_or_is_staff = self.request.user.is_superuser or \
            self.request.user.is_staff
        return bool(is_admin_or_is_staff)

    def handle_no_permission(self):
        messages.error(
            self.request, "No tienes permisos"
        )
        return redirect("accounts:index")

class DoctorCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Doctor
    login_url = 'accounts:login'
    template_name = 'doctors/register.html'
    fields = ['name', 'email', 'speciality']
    success_url = reverse_lazy('doctors:doctor_list')
    
class DoctorListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'doctors/doctor_list.html'

    def get_queryset(self):
        return Doctor.objects.all().order_by('-pk')

class DiaryCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Diary
    login_url = 'accounts:login'
    template_name = 'doctors/diary_register.html'
    fields = ['doctor', 'day', 'schedule', 'consultingroom']
    success_url = reverse_lazy('doctors:diary_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class DiaryUpdateView(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):

    model = Diary
    login_url = 'accounts:login'
    template_name = 'doctors/diary_register.html'
    fields = ['doctor', 'day', 'schedule', 'consultingroom']
    success_url = reverse_lazy('doctors:diary_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class DiaryDeleteView(LoginRequiredMixin, TestMixinIsAdmin, DeleteView):
    
    model = Diary
    success_url = reverse_lazy('doctors:diary_list')
    template_name = 'form_delete.html'

    def get_success_url(self):
        messages.success(self.request, "Appointment pulled apart sucefully!")
        return reverse_lazy('doctors:diary_list')


class DiaryListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'doctors/diary_list.html'

    def get_queryset(self):
        return Diary.objects.filter().order_by('-pk')
    
doctor_register = DoctorCreateView.as_view()
doctor_list = DoctorListView.as_view()
diary_register = DiaryCreateView.as_view()
diary_update = DiaryUpdateView.as_view()
diary_list = DiaryListView.as_view()
diary_delete = DiaryDeleteView.as_view()