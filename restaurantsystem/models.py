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
                            max_length=11,
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
        verbose_name = _(u'Item')
        verbose_name_plural = _(u'Itens')

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
                            max_length=11,
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

class Product(models.Model):

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
        verbose_name = _(u'Produto')
        verbose_name_plural = _(u'Produtos')

    def __unicode__(self):
        return self.name

########################################################################################


class OrderProduct(models.Model):

    order = models.ForeignKey(Order, verbose_name=_(u'Pedido'))

    product = models.ForeignKey(Product, verbose_name=_(u'Produto'))

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
        verbose_name = _(u'Pedido (Produtos)')
        verbose_name_plural = _(u'Pedidos (Produtos)')

    def __unicode__(self):
        return str(self.order.invoice_number) + " | " + self.product.name




########################################################################################

class Purchase(models.Model):

    invoice_number = models.IntegerField(
                                        verbose_name = _(u'Número da Compra')
                                        )

    date = models.DateTimeField(
                            verbose_name = _(u'Data da compra'),
                            )

    employee = models.ForeignKey(Employee, verbose_name=_(u'Funcionário'))

    class Meta:
        verbose_name = _(u'Compra')
        verbose_name_plural = _(u'Compras')

    def __unicode__(self):
        return str(self.invoice_number)

########################################################################################

class PurchaseItem(models.Model):

    purchase = models.ForeignKey(Purchase, verbose_name=_(u'Compra'))

    item = models.ForeignKey(Item, verbose_name=_(u'Item'))

    supplier = models.ForeignKey(Supplier, verbose_name=_(u'Fornecedor'))

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
        verbose_name = _(u'Compras (Item)')
        verbose_name_plural = _(u'Compras (Itens)')

    def save(self, *args, **kwargs):
        super(PurchaseItem, self).save(*args, **kwargs)
        item = Item.objects.get(id=self.item.id)
        item.quantity += self.quantity
        item.save()

    def __unicode__(self):
        return str(self.purchase.invoice_number) + " | " + self.item.name