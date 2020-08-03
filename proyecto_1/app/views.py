from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import ProductoForm, ClienteForm, FacturaForm, DetalleFacturaForm


def menu(request):
    opciones = {'Menu': 'Menu Principal',
                'Producto': 'Producto', 'Cliente': 'Cliente', 'Factura': 'Factura', 'DetalleFactura': 'DetalleFactura'}
    return render(request, 'principal.html', opciones)


def producto(request):
    opciones = {'Menu': 'Menu Principal',
                'Producto': 'Producto', 'Cliente': 'Cliente', 'Factura': 'Factura', 'DetalleFactura': 'DetalleFactura'}
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = ProductoForm()
        opciones['form'] = form
    return render(request, 'producto.html', opciones)


def cliente(request):
    opciones = {'Menu': 'Menu Principal',
                'Producto': 'Producto', 'Cliente': 'Cliente', 'Factura': 'Factura', 'DetalleFactura': 'DetalleFactura'}
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = ClienteForm()
        opciones['form'] = form
    return render(request, 'cliente.html', opciones)


def factura(request):
    opciones = {'Menu': 'Menu Principal',
                'Producto': 'Producto', 'Cliente': 'Cliente', 'Factura': 'Factura', 'DetalleFactura': 'DetalleFactura'}
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = FacturaForm()
        opciones['form'] = form
    return render(request, 'factura.html', opciones)


def detallefactura(request):
    opciones = {'Menu': 'Menu Principal',
                'Producto': 'Producto', 'Cliente': 'Cliente', 'Factura': 'Factura', 'DetalleFactura': 'DetalleFactura'}
    if request.method == 'POST':
        form = DetalleFacturaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = DetalleFacturaForm()
        opciones['form'] = form
    return render(request, 'detallefactura.html', opciones)
