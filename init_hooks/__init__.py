# Copyright (c) 2024, DAS and contributors
# For license information, please see license.txt

import frappe

__version__ = '0.0.1'

def module_name(method_str, is_getattr=False):
    module_path, method_name = method_str.rsplit(".", 1)
    module = frappe.get_module(module_path)
    if not hasattr(module, method_name):
        raise ImportError(
            "method {0} does not exist in module {1}".format(method_name, module_path)
        )
    
    return ["", getattr(module, method_name)] if is_getattr else [module, method_name]

def get_custom_method():
    if not hasattr(frappe.local, "conf") or not frappe.db:
        return
    
    # pastikan table telah terbentuk
    if not frappe.db.exists("DocType", "Override Methods"):
        return
    
    override = frappe.db.sql("""
        SELECT om.name, omd.original_method, omd.overwrite_method
        FROM `tabOverride Methods` om, `tabOverride Methods Details` omd
        WHERE om.name = omd.parent and om.disabled != 1
        ORDER BY priority, om.modified, omd.idx
    """, as_dict=1)

    for row in override:
        original_module, original_method_name = frappe.get_module(row.name), row.original_method
        if '.' in original_method_name:
            class_name, class_method = original_method_name.rsplit(".", 1)
            if not hasattr(original_module, class_name):
                raise ImportError(
                    "Class {0} does not exist in module {1}".format(class_name, original_method_name)
                )
            
            original_module = getattr(original_module, class_name)
            original_method_name = class_method

        if not hasattr(original_module, original_method_name):
            raise ImportError(
                "method {0} does not exist in module {1}".format(original_method_name, row.name)
            )
        
        override_path, override_name = row.overwrite_method.rsplit(".", 1)

        override_module = frappe.get_module(override_path)
        if not hasattr(override_module, override_name):
            raise ImportError(
                "method {0} does not exist in module {1}".format(override_name, override_module)
            )
        
        setattr(original_module, original_method_name, getattr(override_module, override_name))

get_custom_method()
