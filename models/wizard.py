# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'academy.wizard'
    _description = 'wizard: Dang ky thanh vien'

    def _default_sessions(self):
        return self.env['academy.session'].browse(self._context.get('active_id'))
    session_ids = fields.Many2one('academy.session', string="Sessions", required=True, default=_default_sessions)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    @api.multi
    def subscribe(self):
        for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids
        return {}


