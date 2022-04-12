import frappe
import frappe.permissions 
from frappe import _
from frappe.sessions import delete_session


def login_feed(login_manager):
    ip = frappe.local.request_ip
    user = frappe.get_doc('User', login_manager.user)
    branch = {
        "180.195.203.152" : "Garcia's Pawnshop Cavite City Branch",
        "180.191.232.68" : "Garcia's Pawnshop GTC Branch",
        "49.144.100.169" : "Garcia's Pawnshop Molino Branch",
        "49.144.9.203" : "Garcia's Pawnshop Poblacion Branch",
        "136.158.82.68" : "Garcia's Pawnshop Tanza Branch"
    }
    if user.role_profile_name == "Cashier" or user.role_profile_name == "Appraiser" or user.role_profile_name == "Vault Custodian" or user.role_profile_name == "Supervisor/Cashier" or user.role_profile_name == "Appraiser/Cashier" or user.role_profile_name == "Supervisor":
        # if ip != "127.0.0.1":
        if ip == "180.195.203.152" or ip == "180.191.232.68" or ip == "49.144.100.169" or ip == "49.144.9.203" or ip == "136.158.82.68":
            frappe.msgprint(
                msg = 'Welcome, ' + user.full_name,
                title = 'Welcome to ' + branch[ip]
            )
        # user = frappe.get_doc('user', login_manager.user)
        # print(user.role_profile_name)
            # frappe.throw(
            #     title='Error',
            #     msg='test',
            #     exc= RuntimeError
            # )
        else:
            frappe.throw(
                title = 'Log In Restricted',
                msg = 'You are not authorized to login in this station',
                exc = RuntimeError
            )
            return 0

def post_login(login_manager):
    if login_feed(login_manager) == 0:
        delete_session()
