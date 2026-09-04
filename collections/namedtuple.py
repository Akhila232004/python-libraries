# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : namedtuple()
#  Author       : Team Tinitiate
# ==============================================================================



from collections import namedtuple

employee = namedtuple('employee', 'name, dept, sal')

e1 = employee('AAA', 'Sales', '1000')
print(e1.name)
print(e1.dept)
print(e1.sal)
