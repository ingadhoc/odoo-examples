# -*- coding: utf-8 -*-
from openerp.osv import osv
# from openerp.tools.translate import _

class InvoiceReport(osv.AbstractModel):
    _name = 'report.l10n_ar_report_invoice.report_invoice_view'

    def render_html(self, cr, uid, ids, data=None, context=None):
        report_obj = self.pool['report']
        invoice_obj = self.pool['account.invoice']
        report = report_obj._get_report_from_name(cr, uid, 'l10n_ar_report_invoice.report_invoice_view')
        
        # We add report
        docargs = {
            'doc_ids': ids,
            'doc_model': report.model,
            'docs': invoice_obj.browse(cr, uid, ids, context=context),
            'report': report,
        }

        # We add all the key-value pairs of the report configuration
        for report_conf_line in report.line_ids:
            if report_conf_line.value_type == 'text':
                docargs.update({report_conf_line.name: report_conf_line.value_text})
            elif report_conf_line.value_type == 'boolean':
                docargs.update({report_conf_line.name: report_conf_line.value_boolean})        

        return report_obj.render(cr, uid, ids, 'l10n_ar_report_invoice.report_invoice_view', docargs, context=context)