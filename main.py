# -*- coding: UTF-8 -*-
try:
    from uitrace.api import *
except:
    print("cannot import module uitrace.api")

# test platform start
import os
print("adb devices: ")
print(os.system("adb devices"))
print("env: ")
print(os.system("env"))
# test platform end


case_names = ["test_login", "test_select_with_swipe", "test_select_with_click"]
cases = [ "test_wa_wetestdemo.py::TestWetestDemo::{}".format(i) for i in case_names ]
print("{}".format(cases))
pytest_main(default_cases=cases)