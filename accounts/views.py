from django.shortcuts import render, redirect
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required
from .forms import ForgotPasswordForm
from django.contrib import messages
from django.http import HttpResponse,Http404
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.conf import settings


from .models import User
from .forms import UserCustomCreationForm,UserViewerCreationForm


class RegistraUsuario(CreateView):

    model = User
    template_name = 'registro.html'
    form_class = UserCustomCreationForm
    success_url = reverse_lazy('registro_sucesso')

registro = RegistraUsuario.as_view()


def user_active(request, token):
    user = User.objects.get(token=token)
    user.is_active = True
    # if user.is_masteruser is True:
        # user.user_master = user.pk
    user.save()

    return redirect('login')

def recupera_conta(request):
    form = ForgotPasswordForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
        except:
            user = None
        if user:
            token = default_token_generator.make_token(user)
            from templated_email import send_templated_mail
            send_templated_mail(
                template_name='email_recupera_conta',
                from_email='michel.carvalho22@gmail.com',
                recipient_list=[user.email],
                context = {
                    'domain' : settings.SITE_DOMAIN,
                    'user' : user,
                    'token' : token
                },


            )

            return render(request,template_name='recupera_info.html')

    context = {
        'form' : form
    }

    return render(request,'recupera_conta.html',context)









def reset_password(request,pk):
    form = ForgotPasswordForm(request.POST or None)
    user = User.objects.get(pk=pk)
    if user:
       token = default_token_generator.make_token(user)
       from templated_email import send_templated_mail
       send_templated_mail(
          template_name='email_recupera_conta',
          from_email='michel.carvalho22@gmail.com',
          recipient_list=[user.email],
          context = {
         'domain' : settings.SITE_DOMAIN,
         'user' : user,
         'token' : token
         },


       )
       messages.success(request, 'Solicitação realizada. Em breve o usuário receberá um e-mail com a nova senha')
       return redirect('users_viewers_list')

    context = {
        'form' : form
    }

    return render(request,'recover_account.html',context)



def registro_sucesso(request):

    return render(request,'sucesso_conta.html')




def create_new_password(request,id,token):
    user = User.objects.get(id=id)
    if default_token_generator.check_token(user,token):
        form = SetPasswordForm(user,request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login')
        context = {
            'form' : form
         }
        return render(request,'nova_senha.html', context)

    raise Http404


@login_required
def users_viewers_list(request):

    if request.is_ajax():
        template_name = '_table_users_viewers.html'
    else:
        template_name = 'users_viewers_list.html'


    users_viewers = User.objects.filter(user_master=request.user,is_masteruser=False)


    context = {
        'dominio' : settings.SITE_DOMAIN,
        'users_viewers' : users_viewers,
    }
    return render(request,template_name,context)



class RegisterUserViewer(LoginRequiredMixin, CreateView):


        def get_template_names(self):
            if self.request.is_ajax():
                return ["_create_viewer.html"]
            else:
                raise Http404

        def get_success_url(self):
            return reverse_lazy('users_viewers_list')

        model = User
        form_class = UserViewerCreationForm

        def form_valid(self, form):
            userv = form.save(commit=False)
            userv.user_master = self.request.user.user_master
            userv.is_masteruser = False
            userv.is_active = True
            userv.save()

            if self.request.is_ajax():
                context = self.get_context_data(form=form, ok='ok', success=True)
                return self.render_to_response(context)
            else:
                return redirect(self.get_success_url())


register_viewer = RegisterUserViewer.as_view()



class EditUserViewer(LoginRequiredMixin,UpdateView):

    def get_template_names(self):
        if self.request.is_ajax():
            return ["_alter_viewer.html"]
        else:
           raise Http404

    model = User
    fields = ['name','email','is_active','tel_user']

    def get_success_url(self):
        return reverse_lazy('users_viewers_list')

    def form_valid(self,form):
        form.save()

        if self.request.is_ajax():
            context = self.get_context_data(form=form,success=True)
            return self.render_to_response(context)
        else:
            return redirect(self.get_success_url())

edit_viewer = EditUserViewer.as_view()




