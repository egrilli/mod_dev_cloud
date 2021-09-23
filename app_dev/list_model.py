company = [
    ('1','Abcdin'),
    ('2','Hites'),
    ('3','La Polar')
]

state = [
    ('Entregado','Entregado'),
    ('Pendiente','Pendiente'),
    ('No Entregado','No Entregado'),
    ('Entrega Parcial','No Retirado'),
    ('Retirado','Retirado')
]


return_type = [
    ('Retiro','Retiro'),
    ('Anulacion','Anulacion'),
    ('Rechazo','Rechazo'),
    ('Re-ingreso a CD','Re-ingreso a CD')

]


sub_state = [
    ('Conforme','Conforme'),
    ('Domicilio sin moradores','Domicilio sin moradores'),
    ('Domicilio no corresponde','Domicilio no corresponde'),
    ('Cliente Anula Compra','Cliente Anula Compra'),
    ('Producto No Corresponde','Producto No Corresponde'),
    ('Producto Danado','Producto Danado'),
    ('Camion Siniestrado','Camion Siniestrado'),
    ('Camion en Panne','Camion en Panne'),
    ('Despacho Duplicado','Despacho Duplicado'),
    ('Retiro no realizado','Retiro no realizado'),
    ('Retiro y Cambio no realizado','Retiro y Cambio no realizado'),
    ('Fuera de Horario','Fuera de Horario'),
    ('Producto Incompleto','Producto Incompleto'),
    ('Reagendamiento por Cliente','Reagendamiento por Cliente'),
    ('Acceso Inaccsesible','Acceso Inaccsesible'),
    ('Devolucion a CD','Devolucion a CD'),
    ('Devolucion','Devolucion')
]


reason = [
    ('Anula Compra','Anula Compra'),
    ('Rechazo Px no Corresponde','Rechazo Px no Corresponde'),
    ('Rechazo Px danado','Rechazo Px danado'),
    ('Decision Comercial','Decision Comercial'),
    ('Desiste Compra','Desiste Compra'),
    ('No Aplica','No Aplica')
    
]


condition = [
    ('Embalaje Completo Px Noble','Embalaje Completo Px Noble'),
    ('Emalaje Incompleto Px Noble','Emalaje Incompleto Px Noble'),
    ('Sin Embalaje Px Noble','Sin Embalaje Px Noble'),
    ('Estado Px a todo evento','Estado Px a todo evento'),
    ('No Aplica','No Aplica')
]

dev_state = [
    ('Pendiente de Ruta (Estado base inicial)','Pendiente de Ruta (Estado base inicial)'),
    ('Sologo Guia - Cliente Desiste de Retiro','Sologo Guia - Cliente Desiste de Retiro'),
    ('Solo Guia - Rechazo no cumple condicion','Solo Guia - Rechazo no cumple condicion'),
    ('En Bodega CT Temuco','En Bodega CT Temuco'),
    ('En Bodega CT Osorno','En Bodega CT Osorno'),
    ('En Bodega CT Puerto Montt','En Bodega CT Puerto Montt'),
    ('En Reparacion','En Reparacion'),
    ('Enviado a CD','Enviado a CD'),
    ('Aceptado CD - Cerrado','Aceptado CD - Cerrado'),
    ('Rechazado CD','Rechazado CD'),
    ('Cargo en CT Temuco','Cargo en CT Temuco'),
    ('Venta o Cobro - Cerrado','Venta o Cobro - Cerrado')   
]
