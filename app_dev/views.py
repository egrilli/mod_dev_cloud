from django.contrib import messages
from django.db import models
from django.shortcuts import redirect, render
from datetime import datetime
import bcrypt
import json
from app_dev.models import *
from app_dev.decorators import *

def index(request):

    return render(request, 'index.html')


def registro(request):
    if request.method == "POST":
        errors = User.objects.validador_basico(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)

            request.session['register_name'] =  request.POST['first_name']
            request.session['register_last_name'] =  request.POST['last_name']
            request.session['register_email'] =  request.POST['email']

        else:
            request.session['register_name'] = ""
            request.session['register_last_name'] = ""
            request.session['register_email'] = ""

            password_encryp = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode() 

            permission="USER"
            new_user = User.objects.create(
                first_name = request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=password_encryp
            )

            messages.success(request, "El usuario fue agregado con exito.")
            
        return redirect("/administrador/registro")
    else:
        return render(request, 'registro.html')


@login_required
@val_admin
def user(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'usuario.html', context)


def logearse(request):
    if request.method == "POST":
        user = User.objects.filter(email=request.POST['email'])
        if user:
            log_user = user[0]

            if bcrypt.checkpw(request.POST['password'].encode(), log_user.password.encode()):

                usuario = {
                    "id" : log_user.id,
                    "name": f"{log_user}",
                    "email": log_user.email,
                    "rol":log_user.rol
                }

                request.session['usuario'] = usuario
                messages.success(request, "Ingreso Correcto")
                return redirect("/panel")
            else:
                messages.error(request, "Password o Email no corresponden.")
        else:
            messages.error(request, "Email o password no corresponden")

        return redirect("/logearse")
    else:
        return render(request, 'index.html')

    return render(request, 'index.html')



@login_required
def panel(request):
    context = {
        'user': User.objects.get(id=request.session['usuario']['id'])
    }
    return render(request, 'panel.html', context)


def logout(request):
    if 'usuario' in request.session:
        del request.session['usuario']
        messages.error(request, "Sesion Cerrada")
    return redirect("/")


@login_required
@val_admin
def administrador(request):
    return render(request, 'administrador.html')


@login_required
@val_admin
def reporte(request):
    return render(request, 'reporte.html')



@login_required
@val_admin
def newWarehouse(request):


    if request.method == "POST":
        errors = Warehouse.objects.validador_basico(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)

            request.session['register_name'] =  request.POST['name']

        else:
            request.session['register_name'] = ""

            new_warehouse = Warehouse.objects.create(
                name=request.POST['name']
            )

            messages.success(request, "La Bodega fue agregada con exito.")
            
        return redirect("/administrador/bodega/crear")
    else:
        return render(request, 'bodega_nueva.html')


@login_required
@val_admin
def warehouse(request):
    context = {
        'warehouses': Warehouse.objects.all()
    }
    return render(request, 'bodega.html', context)


@login_required
@val_admin
def newCompany(request):


    if request.method == "POST":
        errors = Company.objects.validador_basico(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)

            request.session['register_name'] =  request.POST['name']
            request.session['register_rut'] =  request.POST['rut']
            request.session['register_warehouse'] =  request.POST['warehouse_origin']

        else:
            request.session['register_name'] =  ""
            request.session['register_rut'] =  ""
            request.session['register_warehouse'] =  ""

            new_company = Company.objects.create(
                name = request.POST['name'],
                rut = request.POST['rut'],
                warehouse_origin = request.POST['warehouse_origin']
            )

            messages.success(request, "El Cliente fue agregado con exito.")
            
        return redirect("/administrador/cliente/crear")
    else:
        return render(request, 'cliente_nuevo.html')

@login_required
@val_admin
def company(request):
    context = {
        'companies': Company.objects.all()
    }
    return render(request, 'clientes.html', context)


@login_required
@val_admin
def newPersonal(request):
    context = {
        'warehouses': Warehouse.objects.all()
    }

    if request.method == "POST":
        errors = Personal.objects.validador_basico(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)

            request.session['register_name'] =  request.POST['first_name']
            request.session['register_last_name'] =  request.POST['last_name']
            request.session['register_rut'] =  request.POST['rut']
            request.session['register_birdth'] =  request.POST['birdth_date']
            request.session['register_entry'] =  request.POST['entry_date']
            request.session['register_position'] =  request.POST['position']
            request.session['register_phone'] =  request.POST['phone']
            request.session['register_email'] =  request.POST['email']
            request.session['register_warehouse'] =  request.POST['warehouse_work']

        else:
            request.session['register_name'] = ""
            request.session['register_last_name'] = ""  
            request.session['register_rut'] =  ""
            request.session['register_birdth'] = ""  
            request.session['register_entry'] =  ""
            request.session['register_position'] = ""  
            request.session['register_phone'] =  ""
            request.session['register_email'] =  ""
            request.session['register_warehouse'] = ""  
            
            new_personal = Personal.objects.create(
                rut = request.POST['rut'],
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                birdth_date = request.POST['birdth_date'],
                entry_date = request.POST['entry_date'],
                position = request.POST['position'],
                phone = request.POST['phone'],
                email = request.POST['email'],
                warehouse_work = Warehouse.objects.get(id=request.POST['warehouse_work'])
            )

            messages.success(request, "La Persona fue agregado con exito.")
            
        return redirect("/administrador/personal/crear")
    else:
        return render(request, 'personal_nuevo.html',context)


@login_required
@val_admin
def personal(request):
    context = {
        'personals': Personal.objects.all()
    }
    return render(request, 'personal.html', context)



@login_required
@val_admin
def inversa(request):

    return render(request, 'devolucion_panel.html')


@login_required
@val_admin
def infCargo(request):

    
    order2=DeliveryOrder.objects.filter(state__dev_state = "Venta o Cobro - Cerrado")
    order1=DeliveryOrder.objects.filter(state__dev_state = "Cargo en CT Temuco")

    context = {
        'order1':order1,
        'order2':order2
    }
    return render(request, 'cargos.html',context)




@login_required
@val_admin
def newIorder(request):



    context = {
        'warehouses': Warehouse.objects.all(),
        'companies': Company.objects.all(),
        'users': User.objects.all(),
        'states': state,
        'subStates':sub_state,
        'reasons':reason,
        'conditions':condition,
        'devStates':dev_state
    }

    if request.method == "POST":
        errors = DeliveryOrder.objects.validador_basico(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)

            request.session['register_company'] =  request.POST['company_delivery']
            request.session['register_warehouse_delivery'] =  request.POST['warehouse_delivery']
            request.session['register_warehouse_origin'] =  request.POST['warehouse_origin']
            request.session['register_date_issue'] =  request.POST['date_issue']
            request.session['register_origin_order'] =  request.POST['origin_order']
            request.session['register_order_number'] =  request.POST['order_number']
            request.session['register_ticket_number'] =  request.POST['ticket_number']
            request.session['register_type_order'] =  request.POST['type_order']
            request.session['register_state'] =  request.POST['state']
            request.session['register_sub_state'] =  request.POST['sub_state']
            request.session['register_comment'] =  request.POST['comment']
            request.session['register_reason'] =  request.POST['reason']
            request.session['register_reason_extra'] =  request.POST['reason_extra']
            request.session['register_product'] =  request.POST['product']
            request.session['register_quantity'] =  request.POST['quantity']
            request.session['register_number_packager'] =  request.POST['number_packager']
            request.session['register_sku'] =  request.POST['sku']
            request.session['register_date_return'] =  request.POST['date_return']
            request.session['register_state_return '] =  request.POST['state_return']
            request.session['register_state_extra'] =  request.POST['state_extra']
            request.session['register_created_by'] =  request.POST['created_by']


        else:
            request.session['register_company'] =  ""
            request.session['register_warehouse_delivery'] =  ""
            request.session['register_warehouse_origin'] =   ""
            request.session['register_date_issue'] =   ""
            request.session['register_origin_order'] =   ""
            request.session['register_order_number'] =   ""
            request.session['register_ticket_number'] =   ""
            request.session['register_type_order'] =   ""
            request.session['register_state'] =   ""
            request.session['register_sub_state'] =   ""
            request.session['register_comment'] =   ""
            request.session['register_reason'] =   ""
            request.session['register_reason_extra'] =   ""
            request.session['register_product'] =   ""
            request.session['register_quantity'] =   ""
            request.session['register_number_packager'] =  ""
            request.session['register_sku'] =   ""
            request.session['register_date_return'] =   ""
            request.session['register_state_return '] =   ""
            request.session['register_state_extra'] =   ""
            request.session['register_created_by'] =  ""
            
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            registro = {'Estado Retorno':  request.POST['dev_state'] ,
                        'Comentario': request.POST['dev_comment'] , 
                        'Bodega Fisica': request.POST['warehouse_delivery'],
                        'Fecha Actualizacion': dt_string
                        }

            my_list=[]
            my_list.append(registro)

            new_iorder = DeliveryOrder.objects.create(
                company_delivery  = Company.objects.get(id=request.POST['company_delivery']),
                warehouse_delivery  = Warehouse.objects.get(id=request.POST['warehouse_delivery']),
                warehouse_origin= request.POST['warehouse_origin'],
                date_issue = request.POST['date_issue'],
                origin_order = request.POST['origin_order'],
                order_number = request.POST['order_number'],
                ticket_number = request.POST['ticket_number'],
                type_order = request.POST['type_order'],
                state = StateDelivery.objects.create(
                    beetrack_state = request.POST['beetrack_state'],
                    beetrack_substate = request.POST['beetrack_substate'],
                    beetrack_comment = request.POST['beetrack_comment'],
                    dev_state = request.POST['dev_state'], 
                    dev_comment = request.POST['dev_comment'],
                    dev_reason  = request.POST['dev_reason'],
                    dev_condition  = request.POST['dev_condition'],
                ),
                product = request.POST['product'],
                quantity  = request.POST['quantity'],
                number_packager = request.POST['number_packager'],
                sku = request.POST['sku'],
                created_by  = User.objects.get(id=request.POST['created_by']),
                record = my_list
            )

            
            messages.success(request, "La Guia fue ingresada con Exito")
            
        return redirect("/inversa/data/registro")
    else:
        return render(request, 'devolucion_ingreso.html',context)

@login_required
@val_admin
def dataInversa(request):
    context = {
        'orders': DeliveryOrder.objects.all()
    }

    return render(request, 'devolucion_data.html',context)

@login_required
@val_admin
def guideOrder(request,id):
    context = {
        'order': DeliveryOrder.objects.get(id=id)
    }
    return render(request, 'guia.html', context)


@login_required
@val_admin
def guideOrderEdit(request,id):


    context = {
        'order': DeliveryOrder.objects.get(id=id),
        'warehouses': Warehouse.objects.all(),
        'companies': Company.objects.all(),
        'users': User.objects.all(),
        'devStates':dev_state
    }

    if request.method == "POST":
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        registro = {'Estado Retorno':  request.POST['dev_state'] ,
                    'Comentario': request.POST['dev_comment'] , 
                    'Bodega Fisica': request.POST['warehouse_delivery'],
                    'Fecha Retorno': request.POST['date_return'],
                    'Fecha Actualizacion': dt_string
                    }
        
        order_edit = DeliveryOrder.objects.get(id=id)
        newWarehouse=Warehouse.objects.get(id=request.POST['warehouse_delivery'])
        order_edit.warehouse_delivery = newWarehouse
        edit_list =order_edit.record
        edit_list.append(registro)
        order_edit.record = edit_list
        order_edit.save()
        newState = StateDelivery.objects.get(id=order_edit.state.id)
        newState.dev_state = request.POST['dev_state']
        newState.dev_comment = request.POST['dev_comment']
        newState.date_return = request.POST['date_return']
        newState.save()


        return redirect(f'/inversa/guia/{id}')

    else:
        return  render(request, 'guia_edit.html', context)



@login_required
def warehouseOsorno(request):

    return render(request, 'bodega_osorno.html')

@login_required
def warehouseOsornoDev(request):

    context = {
        'orders': DeliveryOrder.objects.filter(warehouse_origin="Osorno"),
    }

    return render(request, 'bodega_osorno_dev.html',context)

@login_required
def guideOrderOsorno(request,id):
    context = {
        'order': DeliveryOrder.objects.get(id=id)
    }
    return render(request, 'guia_osorno.html', context)


@login_required
def warehousePuerto(request):

    return render(request, 'bodega_puerto.html')

@login_required
def warehousePuertoDev(request):

    context = {
        'orders': DeliveryOrder.objects.filter(warehouse_origin="Puerto Montt"),
    }

    return render(request, 'bodega_puerto_dev.html',context)

@login_required
def guideOrderPuerto(request,id):
    context = {
        'order': DeliveryOrder.objects.get(id=id)
    }
    return render(request, 'guia_puerto.html', context)

@login_required
def warehouseTemuco(request):

    return render(request, 'bodega_temuco.html')

@login_required
def warehouseTemucoDev(request):

    context = {
        'orders': DeliveryOrder.objects.filter(warehouse_origin="Temuco"),
    }

    return render(request, 'bodega_temuco_dev.html',context)

@login_required
def guideOrderTemuco(request,id):
    context = {
        'order': DeliveryOrder.objects.get(id=id)
    }
    return render(request, 'guia_temuco.html', context)


@login_required
def cargoTemuco(request):

    
    order2=DeliveryOrder.objects.filter(state__dev_state = "Venta o Cobro - Cerrado")
    order1=DeliveryOrder.objects.filter(state__dev_state = "Cargo en CT Temuco")

    context = {
        'order1':order1,
        'order2':order2
    }
    return render(request, 'cargos_view_temuco.html',context)

@login_required
def warehouseTemucoDataGeneral(request):

    context = {
        'orders': DeliveryOrder.objects.all()
    }
    return render(request, 'devolucion_data_general.html',context)


@login_required
def guideOrderTemucoGeneral(request,id):
    context = {
        'order': DeliveryOrder.objects.get(id=id)
    }
    return render(request, 'guia_temuco_general.html', context)


@login_required
def cargoTemucoGuia(request,id):
    context = {
        'order': DeliveryOrder.objects.get(id=id)
    }
    return render(request, 'guia_temuco_cargo.html', context)


