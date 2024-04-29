{
    "name": "Register Customization",
    "author": "MT Tech",
    "website": "https://www.mttech-mm.com",
    "support": "MT Tech",
    "category": "Customizations",
    "license": "OPL-1",
    "summary": "Customization(Register Form)",
    "description": """Register Form Customization""",
    "depends": [
        'base',
        'website',        
    ],
    "application": True,
    "data": [
        'security/ir.model.access.csv',
        'views/configuration.xml',
        'views/send_sms.xml',
        'views/log.xml',
        'views/menu.xml'
    ],
    "auto_install": False,
    "installable": True,
    "images": [],
    # 'assets' : {
    #     'web.assets_frontend' : [
    #         'account_customization/static/src/js/*',
    #         'account_customization/static/src/template/*'

    #     ]
    # }
}
