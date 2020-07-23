from accounts.models import User
from django import forms
from .models import StatusProspeccao,FluxoProspeccao




class FormCreateFluxo(forms.ModelForm):


    def __init__(self,user,*args,**kwargs):
       super(FormCreateFluxo,self).__init__(*args,**kwargs)

       self.fields['passo1'].queryset = StatusProspeccao.objects.filter(master_user=user.user_master)
       self.fields['passo_falha1'].queryset = StatusProspeccao.objects.filter(master_user=user.user_master)

       self.fields['passo2'].queryset = StatusProspeccao.objects.filter(master_user=user.user_master)
       self.fields['passo_falha2'].queryset = StatusProspeccao.objects.filter(master_user=user.user_master)

       self.fields['passo3'].queryset = StatusProspeccao.objects.filter(master_user=user.user_master)
       self.fields['passo_falha3'].queryset = StatusProspeccao.objects.filter(master_user=user.user_master)

       self.fields['passo1'].empty_label = 'Ecolher um Status para este passo'
       self.fields['passo_falha1'].empty_label = 'Ecolher um Status para este passo'
       self.fields['passo2'].empty_label = 'Ecolher um Status para este passo'
       self.fields['passo_falha2'].empty_label = 'Ecolher um Status para este passo'
       self.fields['passo3'].empty_label = 'Ecolher um Status para este passo'
       self.fields['passo_falha3'].empty_label = 'Ecolher um Status para este passo'

    class Meta:
        model= FluxoProspeccao
        fields = ['desc_fluxo','qtd_passos','passo1','qtd_contatos1','passo_falha1','passo2','passo_falha2',
                  'passo3','passo_falha3']


