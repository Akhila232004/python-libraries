# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Run all tests discovered under current directory
#  Author       : Team Tinitiate
# ==============================================================================



import unittest

suite = unittest.defaultTestLoader.discover(".")
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
