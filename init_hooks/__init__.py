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
    
    for method, over_method in frappe.get_hooks("override_methods_custom", {}).items():
        from_module, from_method = module_name(method)
        if len(over_method) > 1:
            from_module = getattr(from_module, from_method)
            from_method = over_method[0]
          
        _, to_method = module_name(over_method[-1], True)

        setattr(from_module, from_method, to_method)

    # for method, over_method in frappe.get_hooks("override_class_method_custom", {}).items():
    #     module_class, from_method = method.rsplit(".", 1)
    #     from_module, from_class = module_name(module_class)

    #     _, to_method = module_name(over_method[-1], True)
    #     setattr(getattr(from_module, from_class), from_method, to_method)

get_custom_method()