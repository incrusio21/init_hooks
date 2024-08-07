# Copyright (c) 2024, DAS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class OverrideMethods(Document):
	
	def validate(self):
		self.warning_to_restart()

	def warning_to_restart(self):
		frappe.msgprint("""
			Please restart the web server first to ensure that the function override works properly. 
			<br> If you don't have access to the server, please call the admin."""
		)
