class patient:
  def __init__(self, name, meds):
    self.pt_name = name
    self.pt_meds = meds 

pt1 = patient("name":"mary", "meds": ["diabex", "statin", "novarapid"])

print (pt1)