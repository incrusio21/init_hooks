import frappe

__version__ = '0.0.1'

def get_custom_method():
    def module_name(method_str, is_getattr=False):
        module_path, method_name = method_str.rsplit(".", 1)
        module = frappe.get_module(module_path)
        if not hasattr(module, method_name):
            raise ImportError(
                "method {0} does not exist in module {1}".format(method_name, module_path)
            )
        
        return ["", getattr(module, method_name)] if is_getattr else [module, method_name]
    
    for method, over_method in frappe.get_hooks("override_methods_custom", {}).items():
        from_module, from_method = module_name(method)
        _, to_method = module_name(over_method[-1], True)
        setattr(from_module, from_method, to_method)

get_custom_method()