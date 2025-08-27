"""
def Revise(csp, X, Y):
  revised = False
  for x in X.domain:
    if no y in Y.domain satisfies constraint for (X, Y):
      delete x from X.domain
      revised = True
  return revised
  
"""
""" csp - constraints satisfaction problem
Arc Consistence fn
function AC-3(csp):
  queue = all arcs in csp
  while queue non-empty:
    (X,Y) = DEQUEUE(queue)
    if REVISED(csp, X,Y):
      if size of X.domain == 0:
        return false
"""

#BackTracking Search
"""  
function BackTrack(assigment, csp):
  if assignment comlete: 
    return assignment
  
  var = SELECT-UNASSIGNED-VAR(assignment, csp)
  for value in DOMAIN-VALUES(var, assignment, csp):
    if value consistent with assignment:
      add {var = value} to assignment
      result = BACKTRACK(assignment, csp)
      if result != failure: 
        return result
      
    remove {var = value} from assignment
  return failure
    
"""
### SELECT-UNASSIGNED-VAR(int)
### minimum remaining values ( MRV ) heuristic: select the variable that has the smallest domain
### degree heuristic : select the value that has the highest degree


# Proposed Model development for the Optimiation class => exam timetable for university with limited examrooms and common units especially for first years