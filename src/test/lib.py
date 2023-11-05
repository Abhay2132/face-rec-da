import os


cwd = os.sep.join(__file__.split(os.sep)[:-1])
print("cwd : " , cwd) # os.path.join(__file__, "..", "..", "main.py"))
print(__file__)