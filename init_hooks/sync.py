# Copyright (c) 2024, DAS and contributors
# For license information, please see license.txt

import os
import json

import frappe
from init_hooks import get_custom_method
def sync_override_method():

    apps = frappe.get_installed_apps()

    for app_name in apps:
        for module_name in frappe.local.app_modules.get(app_name) or []:
            folder = frappe.get_app_path(app_name, module_name, "override_methods")
            if os.path.exists(folder):
                for fname in os.listdir(folder):
                    if fname.endswith(".json"):
                        with open(os.path.join(folder, fname), "r") as f:
                            data = json.loads(f.read())

                        if data:
                            sync_override_for_doctype(data)

    frappe.db.commit()
    get_custom_method()

    print("Please restart the web server first to ensure that the function override works properly.")

def sync_override_for_doctype(data):
    """Sync override method for a particular data set"""

    doc = data["doctype"]

    if frappe.db.exists("Override Methods", doc["name"]):
        custom_script = frappe.get_doc("Override Methods", doc["name"])
        custom_script.update(doc)
        custom_script.save()
    else:
        custom_script = frappe.new_doc("Override Methods")
    
    custom_script.update(doc)
    custom_script.save()

    print("Updating override method for {0}".format(doc["name"]))