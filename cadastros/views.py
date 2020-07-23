from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,TemplateView,UpdateView,FormView
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from accounts.models import User
from .models import Lead,StatusProspeccao,FluxoProspeccao
from django.conf import settings
from .forms import FormCreateFluxo

# LEAD

@login_required
def leads_lista(request):
    template_name = 'leads_lista.html'
    leads = Lead.objects.filter(master_user=request.user.user_master)
    context = {
        'lead' : leads,
        'dominio': settings.SITE_DOMAIN,
    }
    return render(request,template_name,context)



class CriaLead(LoginRequiredMixin,CreateView):

    def get_template_names(self):
        if self.request.is_ajax():
            return ["_cria_lead.html"]
        else:
            raise Http404


    model = Lead
    fields = ['cnpj_cpf','razao','fantasia','cep','endereco','numero','complemento','bairro','cidade','uf',
              'email','telefone']

    def get_success_url(self):
        return reverse_lazy('leads_lista')

    def form_valid(self,form):
        Lead = form.save(commit=False)
        Lead.master_user = self.request.user.user_master
        if Lead.cnpj_cpf == None:
            Lead.cnpj_cpf = Lead.pk
        Lead.save()

        if self.request.is_ajax():
            context = self.get_context_data(form=form,success=True)
            return self.render_to_response(context)
        else:
            return redirect(self.get_success_url())


class EditLead(LoginRequiredMixin,UpdateView):
    def get_template_names(self):
        if self.request.is_ajax():
            return ["_edit_lead.html"]
        else:
            raise Http404


    model = Lead
    fields = ['cnpj_cpf','razao','fantasia','cep','endereco','numero','complemento','bairro','cidade','uf',
              'email','telefone']

    def get_success_url(self):
        return reverse_lazy('leads_lista')

    def form_valid(self,form):
        form.save()

        if self.request.is_ajax():
            context = self.get_context_data(form=form,success=True)
            return self.render_to_response(context)
        else:
            return redirect(self.get_success_url())




@login_required
def delete_lead(request, pk):
    lead = get_object_or_404(Lead,master_user=request.user.user_master,pk=pk)

    try:
        lead.delete()
        messages.success(request, 'Registro removido com sucesso !')
    except:
         messages.danger(request, 'Registro vinculado a movimentações, exclusão não ocorreu!')

    return redirect('leads_lista')



# FIM LEAD

# Status Prospecção

@login_required
def status_lista(request):
    template_name = 'status_lista.html'
    status = StatusProspeccao.objects.filter(master_user=request.user.user_master)
    context = {
        'status': status,
        'dominio': settings.SITE_DOMAIN,
    }
    return render(request, template_name, context)



class CriaStatus(LoginRequiredMixin,CreateView):

    def get_template_names(self):
        if self.request.is_ajax():
            return ["_cria_status.html"]
        else:
            raise Http404


    model = StatusProspeccao
    fields = ['status_desc','intervalo']

    def get_success_url(self):
        return reverse_lazy('status_lista')

    def form_valid(self,form):
        Status = form.save(commit=False)
        Status.master_user = self.request.user.user_master
        Status.save()

        if self.request.is_ajax():
            context = self.get_context_data(form=form,success=True)
            return self.render_to_response(context)
        else:
            return redirect(self.get_success_url())



class EditStatus(LoginRequiredMixin,UpdateView):
    def get_template_names(self):
        if self.request.is_ajax():
            return ["_edit_status.html"]
        else:
            raise Http404


    model = StatusProspeccao
    fields = ['status_desc', 'intervalo']

    def get_success_url(self):
        return reverse_lazy('status_lista')

    def form_valid(self,form):
        form.save()

        if self.request.is_ajax():
            context = self.get_context_data(form=form,success=True)
            return self.render_to_response(context)
        else:
            return redirect(self.get_success_url())


@login_required
def delete_status(request, pk):
    status = get_object_or_404(StatusProspeccao,master_user=request.user.user_master,pk=pk)

    try:
        status.delete()
        messages.success(request, 'Registro removido com sucesso !')
    except:
         messages.danger(request, 'Registro vinculado a movimentações, exclusão não ocorreu!')

    return redirect('status_lista')




# FIM Status Prospecção


# FLUXO WORKFLOW

@login_required
def fluxo_lista(request):
    template_name = 'fluxo_lista.html'
    fluxo = FluxoProspeccao.objects.filter(master_user=request.user.user_master)
    context = {
        'fluxo': fluxo,
        'dominio': settings.SITE_DOMAIN,
    }
    return render(request, template_name, context)



class CriaFluxo(LoginRequiredMixin,CreateView):

    def get_template_names(self):
        if self.request.is_ajax():
            return ["_cria_fluxo.html"]
        else:
            raise Http404


    model = FluxoProspeccao
    form_class = FormCreateFluxo

    def get_success_url(self):
        return reverse_lazy('fluxo_lista')

    def form_valid(self,form):
        Fluxo = form.save(commit=False)
        Fluxo.master_user = self.request.user.user_master
        Fluxo.save()

        if self.request.is_ajax():
            context = self.get_context_data(form=form,success=True)
            return self.render_to_response(context)
        else:
            return redirect(self.get_success_url())
#
#
#
# class EditStatus(LoginRequiredMixin,UpdateView):
#     def get_template_names(self):
#         if self.request.is_ajax():
#             return ["_edit_status.html"]
#         else:
#             raise Http404
#
#
#     model = StatusProspeccao
#     fields = ['status_desc', 'intervalo']
#
#     def get_success_url(self):
#         return reverse_lazy('status_lista')
#
#     def form_valid(self,form):
#         form.save()
#
#         if self.request.is_ajax():
#             context = self.get_context_data(form=form,success=True)
#             return self.render_to_response(context)
#         else:
#             return redirect(self.get_success_url())
#
#
# @login_required
# def delete_status(request, pk):
#     status = get_object_or_404(StatusProspeccao,master_user=request.user.user_master,pk=pk)
#
#     try:
#         status.delete()
#         messages.success(request, 'Registro removido com sucesso !')
#     except:
#          messages.danger(request, 'Registro vinculado a movimentações, exclusão não ocorreu!')
#
#     return redirect('status_lista')






# FIM FLUXO WORKFLOW





edit_lead = EditLead.as_view()
cria_lead = CriaLead.as_view()
cria_status = CriaStatus.as_view()
edit_status = EditStatus.as_view()
cria_fluxo = CriaFluxo.as_view()

