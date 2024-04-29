from odoo import models, fields, api, _

class SMSLogs(models.Model):
    """
    Model for saving SMS logs.
    """
    _name = "sms.log"
    _description = "SMS Log"

    phone = fields.Char(string="Phone Number",help="Recipient's phone number")
    message = fields.Text(string="Message Content", help="Content of the SMS message")
    sender_id = fields.Many2one("smspoh.configuration", string="Sender", help="Configuration for sending SMS messages")
    status = fields.Selection([('fail','Fail'),('pass','Pass' )],string="Status")
    type = fields.Selection([('sms','SMS'),('otp','otp' )],string="SMS")
    admin_id = fields.Many2one("res.partner", string="Created By", help="The person who created this record")

    @api.model
    def create(self, vals):
        vals["admin_id"] = self.env.user.partner_id.id    
        return super(SMSLogs, self).create(vals)