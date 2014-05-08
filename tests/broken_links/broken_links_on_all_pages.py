import unittest

from requests.exceptions import InvalidSchema, MissingSchema, ConnectionError


__author__ = 'farooque'

import nose.plugins.attrib
import requests

import src
from src import baseTest
from src import clogger
from src import config
from src.page_helpers import utils

logger = src.clogger.setup_custom_logger(__name__)

page_url = config.CliConfig().common.url + "/developers/"

visited = set()


class BrokenLinkTestSuite(baseTest.CrittercismTestCase):
    def assert_on_broken_links(self):
        session = requests.session()
        with self.multiple_assertions():
            for link in utils.get_all_links(self.browser):
                # This means either we are out of portal or already visited the link
                if "crittercism.com" not in link or link in visited:
                    logger.debug("Skipping link %s because it is either visited or not a crittercism link" % link)
                    continue

                visited.add(link)
                logger.debug("Going to  '%s'" % link)
                try:
                    resp = session.get(link)
                    self.assertTrue((resp.status_code not in [500, 404]),
                                    ("Return code %s URL %s" % (resp.status_code, link)))

                    self.browser.get(link)
                    #Needs to login instead any of the link redirect us to login page
                    if "login" in self.browser.current_url and self.browser.find_elements_by_id('email').__len__() > 1:
                        utils.login()

                    element = self.browser.find_elements_by_xpath(
                        '//*[contains(text(),"Well, this is embarrassing - you found a broken link.")]').__len__()
                    self.assertGreater(1, element, "Found a broken Link : " + link)
                    # call itself if the link contains crittercism else it will crawl the entire web :)
                    self.assert_on_broken_links()
                except (InvalidSchema, MissingSchema, ConnectionError):
                    continue

    @classmethod
    def setUpClass(cls):
        super(BrokenLinkTestSuite, cls).setUpClass()

    def setUp(self):
        pass


    @nose.plugins.attrib.attr(genre='links')
    def test_broken_links_developers_page(self):
        page_url = config.CliConfig().common.url + "/developers/"
        self.browser.get(page_url)
        self.assert_on_broken_links()

    @nose.plugins.attrib.attr(genre='links')
    def test_broken_links_support_page(self):
        page_url = "http://support.crittercism.com/"
        self.browser.get(page_url)
        self.assert_on_broken_links()


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        super(BrokenLinkTestSuite, cls).tearDownClass()
        logger.info("Finished executing BrokenLinkTestSuite")
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)