from . import __version__ as app_version

app_name = "init_hooks"
app_title = "Init Hooks"
app_publisher = "DAS"
app_description = "Make Custom Hooks"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "das@gmail.com"
app_license = "MIT"

after_sync = "init_hooks.sync.sync_override_method"
after_migrate = "init_hooks.sync.sync_override_method"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/init_hooks/css/init_hooks.css"
# app_include_js = "/assets/init_hooks/js/init_hooks.js"

# include js, css files in header of web template
# web_include_css = "/assets/init_hooks/css/init_hooks.css"
# web_include_js = "/assets/init_hooks/js/init_hooks.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "init_hooks/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "init_hooks.install.before_install"
# after_install = "init_hooks.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "init_hooks.uninstall.before_uninstall"
# after_uninstall = "init_hooks.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "init_hooks.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"init_hooks.tasks.all"
#	],
#	"daily": [
#		"init_hooks.tasks.daily"
#	],
#	"hourly": [
#		"init_hooks.tasks.hourly"
#	],
#	"weekly": [
#		"init_hooks.tasks.weekly"
#	]
#	"monthly": [
#		"init_hooks.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "init_hooks.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "init_hooks.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "init_hooks.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Request Events
# ----------------
# before_request = ["init_hooks.utils.before_request"]
# after_request = ["init_hooks.utils.after_request"]

# Job Events
# ----------
# before_job = ["init_hooks.utils.before_job"]
# after_job = ["init_hooks.utils.after_job"]

# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"init_hooks.auth.validate"
# ]

