from __future__ import unicode_literals
from frappe import _
def get_data():
	return [
	{
	  "label": _("Customer Management"),
	  "items": [
				{
					"type": "doctype",
					"name": "Customer Setup",
					"description": _("Customer Setup"),
				},
				{
					"type": "doctype",
					"name": "User Company List",
					"description": _("User Company List")
				}
			]
	},
	{
			"label": _("Vehicle Management"),
			"items": [
				{
					"type": "doctype",
					"name": "Add New Vehicle",
					"description": _("Add new vehcile")
					
				},
				{
					"type": "report",
					"name": "Two Cost Report",
					"doctype": "Add New Vehicle"
				},
				{
					"type": "report",
					"name": "Vehicle Cost Analysis",
					"doctype": "Add New Vehicle"
				},
				{
					"type": "report",
					"name": "Vehicle Datelines",
					"doctype": "Add New Vehicle"
				}
			]
	},
	{
			"label": _("PGL Company Management"),
			"items": [
				{
					"type": "doctype",
					"name": "PGL Company Profile",
					"description": _("Add and View PGL Company details"),
					
				},
				{
					"type": "doctype",
					"name": "Load Locations",
					"description": _("Add and view load locations"),
					
				},
				{
					"type": "doctype",
					"name": "Vehicle Status",
					"description": _("Add and View Vehicle load status")
					
				},
				{
					"type": "doctype",
					"name": "Shippment Status",
					"description": _("Add and View Shippment status")
					
				}

			]
	},
	{
			"label": _("Shipment Management"),
			"items": [
				{
					"type": "doctype",
					"name": "View Shippment",
					"description": _("Add and View Towing Rates")
					
				},
				{	
					"type": "report",
					"name": "Shippment Summary",
					"doctype": "View Shippment"
				},

			]
	},
	{
			"label": _("Invoices Management"),
			"items": [
				{
					"type": "doctype",
					"name": "View Invoices",
					"description": _("Add and View Invoice"),
					
				}

			]
	},
	{
			"label": _("Rates Management"),
			"items": [
				{
					"type": "doctype",
					"name": "View Towing Rate",
					"description": _("Add and View Towing Rates"),
					
				},
				{
					"type": "doctype",
					"name": "View shipping Rates",
					"description": _("Add and view Shipping Rates")
					
				}

			]
	},
	{
			"label": _("Help Desk"),
			"items": [
				{
					"type": "doctype",
					"name": "Help Desk",
					"description": _("Add and View Help Desk"),
					
				}

			]
	},





]