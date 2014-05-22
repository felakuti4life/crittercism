import random
import unittest
from selenium.webdriver.common.by import By
from src.page_helpers import team
from src.page_helpers import utils

__author__ = 'farooque'

import nose.plugins.attrib

import src
from src import baseTest
from src.data_driven_test_wrapper import ddt_list, data, data_driven_test


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


@data_driven_test
class CrashReportTestSuite(baseTest.CrittercismTestCase):
    app_ids = []

    @classmethod
    def setUpClass(cls):
        super(CrashReportTestSuite, cls).setUpClass()
        cls.browser.get(cls.config.common.url + "/developers/register-application")
        app_name = "IOS-" + str(random.random())
        cls.browser.find_element_by_id("app-name").send_keys(app_name)
        #cls.browser.find_element_by_id("commit").click()
        cls.assertFalse(utils.find_element_and_submit(cls.browser, By.NAME, 'commit'),
                                 " Broken link at " + cls.browser.current_url)

        CrashReportTestSuite.app_ids = team.get_id_from_app_name(browser=cls.browser, app_name=app_name)


    def setUp(self):
        self.browser.get(self.config.common.url + "/developers/crash-summary/" + CrashReportTestSuite.app_ids[0])
        pass


    @nose.plugins.attrib.attr(sample=True, genre="crash-report")
    @data(generate_list_of_crash_types())
    @ddt_list
    def test_crash_data(self, value=None):
        __name__ + """ [Test] Verify the crash data of all crash types"""

        for period in self.browser.find_elements_by_xpath("//label/span[@class='ui-button-text']"):
            logger.debug("working on period %s" % period.text)
            #period.click()
            self.assertFalse(utils.click(browser=self.browser, web_element=period),
                                 " Broken link at " + self.browser.current_url)


            self.assertFalse(utils.find_element_and_click(self.browser, By.NAME, 'add-team-member'),
                                 " Broken link at " + self.browser.current_url)

            with self.multiple_assertions():
                self.assertEqual(self.browser.find_element_by_id("stats-number-today").text,"0",
                                 ("Expecting No crash but found %s" % self.browser.find_element_by_id("stats-number-today").text) )

                self.assertEqual(self.browser.find_element_by_id("stats-number-week").text,"0",
                                 ("Expecting No crash but found %s" % self.browser.find_element_by_id("stats-number-week").text) )

                self.assertEqual(self.browser.find_element_by_id("stats-number-all-time").text,"0",
                                 ("Expecting No crash but found %s" % self.browser.find_element_by_id("stats-number-all-time").text) )


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        team.delete_app_given_ids(browser=cls.browser, app_ids=CrashReportTestSuite.app_ids)
        super(CrashReportTestSuite, cls).tearDownClass()

        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
