def master_list():
    pt1 = {"name": "mary", "meds": ["ramipril", "asprin"]}
    pt2 = {"name": "ned", "meds": ["asprin", "plavix", "symbicort"]}
    pt3 = {"name": "jack", "meds": ["diabex", "novorapid", "statin"]}
    role_call = [pt1, pt2, pt3]
    return role_call

def print_maste_list(pt_list):
    for pt in pt_list:
        print(pt)

def print_pt_meds(pt_list, name):
    for pt in pt_list:
        if pt["name"] == name:
            print(pt.get("meds"))
            print("med list printed successfully")
        print("")

def add_pt(pt_list, add_name, add_meds):
    new_pt = {"name": add_name, "meds": add_meds}
    pt_list.append(new_pt)

def remove_pt(pt_list, del_name):
    for lu_pt in pt_list:
        if lu_pt["name"] == del_name:
            pt_list.remove(lu_pt)
            print(f"{del_name} was removed from the patient list")
        print("")   

def add_med(pt_list, name):
    for pt in pt_list:
        if pt["name"] == name:
            new_med = input("What would you like to add: ")
            pt["meds"].append(new_med)
            print(f"{new_med} was addeded")
        print("")   

def remove_med(pt_list, lu_pt):
    for pt in pt_list:
        if pt ["name"] == lu_pt:
            del_med = input("enter position of med you would like to remove: ")
            del pt["meds"][int(del_med)-1]
            print("deletion successful")
        print("")
