from django.db import models

# Create your models here.

class Sala(models.Model):
    nome = models.CharField(max_length=50, null=False, verbose_name="Nome :")
    obs = models.TextField( verbose_name="Observação")

    def __str__(self):
        return self.nome

class Armario(models.Model):
    nome = models.CharField(max_length=50, null=False, verbose_name="Nome :")
    sigla = models.CharField(max_length=50, null=False, verbose_name="SIGLA :")
    tombo = models.CharField(max_length=50, null=False, verbose_name="Tombo :")
    sala_armario = models.ForeignKey(Sala, on_delete=models.PROTECT, related_name='Sala_armario')
    obs = models.TextField(verbose_name="Observação")

    class Meta:
        verbose_name = u'Modelo'
        verbose_name_plural = u'Armários'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Estante(models.Model):
    nome = models.CharField(max_length=50, null=False, verbose_name="Nome :")
    sigla = models.CharField(max_length=50, null=False, verbose_name="SIGLA :")
    tombo = models.CharField(max_length=50, null=False, verbose_name="Tombo :")
    sala_estante = models.ForeignKey(Sala, on_delete=models.PROTECT, related_name='Sala_esteante')
    obs = models.TextField(verbose_name="Observação")

    class Meta:
        verbose_name = u'Modelo'
        verbose_name_plural = u'Estantes'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Bancada(models.Model):
    nome = models.CharField(max_length=50, null=False, verbose_name="Nome :")
    sigla = models.CharField(max_length=50, null=False, verbose_name="SIGLA :")
    sala_bancada = models.ForeignKey(Sala, on_delete=models.PROTECT, related_name='Sala_Bancada')
    obs = models.TextField( verbose_name="Observação")

    def __str__(self):
        return self.nome


class Prateleira(models.Model):
    nome = models.CharField(max_length=50, null=False, verbose_name="Nome :")
    sigla = models.CharField(max_length=50, null=False, verbose_name="SIGLA :")
    armario_prateleira = models.ForeignKey(Armario, on_delete=models.PROTECT, related_name='Armario_Prateleira')
    bancada_prateleira = models.ForeignKey(Bancada, on_delete=models.PROTECT, related_name='Bancada_Prateleira')
    estante_prateleira = models.ForeignKey(Estante, on_delete=models.PROTECT, related_name='Estante_prateleira')

    def __str__(self):
        return self.nome

class Gaveta(models.Model):
    nome = models.CharField(max_length=50, null=False, verbose_name="Nome :")
    sigla = models.CharField(max_length=50, null=False, verbose_name="SIGLA :")
    armario_gaveta = models.ForeignKey(Armario, on_delete=models.PROTECT, related_name='Armario_gaveta')

    def __str__(self):
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=50, null=False, verbose_name="Nome :")
    sigla = models.CharField(max_length=50, null=False, verbose_name="SIGLA :")
    obs = models.TextField(verbose_name="Observação")

    def __str__(self):
        return self.nome

class Unidade(models.Model):
    nome = models.CharField(max_length=50, null=False, verbose_name="Nome :")
    sigla = models.CharField(max_length=50, null=False, verbose_name="SIGLA :")

    def __str__(self):
        return self.nome

class Origem(models.Model):
    nome = models.CharField(max_length=50, null=False, verbose_name="Nome :")
    sigla = models.CharField(max_length=50, null=False, verbose_name="SIGLA :")

    class Meta:
        verbose_name = u'Modelo'
        verbose_name_plural = u'Origem'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Outros(models.Model):
    nome = models.CharField(max_length=50, null=False, verbose_name="Nome :")
    sigla = models.CharField(max_length=50, null=False, verbose_name="SIGLA :")
    obs = models.TextField( verbose_name="Observação")

    def __str__(self):
        return self.nome


class Diverso(models.Model):
    nome = models.CharField(max_length=100, null=False, verbose_name="Nome :")
    quantidade = models.IntegerField(null=False, verbose_name="Quantidade :")
    u_md = models.ForeignKey(Unidade, on_delete=models.PROTECT, related_name='Unidade')
    ficha_tec = models.ImageField(upload_to='images',null=False, verbose_name="Ficha Técnica :")
    especficacao_t = models.TextField(null=False, verbose_name="Especificação Técnica")
    obs = models.TextField(verbose_name="Observação")
    sala_diversos = models.ForeignKey(Sala, on_delete=models.PROTECT, related_name='Sala_Diversos')
    armario_diversos = models.ForeignKey(Armario, on_delete=models.PROTECT, related_name='Armario_Diversos')
    bancada_diversos = models.ForeignKey(Bancada, on_delete=models.PROTECT, related_name='Bancada_Diversos')
    estante_diversos = models.ForeignKey(Estante, on_delete=models.PROTECT, related_name='Estante_Diversos')
    gaveta_diversos = models.ForeignKey(Gaveta, on_delete=models.PROTECT, related_name='Gaveta_Diversos')

    def __str__(self):
        return self.nome


class Equipamento(models.Model):
    CALIB_CHOICES = (
        ("SIM", "SIM"),
        ("NAO", "NÃO"),
    )
    nome = models.CharField(max_length=100, null=False, verbose_name="Nome :")
    tombo = models.CharField(max_length=20, null=False, verbose_name="Tombo :")
    marca_Equipamento = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name='Marca')
    data_compra = models.DateField(null=False, verbose_name="Data da Compra")
    data_u_m = models.DateField(null=False, verbose_name="Data da Última Manutenção")
    origem = models.ImageField(upload_to='images', verbose_name="Anexar PDF ou imagem :")
    ficha_tec = models.ImageField(upload_to='images', null=False, verbose_name="Ficha Técnica :")
    especficacao_t = models.TextField(verbose_name="Especificação Técnica")
    calibragem = models.CharField(max_length=3, null=False, choices=CALIB_CHOICES)
    obs = models.TextField(verbose_name="Observação :")
    sala_equipamentos = models.ForeignKey(Sala, on_delete=models.PROTECT, related_name='Sala_Equipamentos')
    armario_equipamentos = models.ForeignKey(Armario, on_delete=models.PROTECT, related_name='Armario_Equipamentos')
    bancada_equipamentos = models.ForeignKey(Bancada, on_delete=models.PROTECT, related_name='Bancada_Equipamentos')
    estante_equipamentos = models.ForeignKey(Estante, on_delete=models.PROTECT, related_name='Estante_Equipamentos')
    gaveta_equipamentos = models.ForeignKey(Gaveta, on_delete=models.PROTECT, related_name='Gaveta_Equipamentos')

    def __str__(self):
        return self.nome


class Vidraria(models.Model):
    nome = models.CharField(max_length=100, null=False, verbose_name="Nome :")
    quantidade = models.IntegerField(null=False, verbose_name="Quantidade :")
    ficha_tec = models.ImageField(upload_to='images', verbose_name="Ficha Técnica :")
    especficacao_t = models.TextField( verbose_name="Especificação Técnica")
    obs = models.TextField(verbose_name="Observação")
    sala_vidraria = models.ForeignKey(Sala, on_delete=models.PROTECT, related_name='Sala_Vidraria')
    armario_vidraria = models.ForeignKey(Armario, on_delete=models.PROTECT, related_name='Armario_Vidraria')
    bancada_vidraria = models.ForeignKey(Bancada, on_delete=models.PROTECT, related_name='Bancada_Vidraria')
    estante_vidraria = models.ForeignKey(Estante, on_delete=models.PROTECT, related_name='Estante_Vidraria')
    gaveta_vidraria = models.ForeignKey(Gaveta, on_delete=models.PROTECT, related_name='Gaveta_Vidraria')



    def __str__(self):
        return self.nome

#####################################

class Reagente(models.Model):
    DISPON_CHOICES = (
        ("SIM", "SIM"),
        ("NAO", "NÃO"),
    )
    nome = models.CharField(max_length=100, null=False, verbose_name="Nome :")
    formula_q = models.CharField(max_length=50, null=False, verbose_name="Formula Química :")
    grau_p = models.CharField(max_length=50, null=False, verbose_name="Gráu de Pureza :")
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT, related_name='unidade')
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name='reagente')
    quantidade = models.IntegerField(null=False, verbose_name="Quantidade :")
    data_validade = models.DateField(null=False, verbose_name="Data de Validade")
    controle_pfex = models.CharField(max_length=50, verbose_name="Controle PF / Exercito :")
    ficha_tec = models.ImageField(upload_to='images', verbose_name="Anexar PDF ou imagem :")
    massamolecular = models.CharField(max_length=50, null=False, verbose_name="Massa Molecular :")
    densidade = models.CharField(max_length=50, null=False, verbose_name="Densidade :")
    disponibilidade = models.CharField(max_length=3, null=False, choices=DISPON_CHOICES)
    obs = models.TextField(verbose_name="Observação :")
    sala_reagente = models.ForeignKey(Sala, on_delete=models.PROTECT, related_name='Sala_Reagente')
    armario_reagente = models.ForeignKey(Armario, on_delete=models.PROTECT, related_name='Armario_Reagente')
    bancada_reagente = models.ForeignKey(Bancada, on_delete=models.PROTECT, related_name='Bancada_Reagente')
    estante_reagente = models.ForeignKey(Estante, on_delete=models.PROTECT, related_name='Estante_Reagente')
    gaveta_reagente = models.ForeignKey(Gaveta, on_delete=models.PROTECT, related_name='Gaveta_Reagente')

    def __str__(self):
        return self.nome

### implementar um para muitos reagentes####

class Solucao(models.Model):
        nome = models.CharField(max_length=100, null=False)
        concetracao = models.CharField(max_length=50, null=False)
        reagente = models.ManyToManyField(Reagente)
        data_producao = models.DateField(null=False, verbose_name="data_Producao")
        obs = models.TextField(null=False, verbose_name="Observação :")
        sala_solucao = models.ForeignKey(Sala, on_delete=models.PROTECT, related_name='Sala_Solucao')
        armario_solucao = models.ForeignKey(Armario, on_delete=models.PROTECT, related_name='Armario_Solucao')
        bancada_solucao = models.ForeignKey(Bancada, on_delete=models.PROTECT, related_name='Bancada_Solucao')
        estante_solucao = models.ForeignKey(Estante, on_delete=models.PROTECT, related_name='Estante_Solucao')
        gaveta_solucao = models.ForeignKey(Gaveta, on_delete=models.PROTECT, related_name='Gaveta_Solucao')

        class Meta:
            verbose_name = u'Modelo'
            verbose_name_plural = u'Soluções'
            ordering = ['nome']
        def __str__(self):
            return self.nome


class Aulasprontas(models.Model):
    nome = models.CharField(max_length=200, null=False)
    reagente_ap = models.ForeignKey(Reagente, on_delete=models.PROTECT, related_name='Reagente_Aula')
    quantidade_reagente = models.IntegerField(null=False, verbose_name="Quant_Reagente :")
    solucao_ap = models.ForeignKey(Solucao, on_delete=models.PROTECT, related_name='Solução_Aula')
    quantidade_solucao = models.IntegerField(null=False, verbose_name="Quant_solucao :")
    diverso_ap = models.ManyToManyField(Diverso)
    equepamentos_ap = models.ManyToManyField(Equipamento)
    vidraria_ap = models.ManyToManyField(Vidraria)
    obs_aula_pronta = models.TextField(verbose_name="Observação :")


    class Meta:
        verbose_name = u'Aulasprontas'
        verbose_name_plural = u'Modelos de Aulas Práticas Prontas'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class AulaPratica_COM_Modelo(models.Model):

    TURNO_CHOICES = (
        ("MANHA", "MANHÃ"),
        ("TARDE", "TARDE"),
        ("NOITE", "NOITE"),
    )
    apsala = models.ForeignKey(Sala, on_delete=models.PROTECT, related_name='salaap', verbose_name="Sala")
    data_solicitacao = models.DateField(null=False, blank=False, verbose_name="Data da Solicitação")
    turno = models.CharField(max_length=5, null=False, choices=TURNO_CHOICES)
    data_H_inicio= models.DateTimeField(null=False, blank=False, verbose_name="Data Inicio")
    data_H_final = models.DateTimeField(null=False, blank=False, verbose_name="Data Fim")
    quant_aluno = models.IntegerField(null=False, blank=False, verbose_name="Quantidade de Alunos:")
    aulas_prontas = models.ForeignKey(Aulasprontas, on_delete=models.PROTECT, related_name='Aulasprontas', verbose_name="Modelos de Aulas Prontas")
    obs1 = models.TextField(verbose_name="Observação :")

    class Meta:
        verbose_name = u'AulaPratica'
        verbose_name_plural = u'Aula Prática Com Modelo'
        ordering = ['apsala']

    def __str__(self):
        return self.nome
