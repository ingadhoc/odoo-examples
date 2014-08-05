# -*- coding: utf-8 -*-
{
    'name': "Qweb Report Examples",

    'summary': """
        Simple module to test some functionalities and make some examples related to the
        QWeb reporting facilities of Odoo V8""",

    'description': """
Qweb Report Examples
====================
Simple module to test some functionalities and make some examples related to the QWeb reporting facilities of Odoo V8

Tener en cuenta:
----------------
* Leer bootstrap: http://getbootstrap.com/css/
* Ver qweb en https://doc.openerp.com/trunk/web/qweb especialmente las directivas de q-web en https://doc.openerp.com/trunk/web/qweb/#defining-templates
* Probar css http://jsfiddle.net/h8SBh/1/
* Para reportes y css!!! http://ksesocss.blogspot.com/2012/05/estilos-css-para-imprimir-la-regla-page.html 
* Los reportes constan basicamente de:
    * Un registro en la clase de reportes (ir.actions.report.xml) que se puede crear con el atajo "<report". Se suelen crear todos los reportes de un modulo en el archivo "[nombre_de_modulo]_report.xml"
    * Cada reporte qweb tiene además vistas definidas, dichas vistas se suelen guardar en la carpeta views. Se crea un archivo para cada reporte
    * Si se requieren funcionalidades avanzadas, se pueden crear archivos .py que modifican el funcionamiento por defecto de los reportes, eso suele ir en la carpeta "reports" (solo archivos .py). En dicha carpeta se suelen almacenar también los cubos (su corresndiente .py y .xml)
    * Si se requiere de un wizard, tanto el .py como el .xml irían en la carpeta "wizard"
* Respecto a las vistas de reportes
    * Se pueden heradar como cualquier vista. Es recomendable probarlo desde la interfaz de odoo ya que al querer guardar el registor nos va a validar si la vista es correcta o no. Luego lo llevamos al modulo.
* Respecto a los reportes:
    * Resulta muy practico empezarlos con tipo html, al pedir una vez el reporte se abre una nueva ventana, pero podemos copiar la url y llevarla a nuestro explorador. Luego simplemente refrezcando podemos tener actualizaciones del reporte.
    """,

    'author': "Ingenieria ADHOC",
    'website': "http://www.ingadhoc.com",

    # Categories can be used to filter modules in modules listing
    # Check <odoo>/addons/base/module/module_data.xml of the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # Agregamos estas dependencias para el ejemplo, website lo ponemos para que sea editable en interfaz web
    'depends': ['base','website','sale','account'],
    'data': [
        # cargamos las vistas de los reportes        
        'views/report_ejemplo1.xml', # reporte sensillo que es recorrido aparte y traducido
        'views/report_ejemplo2.xml', # reporte sensillo recorrido en el mismo
        'views/report_ejemplo3.xml', # reporte que define su propio header
        'views/report_ejemplo4.xml', # reporte que tiene su propio parser (.py)
        'views/report_ejemplo5.xml', # reporte que utiliza una funcion agregada a partenr 
        'views/report_ejemplo6.xml', # reporte que muestra un monton de ejemplos, hay que seguir agregando acá
                
        # Mostramos herencia de reportes, modificamos el header y footer por defecto
        'views/report_external_layout_header.xml',
        'views/report_external_layout_footer.xml',

        # cargamos los reportes
        'nombre_de_modulo_report.xml',
    ],

    'demo': [
    ],

    'tests': [
    ],
}
