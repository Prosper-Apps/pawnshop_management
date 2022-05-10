import frappe
from frappe.utils import today


@frappe.whitelist()
def update_pawn_tickets():
    non_jewelry = frappe.db.get_all('Pawn Ticket Non Jewelry', 
        filters={
            'workflow_state': 'Active'
        },
        pluck='name')
    for i in range(len(non_jewelry)):
        pawn_ticket=frappe.get_doc('Pawn Ticket Non Jewelry', non_jewelry[i])
        print(type(pawn_ticket.expiry_date))
        # if pawn_ticket.expiry_date) < str(today()):
        #     print("True")

@frappe.whitelist()
def get_child_table():
    items = frappe.get_doc('Pawn Ticket Non Jewelry', '6B')
    return items

@frappe.whitelist()
def status_change_date(pawn_ticket_no):
    frappe.db.set_value('Pawn Ticket Non Jewelry', pawn_ticket_no, 'change_status_date', today())
    frappe.db.commit()

@frappe.whitelist()
def increment_b_series(branch):
    if branch == "Rabie's House":
        doc = frappe.get_doc("Non Jewelry Naming Series", "Rabie's House")
        doc.b_series += 1
        doc.save(ignore_permissions=True)
    elif branch == "Garcia's Pawnshop - CC":
        doc = frappe.get_doc("Non Jewelry Naming Series", "Garcia's Pawnshop - CC")
        doc.b_series += 1
        doc.save(ignore_permissions=True)
    elif branch == "Garcia's Pawnshop - MOL":
        doc = frappe.get_doc("Non Jewelry Naming Series", "Garcia's Pawnshop - MOL")
        doc.b_series += 1
        doc.save(ignore_permissions=True)
    elif branch == "Garcia's Pawnshop - POB":
        doc = frappe.get_doc("Non Jewelry Naming Series", "Garcia's Pawnshop - POB")
        doc.b_series += 1
        doc.save(ignore_permissions=True)
    elif branch == "Garcia's Pawnshop - GTC":
        doc = frappe.get_doc("Non Jewelry Naming Series", "Garcia's Pawnshop - GTC")
        doc.b_series += 1
        doc.save(ignore_permissions=True)
    elif branch == "Garcia's Pawnshop - TNZ":
        doc = frappe.get_doc("Non Jewelry Naming Series", "Garcia's Pawnshop - TNZ")
        doc.b_series += 1
        doc.save(ignore_permissions=True)