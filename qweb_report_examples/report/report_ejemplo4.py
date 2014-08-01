# -*- coding: utf-8 -*-
from openerp.osv import osv

report_name = 'qweb_report_examples.report_ejemplo4'
class InvoiceReport(osv.AbstractModel):
    """ Para modificar el parser por defecto debemos copiar este archivo y 
    * Poner en _name: "report.[nombre_de_reporte]"
    * esto lo facilitamos completando "report_name"
    
    Para entender porque funciona esto, se puede ver el archivo "report/models/report.py"
    en la funcion "get_html". Si se quisiese extender funcionalidad para todos los reportes, 
    deberíamos modificar dicho procedimiento (eso lo hicimos en el modulo "report_extended")
    
    En este ejemplo le pasamos al reporte en cuestion, dentro de la variable "report" al 
    propio reporte para poder utilizarlo en el reporte.
    """
    # global report_name
    # _name = 'report.' + 'qweb_report_examples.report_ejemplo4'
    _name = 'report.' + report_name

    def render_html(self, cr, uid, ids, data=None, context=None):
        """Esta es la funcion principal que se encarga de modificar lo que va a 
        recibir el reporte"""

        report_obj = self.pool['report']
        invoice_obj = self.pool['account.invoice']
        # Agregamos el reporte actual
        report = report_obj._get_report_from_name(cr, uid, report_name)
        docargs = {
            'doc_ids': ids,
            'doc_model': report.model,
            'docs': invoice_obj.browse(cr, uid, ids, context=context),
            'report': report,
            # Le cambiamos el nombre al proposito, para notar que una cosa es la funcion
            # que uso y otra lo que le paso al reporte
            # Esta funcion la comentamos porque no se como hacer para que cr y uid no haga falta que los pase
            # imagino que se hace como esta en el reporte_ejemplo6
            # 'get_sale_order_amounts': self.get_partner_sale_order_amounts,
        }

        return report_obj.render(cr, uid, ids, report_name, docargs, context=context)

    # def get_partner_sale_order_amounts(self, cr, uid, partner_id, state, context=None):
    #     """Funcion que creamos para ser usada solo en este reporte. 
    #     Si nos hubiese interesado que sirva para otros casos la podriamos haber creado en 
    #     la clase res.partner (heredando res.partner y listo), ver ejemplo en report_example5.

    #     Esta funcion devuelve un diccionario con los montos sumados de las sales orders en un
    #     determinado estado para un un partner.
    #     """
    #     print 'context',context
    #     print 'self',self
    #     cr = self.cr
    #     uid = self.uid
    #     sale_order_obj = self.pool['sale.order']
    #     sale_order_ids = sale_order_obj.search(cr, uid, [('partner_id','=',partner_id),
    #         ('state','=',state)], context=context)
    #     sale_orders = sale_order_obj.browse(cr, uid, sale_order_ids, context=context)
    #     ret = {
    #         'amount_total': sum([x.amount_total for x in sale_orders]),
    #         'amount_tax': sum([x.amount_tax for x in sale_orders]),
    #         'amount_untaxed': sum([x.amount_untaxed for x in sale_orders]),
    #         'amount_undiscounted': sum([x.amount_undiscounted for x in sale_orders]),
    #     }
    #     return ret