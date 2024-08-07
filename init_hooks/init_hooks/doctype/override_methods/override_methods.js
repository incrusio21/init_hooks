// Copyright (c) 2024, DAS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Override Methods', {
	refresh: function(frm) {
		if (!cur_frm.doc.__islocal && frappe.boot.developer_mode) {
			frm.add_custom_button(__('Export Methods'), () => {
				frappe.prompt(
					[
						{
							fieldtype: "Link",
							fieldname: "module",
							options: "Module Def",
							label: __("Module to Export"),
							reqd: 1,
						},
						{
							fieldtype: "Check",
							fieldname: "sync_on_migrate",
							label: __("Sync on Migrate"),
							default: 1
						}
					],
					function(data) {
						frappe.call({
							method: "init_hooks.utils.export_method",
							args: {
								docname: frm.doc.name,
								module: data.module,
								sync_on_migrate: data.sync_on_migrate
							}
						});
					},
					__("Select Module")
				);
			});
		}
	}
});
