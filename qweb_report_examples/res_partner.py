# -*- coding: utf-8 -*-
from openerp.osv import osv

class res_partner(osv.osv):
    _inherit = 'res.partner'

    def get_partner_sale_order_amounts(self, cr, uid, partner_id, state, context=None):
        """
        Esta funcion devuelve un diccionario con los montos sumados de las sales orders en un
        determinado estado para un un partner.
        """
        sale_order_obj = self.pool['sale.order']
        sale_order_ids = sale_order_obj.search(cr, uid, [('partner_id','=',partner_id),
            ('state','=',state)], context=context)
        sale_orders = sale_order_obj.browse(cr, uid, sale_order_ids, context=context)
        ret = {
            'amount_total': sum([x.amount_total for x in sale_orders]),
            'amount_tax': sum([x.amount_tax for x in sale_orders]),
            'amount_untaxed': sum([x.amount_untaxed for x in sale_orders]),
            'amount_undiscounted': sum([x.amount_undiscounted for x in sale_orders]),
        }
        return ret