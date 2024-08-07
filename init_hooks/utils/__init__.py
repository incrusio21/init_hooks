# Copyright (c) 2024, DAS and contributors
# For license information, please see license.txt

import os

import frappe
from frappe import _

from frappe.modules.utils import get_module_path, scrub
from frappe.utils.data import cint

@frappe.whitelist()
def export_method(docname, module, sync_on_migrate=0):
    """Export Custom Method for override method to the app folder.
	This will be synced with bench migrate"""

    sync_on_migrate = cint(sync_on_migrate)
    
    if not frappe.get_conf().developer_mode:
        raise Exception("Not developer mode")
    
    custom = {
		"sync_on_migrate": sync_on_migrate,
	}
    
    folder_path = os.path.join(get_module_path(module), "override_methods")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    custom["doctype"] = frappe.get_doc("Override Methods", docname).as_dict()

    path = os.path.join(folder_path, scrub(docname) + ".json")
    with open(path, "w") as f:
        f.write(frappe.as_json(custom))

    frappe.msgprint(_("Override Method for <b>{0}</b> exported to:<br>{1}").format(docname, path))