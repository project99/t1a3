def pt_list ():
  pt1 = {"name": "mary", "meds": ["ramipril", "asprin"]}
  pt2 = {"name": "ned", "meds": ["asprin", "plavix", "symbicort"]}
  pt3 = {"name": "jack", "meds": ["diabex", "novorapid", "statin"]}
  pt1["meds"].extend(["statin"])
  print (pt1)

pt_list ()