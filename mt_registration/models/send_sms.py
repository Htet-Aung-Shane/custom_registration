from odoo import models, fields, api, _
import requests


class SendSMS(models.Model):
    """
    Model for sending SMS messages.
    """

    _name = "send.sms"
    _description = "Send SMS"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    phone = fields.Char(
        string="Phone Number", required=True, help="Recipient's phone number"
    )
    message = fields.Text(
        string="Message Content", required=True, help="Content of the SMS message"
    )
    sender_id = fields.Many2one(
        "smspoh.configuration",
        string="Sender",
        required=True,
        help="Configuration for sending SMS messages",
    )
    is_send = fields.Boolean(
        string="Active", default=False, help="Whether SMS is sent or not"
    )

    def action_send(self):
        self.is_send = True
        sender_name = self.sender_id.name
        url = self.sender_id.url
        key = self.sender_id.api_key
        headers = {
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        }
        data = {
            "to": self.phone,
            "message": self.message,
            "sender": sender_name,
        }

        print("data>>>", data)
        print("url>>>", url)
        print("headers>>>", headers)
        log_vals = {
            "phone": self.phone,
            "message": self.message,
            "sender_id": self.sender_id.id,
            "status": "fail",  # Default status is set to "fail"
            "type": "sms",
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                log_vals["status"] = (
                    "pass"  # Update status to "pass" if request is successful
                )
        except Exception as e:
            print(f"Error occurred while sending SMS: {str(e)}")

        self.env["sms.log"].create(log_vals)
