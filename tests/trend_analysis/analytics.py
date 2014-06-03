from datetime import time
import inspect
from selenium.webdriver.common.by import By

import random
import selenium.webdriver.common.keys
import unittest2 as unittest
import nose.plugins.attrib

import src
from src import baseTest
from src.page_helpers import team
from src.data_driven_test_wrapper import ddt_list, data, data_driven_test
from src.page_helpers import utils

__author__ = 'ethan'

logger = src.clogger.setup_custom_logger(__name__)

def generate_list_of_crash_types():
    """



    :rtype : object
    :return:
    """
    crash_types = []
    crash_types.append("all")
    crash_types.append("resolved")
    crash_types.append("known")
    crash_types.append("unresolved")
    return crash_types

class AnalyticsTestSuite(baseTest.CrittercismTestCase):
    app_ids= []

    @classmethod
    def setUpClass(cls):
        """


        """
        super(AnalyticsTestSuite, cls).setUpClass()
        #cls.browser.get(cls.config.common.url + "/developers/analytics/52fb0fdb8b2e3365c6000008")
        AnalyticsTestSuite.app_ids = team.get_id_from_app_name(browser=cls.browser, app_name="Crittercism Demo")

    def setUp(self):
        """
        Setup for the testcase


        """
        self.browser.get(self.config.common.url + "/developers/analytics/" + AnalyticsTestSuite.app_ids[0])
        pass


    @nose.plugins.attrib.attr(genre='analytics')
    #@unittest.skip("Reason : why it is skipped")
    def test_au_version(self):
        """
            1) Today's DAU and MAU

        """
        __name__ + """[Test] test that DAU is returned below graph"""
        empty_string = ""
        #data is a dummy string that will later be replaced with actual data
        with self.multiple_assertions():
            self.assertNotEqual(first= self.get_web_element(value='//*[@id="dau-container"]/../div[3]/strong').text,
                                second=empty_string,
                                msg="DAU result does not appear")
            self.assertNotEqual(first= self.get_web_element(value='//*[@id="dau-container"]/../div[3]/span').text,
                                second=empty_string,
                                msg="MAU result does not appear")

            pass

    ######### BY VERSION ############
    @nose.plugins.attrib.attr(genre='analytics')
    def test_todays_apploads_crashes_version(self):
        """
            2) crashes vs application loads by version
        """
        versions = []
        versions.append(self.get_web_element(
            value='//*[@id="crashes-ratio-container"]/../div[2]/div[2]/strong').text)
        #versions.append(self.get_web_element(
         #   value='//*[@id="crashes-ratio-container"]/../div[2]/div[3]/strong').text)

        crashes = []
        crashes.append(self.get_web_element(
            value='//*[@id="crashes-ratio-container"]/../div[2]/div[2]/span').text)
        #crashes.append(self.get_web_element(
        #    value='//*[@id="crashes-ratio-container"]/../div[2]/div[3]/span').text)
        crash_table = dict(zip(versions, crashes))
        blank_data = {"1.0.0.0":"",
                      "0.4.2":""}

        self.assertFalse(crash_table == blank_data, "Listed apploads data does not match given data")


    @nose.plugins.attrib.attr(genre='analytics')
    def test_todays_dau_crashes_version(self):
        """
            3) crashes vs DAU by version
        """
        versions = []
        versions.append(self.get_web_element(
            value='//*[@id="crashes-ratio-container"]/../div[2]/div[2]/strong').text)
        #versions.append(self.get_web_element(
        #    value='//*[@id="crashes-ratio-container"]/../div[2]/div[3]/strong').text)

        crashes = []
        crashes.append(self.get_web_element(
            value='//*[@id="affected-users-ratio-container"]/../div[2]/div[2]/span').text)
        #crashes.append(self.get_web_element(
        #    value='//*[@id="affected-users-ratio-container"]/../div[2]/div[3]/span').text)
        crash_table = dict(zip(versions, crashes))
        blank_data = {"1.0.0.0":"",
                      "0.4.2":""}

        self.assertNotEqual(crash_table, blank_data, "Daily Active Users that crashed by version does not match given data")

    @nose.plugins.attrib.attr(genre='analytics')
    def test_todays_apploads_version(self):
        """
            4) app loads by version
        """
        versions = []
        versions.append(self.get_web_element(
            value='//*[@id="app-load-version-container"]/../div[2]/div[2]/strong').text)
        #versions.append(self.get_web_element(
        #    value='//*[@id="app-load-version-container"]/../div[2]/div[3]/strong').text)

        crashes = []
        crashes.append(self.get_web_element(
            value='//*[@id="app-load-version-container"]/../div[2]/div[2]/span').text)
        #crashes.append(self.get_web_element(
        #    value='//*[@id="app-load-version-container"]/../div[2]/div[3]/span').text)
        crash_table = dict(zip(versions, crashes))

        blank_data = {"1.0.0.0":"",
                      "0.4.2":""}


        self.assertNotEqual(crash_table, blank_data, "App loads by version does not match given data")

    @nose.plugins.attrib.attr(genre='analytics')
    def test_todays_dau_version(self):
        """
            5) daily active users by version
        """
        versions = []
        versions.append(self.get_web_element(
            value='//*[@id="dau-version-container"]/../div[2]/div[2]/strong').text)
        #versions.append(self.get_web_element(
        #    value='//*[@id="dau-version-container"]/../div[2]/div[3]/strong').text)

        crashes = []
        crashes.append(self.get_web_element(
            value='//*[@id="dau-version-container"]/../div[2]/div[2]/span').text)
        #crashes.append(self.get_web_element(
        #    value='//*[@id="dau-version-container"]/../div[2]/div[3]/span').text)
        crash_table = dict(zip(versions, crashes))
        blank_data = {"1.0.0.0":"",
                      "0.4.2":""}

        self.assertNotEqual(crash_table, blank_data, "Daily Active Users by version does not match given data")

    @nose.plugins.attrib.attr(genre='analytics')
    def test_todays_crashes_version(self):
        """
            6) crashes by version
        """
        versions = []
        versions.append(self.get_web_element(
            value='//*[@id="crashes-version-container"]/../div[2]/div[2]/strong').text)
        #versions.append(self.get_web_element(
        #    value='//*[@id="crashes-version-container"]/../div[2]/div[3]/strong').text)

        crashes = []
        crashes.append(self.get_web_element(
            value='//*[@id="crashes-version-container"]/../div[2]/div[2]/span').text)
        #crashes.append(self.get_web_element(
        #    value='//*[@id="crashes-version-container"]/../div[2]/div[3]/span').text)
        crash_table = dict(zip(versions, crashes))
        blank_data = {"1.0.0.0":"",
                      "0.4.2":""}
        self.assertNotEqual(crash_table, blank_data, "Crashes by version does not match given data")

    @nose.plugins.attrib.attr(genre='analytics')
    def test_todays_affected_users_version(self):
        """
            7) users affected by at least one crash by version
        """
        versions = []
        versions.append(self.get_web_element(
            value='//*[@id="affected-users-version-container"]/../div[2]/div[2]/strong').text)
        #versions.append(self.get_web_element(
        #    value='//*[@id="affected-users-version-container"]/../div[2]/div[3]/strong').text)

        crashes = []
        crashes.append(self.get_web_element(
            value='//*[@id="affected-users-version-container"]/../div[2]/div[2]/span').text)
        #crashes.append(self.get_web_element(
        #    value='//*[@id="affected-users-version-container"]/../div[2]/div[2]/span').text)
        crash_table = dict(zip(versions, crashes))
        blank_data = {"1.0.0.0":"",
                      "0.4.2":""}

        self.assertNotEqual(crash_table, blank_data, "Affected users by version does not match given data")

    ############ BY DEVICE ##############
    @nose.plugins.attrib.attr(genre='analytics')
    def test_todays_apploads_device(self):
        """
            8) App Loads by Device
        """
        versions = []
        versions.append(self.get_web_element(
            value='//*[@id="app-load-device-container"]/../div[2]/div[2]/strong').text)
        versions.append(self.get_web_element(
            value='//*[@id="app-load-device-container"]/../div[2]/div[3]/strong').text)
        versions.append(self.get_web_element(
            value='//*[@id="app-load-device-container"]/../div[2]/div[4]/strong').text)
        versions.append(self.get_web_element(
            value='//*[@id="app-load-device-container"]/../div[2]/div[5]/strong').text)
        versions.append(self.get_web_element(
            value='//*[@id="app-load-device-container"]/../div[2]/div[6]/strong').text)

        crashes = []
        crashes.append(self.get_web_element(
            value='//*[@id="app-load-device-container"]/../div[2]/div[2]/span').text)
        crashes.append(self.get_web_element(
            value='//*[@id="app-load-device-container"]/../div[2]/div[3]/span').text)
        crashes.append(self.get_web_element(
            value='//*[@id="app-load-device-container"]/../div[2]/div[4]/span').text)
        crashes.append(self.get_web_element(
            value='//*[@id="app-load-device-container"]/../div[2]/div[5]/span').text)
        crashes.append(self.get_web_element(
            value='//*[@id="app-load-device-container"]/../div[2]/div[6]/span').text)

        crash_table = dict(zip(versions, crashes))
        blank_data = {"iPhone 4s":"",
                      "iPhone 5 CDMA+LTE":"",
                      "iPhone 4 CDMA":"",
                      "2nd Gen iPad mini Retina, WiFi/Cellular":"",
                      "2nd Gen iPad mini Retina, WiFi":""}

        self.assertNotEqual(crash_table, blank_data, "App loads by device does not match given data")

    @nose.plugins.attrib.attr(genre='analytics')
    def test_todays_crashes_device(self):
        """
            9) Crashes by Device
        """
        versions = []
        versions.append(self.get_web_element(
            value='//*[@id="crashes-device-container"]/../div[2]/div[2]/strong').text)
        versions.append(self.get_web_element(
            value='//*[@id="crashes-device-container"]/../div[2]/div[3]/strong').text)
        versions.append(self.get_web_element(
            value='//*[@id="crashes-device-container"]/../div[2]/div[4]/strong').text)
        versions.append(self.get_web_element(
            value='//*[@id="crashes-device-container"]/../div[2]/div[5]/strong').text)
        versions.append(self.get_web_element(
            value='//*[@id="crashes-device-container"]/../div[2]/div[6]/strong').text)

        crashes = []
        crashes.append(self.get_web_element(
            value='//*[@id="crashes-device-container"]/../div[2]/div[2]/strong').text)
        crashes.append(self.get_web_element(
            value='//*[@id="crashes-device-container"]/../div[2]/div[2]/strong').text)
        crashes.append(self.get_web_element(
            value='//*[@id="crashes-device-container"]/../div[2]/div[2]/strong').text)
        crashes.append(self.get_web_element(
            value='//*[@id="crashes-device-container"]/../div[2]/div[2]/strong').text)
        crashes.append(self.get_web_element(
            value='//*[@id="crashes-device-container"]/../div[2]/div[2]/strong').text)

        crash_table = dict(zip(versions, crashes))
        blank_data = {"iPhone 4s":"",
                      "iPhone 5 CDMA+LTE":"",
                      "iPhone 4 CDMA":"",
                      "2nd Gen iPad mini Retina, WiFi/Cellular":"",
                      "2nd Gen iPad mini Retina, WiFi":""}

        self.assertNotEqual(crash_table, blank_data, "Crashes by device does not match given data")

    @nose.plugins.attrib.attr(genre='analytics')
    def test_todays_appload_crashes_device(self):
        """
            10) % of Apploads that Crashed by Device
        """
        versions = []
        versions.append(self.get_web_element(
            value="/html/body/div[3]/div/div[5]/div[4]/div/div[2]/div[2]/strong").text)
        versions.append(self.get_web_element(
            value="/html/body/div[3]/div/div[5]/div[4]/div/div[2]/div[3]/strong").text)
        versions.append(self.get_web_element(
            value="/html/body/div[3]/div/div[5]/div[4]/div/div[2]/div[4]/strong").text)
        versions.append(self.get_web_element(
            value="/html/body/div[3]/div/div[5]/div[4]/div/div[2]/div[5]/strong").text)
        versions.append(self.get_web_element(
            value="/html/body/div[3]/div/div[5]/div[4]/div/div[2]/div[6]/strong").text)

        crashes = []
        crashes.append(self.get_web_element(
            value="/html/body/div[3]/div/div[5]/div[4]/div/div[2]/div[2]/strong").text)
        crashes.append(self.get_web_element(
            value="/html/body/div[3]/div/div[5]/div[4]/div/div[2]/div[2]/strong").text)
        crashes.append(self.get_web_element(
            value="/html/body/div[3]/div/div[5]/div[4]/div/div[2]/div[2]/strong").text)
        crashes.append(self.get_web_element(
            value="/html/body/div[3]/div/div[5]/div[4]/div/div[2]/div[2]/strong").text)
        crashes.append(self.get_web_element(
            value="/html/body/div[3]/div/div[5]/div[4]/div/div[2]/div[2]/strong").text)

        crash_table = dict(zip(versions, crashes))
        blank_data = {"iPhone 4s":"0.0%",
                      "iPhone 5 CDMA+LTE":"0.0%",
                      "iPhone 4 CDMA":"0.0%",
                      "2nd Gen iPad mini Retina, WiFi/Cellular":"0.0%",
                      "2nd Gen iPad mini Retina, WiFi":"0,0%"}

        self.assertEqual(crash_table, blank_data, "Apploads that crashed by device does not match given data")

    def tearDown(self):
       pass


    @classmethod
    def tearDownClass(cls):
        super(AnalyticsTestSuite, cls).tearDownClass()
        logger.info("Finished executing AnalyticsTestSuite")
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)