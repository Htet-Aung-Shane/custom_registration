from odoo import models, fields, api, _

class SMSConfiguration(models.Model):
    """
    Model for SMS configuration settings.
    """
    _name = "smspoh.configuration"
    _description = "SMS Configuration"

    name = fields.Char(string="Sender Name", required=True, help="Name of the SMS sender")
    url = fields.Char(string="API URL", index=True, required=True, help="URL for the SMS API")
    api_key = fields.Char(string="API Key", index=True, required=True, help="API key for accessing the SMS API")
    active = fields.Boolean(string="Active", default=True, help="Whether this configuration is active or not")
    priority = fields.Integer(string="Priority", help="Priority of the SMS configuration")

