# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Visit(models.Model):
     _name = 'custom_crm.visit'
     _description = 'Visit'

     name = fields.Char(string='Descripción')
     customer = fields.Char(string='Cliente')
     date = fields.Datetime(string='Fecha')
     type = fields.Selection([('P', 'Presencial'), ('W', 'WhatsApp'), ('T', 'Telefónico')], string='Tipo', required=True)
     done = fields.Boolean(string='Realizada', readonly=True)