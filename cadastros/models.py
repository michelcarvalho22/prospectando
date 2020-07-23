from django.db import models

# Create your models here.


class Lead(models.Model):

    # informação do dono da conta (usuario Master)
    master_user = models.ForeignKey('accounts.User',models.CASCADE,verbose_name='Usuário Master')

    # dados principais
    cnpj_cpf = models.CharField('CNPJ/CPF',max_length=20, null=True,blank=True)
    razao = models.CharField('Razão/Nome', max_length=60)
    fantasia = models.CharField('Fantasia', max_length=40, blank=True,null=True)

    # endereço
    cep = models.CharField('CEP', max_length=12, blank=True, null=True)
    endereco = models.CharField('Endereço',max_length=50,blank=True,null=True)
    numero = models.CharField('Nº',max_length=10, blank=True,null=True)
    complemento = models.CharField('Complemento', max_length=30,blank=True,null=True)
    bairro = models.CharField('Bairro', max_length=40, blank=True, null=True)
    cidade = models.CharField('Cidade', max_length=30, blank=True, null=True)
    uf = models.CharField('UF', max_length=2, blank=True, null=True)

    # dados contato
    email = models.EmailField('Email',max_length=100)
    telefone = models.CharField('Telefone',max_length=20)

    # outros dados
    data_cadastro = models.DateTimeField('Data de cadastro', auto_now_add=True,blank=True,null=True)
    situacao = models.BooleanField('Ativo',default=True)


    class Meta:
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'
        unique_together = [
           ('master_user', 'cnpj_cpf')
        ]

    def __str__(self):
        return self.razao


class StatusProspeccao(models.Model):

    master_user = models.ForeignKey('accounts.User', models.CASCADE, verbose_name='Usuário Master')

    status_desc = models.CharField('Descrição',max_length=40)
    intervalo = models.IntegerField('Intervalo de retorno (dias)')


    class Meta:
        verbose_name = 'Status Prospecção'
        unique_together = [
            ('master_user', 'status_desc')
        ]


    def __str__(self):
        return self.status_desc


class FluxoProspeccao(models.Model):


    master_user = models.ForeignKey('accounts.User', models.CASCADE, verbose_name='Usuário Master')

    desc_fluxo = models.CharField('Descrição do Fluxo',max_length=60)
    qtd_passos = models.IntegerField('Quantidade Passos')


    passo1 = models.ForeignKey('cadastros.StatusProspeccao',models.CASCADE,verbose_name='Passo1',
                               related_name='passo1' ,null=True, blank=True)
    qtd_contatos1 = models.IntegerField('Quantidade Contatos',default=0)
    passo_falha1 = models.ForeignKey('cadastros.StatusProspeccao', models.CASCADE,
                               verbose_name='Próximo Passo - Falha', related_name='passo_falha1',
                               null=True, blank=True)


    passo2 = models.ForeignKey('cadastros.StatusProspeccao', models.CASCADE, verbose_name='Passo2',
                               related_name='passo2',null=True, blank=True)
    qtd_contatos2 = models.IntegerField('Quantidade Contatos',default=0)
    passo_falha2 = models.ForeignKey('cadastros.StatusProspeccao', models.CASCADE,
                                     verbose_name='Próximo Passo - Falha', related_name='passo_falha2',
                                     null = True, blank = True)


    passo3 = models.ForeignKey('cadastros.StatusProspeccao', models.CASCADE, verbose_name='Passo3',
                               related_name='passo3',null = True, blank = True)
    qtd_contatos3 = models.IntegerField('Quantidade Contatos',default=0)
    passo_falha3 = models.ForeignKey('cadastros.StatusProspeccao', models.CASCADE,
                                     verbose_name='Próximo Passo - Falha', related_name='passo_falha3',
                                     null=True, blank=True)


    class Meta:
        verbose_name = 'Fluxo Prospecção'
        unique_together = [
            ('master_user','desc_fluxo')
        ]

    def __str__(self):
        return self.desc_fluxo
