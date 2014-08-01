# -*- coding: utf-8 -*-
import time
from openerp.osv import osv
from openerp.report import report_sxw

report_name = "qweb_report_examples.report_ejemplo6"

class report_parser(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context=None):
        super(report_parser, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            # le cambiamos el nombre solo para mostrar que puede tener
            # distinto nombre con la que veo en el reporte
            'sale_orders' : self.search_partner_sale_orders,
        })

    def search_partner_sale_orders(self, partner_id, context=None):
        """ Funcion que busca las sales order de un partenr
        No se porque pero este self tiene el .cr y el .uid, tendra que ser cosa
        de la clase report_sxw.rml_parse
        """
        sale_order_obj = self.pool['sale.order']
        sale_order_ids = sale_order_obj.search(self.cr, self.uid, [('partner_id','=',partner_id)], context=context)
        return sale_order_obj.browse(self.cr, self.uid, sale_order_ids, context=context)

class example_report_view(osv.AbstractModel):
    _name = 'report.' + report_name
    _inherit = 'report.abstract_report'
    _template = report_name
    _wrapped_report_class = report_parser

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
