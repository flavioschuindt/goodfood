#coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

########################################################################################
class Employee(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER = (
        (MALE, 'Masculino'),
        (FEMALE, 'Feminino'),
    )

    name = models.CharField(
                            max_length=100,
                            verbose_name = _(u'Nome'),
                            )
    salary = models.DecimalField(
                                 max_digits=7,
                                 decimal_places=2,
                                 verbose_name = _(u'Salário')
                                )
    gender = models.CharField(
                              max_length=1,
                              verbose_name = _(u'Sexo'),
                              choices=GENDER,
                              default=MALE,
                            )

    address = models.CharField(
                            max_length=300,
                            verbose_name = _(u'Endereço'),
                            )

    phone_number = models.CharField(
                            max_length=9,
                            verbose_name = _(u'Telefone'),
                            )

    admission_date = models.DateField(
                            verbose_name = _(u'Data de Admissão'),
    )

    is_administrative = models.BooleanField(
                            verbose_name = _(u'Administrativo?'),
                            )

    class Meta:
        verbose_name = _(u'Funcionário')
        verbose_name_plural = _(u'Funcionários')

    def __unicode__(self):
        return self.name


########################################################################################

class Item(models.Model):

    UNIT = (
        ('Kg', 'Kg'),
        ('Un.', 'Un.'),
        ('L', 'L'),
    )

    name = models.CharField(
                            max_length=50,
                            verbose_name = _(u'Nome'),
                            )

    quantity = models.DecimalField(
                            max_digits=10,
                            decimal_places=2,
                            verbose_name = _(u'Quantidade'),
                            default=0,
                            )

    unit = models.CharField(
                            max_length=4,
                            choices = UNIT,
                            verbose_name = _(u'Unidade'),
                            default='Kg',
                            )

    brand = models.CharField(
                            max_length=50,
                            verbose_name = _(u'Marca'),
                            )


    class Meta:
        verbose_name = _(u'Item da Dispensa')
        verbose_name_plural = _(u'Itens da Dispensa')

    def __unicode__(self):
        return self.name

########################################################################################

class Supplier(models.Model):

    name = models.CharField(
                            max_length=50,
                            verbose_name = _(u'Nome'),
                            )

    address = models.CharField(
                            max_length=300,
                            verbose_name = _(u'Endereço'),
                            )

    phone_number = models.CharField(
                            max_length=9,
                            verbose_name = _(u'Telefone'),
                            )

    items = models.ManyToManyField(Item)

    class Meta:
        verbose_name = _(u'Fornecedor')
        verbose_name_plural = _(u'Fornecedores')

    def __unicode__(self):
        return self.name

########################################################################################

class Order(models.Model):

    invoice_number = models.IntegerField(
                                        verbose_name = _(u'Número do Pedido')
                                        )

    date = models.DateTimeField(
                            verbose_name = _(u'Data do pedido'),
                            )

    employee = models.ForeignKey(Employee, verbose_name=_(u'Funcionário'))


    class Meta:
        verbose_name = _(u'Pedido')
        verbose_name_plural = _(u'Pedidos')

    def __unicode__(self):
        return str(self.invoice_number)

########################################################################################

class MenuItem(models.Model):

    name = models.CharField(
                        max_length=50,
                        verbose_name = _(u'Nome'),
                           )

    description = models.CharField(
                        max_length=300,
                        verbose_name = _(u'Descrição'),
                           )

    price = models.DecimalField(
                            max_digits=5,
                            decimal_places=2,
                            verbose_name = _(u'Preço'),
                            )

    class Meta:
        verbose_name = _(u'Item do Cardápio')
        verbose_name_plural = _(u'Itens do Cardápio')

    def __unicode__(self):
        return self.name

########################################################################################


class OrderMenuItem(models.Model):

    order = models.ForeignKey(Order, verbose_name=_(u'Pedido'))

    menu_item = models.ForeignKey(MenuItem, verbose_name=_(u'Item do Cardápio'))

    quantity = models.DecimalField(
                            max_digits=5,
                            decimal_places=2,
                            verbose_name = _(u'Quantidade'),
                            )

    unit_price = models.DecimalField(
                            max_digits=5,
                            decimal_places=2,
                            verbose_name = _(u'Preço Unitário'),
                            )

    class Meta:
        verbose_name = _(u'Item de Pedido')
        verbose_name_plural = _(u'Itens de Pedido')

    def __unicode__(self):
        return str(self.order.invoice_number) + " | " + self.menu_item.name




########################################################################################