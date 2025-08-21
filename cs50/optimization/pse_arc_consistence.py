"""
def Revise(csp, X, Y):
  revised = False
  for x in X.domain:
    if no y in Y.domain satisfies constraint for (X, Y):
      delete x from X.domain
      revised = True
  return revised
  
"""
"""
Arc Consistence fn
function AC-3(csp):
  queue = all arcs in csp
  while queue non-empty
"""