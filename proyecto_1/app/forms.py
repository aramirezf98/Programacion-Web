from django import forms
from .models import Producto
from .models import Cliente
from .models import Factura
from .models import DetalleFactura

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('descripcion','precio','stock','iva')
        label = {'descripcion':'Producto','precio':'Precio','stock':'Stock','iva':'Iva'}

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fiels = ('ruc','nombre','direccion','producto')
        label = {'ruc':'Ruc','nombre':'Nombre','direccion':'Direccion','producto':'Producto'}

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fiels = ('cliente','fecha','total')
        label = {'cliente':'Cliente','fecha':'Fecha','total':'Total'}

class DetalleFacturaForm(forms.ModelForm):
    class Meta:
        model = DetalleFactura
        fiels = ('factura','producto','cantidad','precio','subtotal')
        label = {'factura':'Factura','prodcuto':'Producto','cantidad':'Cantidad','precio':'Precio','subtotal':'Subtotal'}