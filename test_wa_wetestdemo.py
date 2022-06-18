# -*- coding: UTF-8 -*-
from uitrace.api import *
import pytest

record_dir=os.environ.get("RECORD_DIR")
output_dir = os.path.join(record_dir, "wa_log") if record_dir else ""

app_package = "com.tencent.wetestdemo"
app_activity = "{}.{}".format(app_package, ".LoginActivity")

class TestWetestDemo:
    @classmethod
    def setup_class(cls):
        init_driver(output_dir=output_dir)
        press(DeviceButton.HOME)
        time.sleep(1)

    @classmethod
    def teardown_class(cls):
        press(DeviceButton.HOME)
        stop_driver()

    def setup_method(self,method):
        start_app(app_package)
        time.sleep(1)


    def teardown_method(self,method):
        stop_app(app_package)
        press(DeviceButton.HOME)
        time.sleep(1)
    
    def test_login(self):
        restart_app(app_package)
        click('//android.view.ViewGroup[@resource-id="com.tencent.wetestdemo:id/container"]/android.widget.EditText[@text="Username" and @resource-id="com.tencent.wetestdemo:id/username"]', by=DriverType.UI, timeout=20)
        input_text("admin")
        click('//android.view.ViewGroup[@resource-id="com.tencent.wetestdemo:id/container"]/android.widget.EditText[@text="Password" and @resource-id="com.tencent.wetestdemo:id/password"]', by=DriverType.UI, timeout=20)
        input_text("admin")
        click('//android.view.ViewGroup[@resource-id="com.tencent.wetestdemo:id/container"]/android.widget.Button[@text="SIGNIN" and @resource-id="com.tencent.wetestdemo:id/login"]', by=DriverType.UI, timeout=20)
        time.sleep(1)
    
    @pytest.mark.run(order=1)
    def test_select_with_click(self):
        self.test_login()
        click('//android.widget.ListView[@resource-id="com.tencent.wetestdemo:id/list_item"]/android.widget.CheckedTextView[@text="Item0" and @resource-id="android:id/text1"]', by=DriverType.UI, timeout=20)
        click('//android.widget.ListView[@resource-id="com.tencent.wetestdemo:id/list_item"]/android.widget.CheckedTextView[@text="Item5" and @resource-id="android:id/text1"]', by=DriverType.UI, timeout=20)
        click('//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.LinearLayout/android.widget.Button[@text="SUBMIT" and @resource-id="com.tencent.wetestdemo:id/submitbtn"]', by=DriverType.UI, timeout=20)
        time.sleep(2)

    def test_select_with_swipe(self):
        self.test_login()
        click('//android.widget.ListView[@resource-id="com.tencent.wetestdemo:id/list_item"]/android.widget.CheckedTextView[@text="Item0" and @resource-id="android:id/text1"]', by=DriverType.UI, timeout=20)
        click('//android.widget.ListView[@resource-id="com.tencent.wetestdemo:id/list_item"]/android.widget.CheckedTextView[@text="Item5" and @resource-id="android:id/text1"]', by=DriverType.UI, timeout=20)
        slide(loc_from='//android.widget.ListView[@resource-id="com.tencent.wetestdemo:id/list_item"]/android.widget.CheckedTextView[@text="Item10" and @resource-id="android:id/text1"]', loc_shift=(0.119, -0.62), by=DriverType.UI)
        click([0.571, 0.824], by=DriverType.POS, duration=0.05)
        click('//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.LinearLayout/android.widget.Button[@text="SUBMIT" and @resource-id="com.tencent.wetestdemo:id/submitbtn"]', by=DriverType.UI, timeout=20)