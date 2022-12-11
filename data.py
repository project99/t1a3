def pt_list ():
  pt1 = {"name": "mary", "meds": ["ramipril", "asprin"]}
  pt2 = {"name": "ned", "meds": ["asprin", "plavix", "symbicort"]}
  pt3 = {"name": "jack", "meds": ["diabex", "novorapid", "statin"]}
  
  pt1["meds"].extend(["statin", "movicol"])
  pt_summary = [pt1, pt2, pt3]

def add_pt():
  name = input("Name of new pt: ")
  meds = input("Meds of new pt: ").split()

  def add_fx(pt_add, name, meds):
    new_pt={"name":name, "meds":meds}
    pt_add.extend(new_pt)

  add_fx(pt_summary, name, meds)



  pt_summary = [pt1, pt2, pt3]
  print (pt_summary)

pt_list ()