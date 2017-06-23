from selenium import webdriver
from pyvirtualdisplay import Display
from googletrans import Translator as GoogleTrans
import time
import re

RE_COMMA = re.compile('(,|，|.|。|!|！|？|\?|\n|……)')
class BingTranslator(object):

    """Translate the text
       Simple Usage:
       text_list = ["I have a dream", "heaven fall"]
       translation = BingTranslator(src_text=text_list)
       translation.translat()
       print(translation.trans)
    """

    def __init__(self, src_text, tar_lang='zh-CN'):
        """Initilize the class """
        self.site = "https://www.bing.com/translator/?mkt=zh-CN"
        self.lang_selector_xpath = "(.//*[@id='LS_LangList']/div)[2]"
        self._src_text = src_text
        self._tar_lang = tar_lang
        # hide the Firefox interface
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()
        # start Firefox
        self.browser = webdriver.Firefox()
        self.browser.get(self.site)
        self.input = self.browser.find_element_by_id("srcText")
        self.output = self.browser.find_element_by_id("destText")
        self._lang_xpath =self.lang_xpath()
        self.lang_selector = self.browser.find_element_by_xpath(self.lang_selector_xpath)
        self.lang_selector_chinese = self.browser.find_element_by_xpath(self._lang_xpath)
        self.trans = list()

    def translate(self):
        """Translate the src_text to target language
        finally set the result to self.trans

        """
        # simulate the webbroser to click the language button
        src_text = self._src_text
        self.lang_selector.click()
        self.lang_selector_chinese.click()

        for sentense in src_text:
            if not re.match(RE_COMMA, item):
                self.input.clear()
                self.input.send_keys(sentense)
                time.sleep(1)
                self.trans.append((sentense, self.output.text))
            else :
                self.trans.append((sentense, sentense))

        # stop the simulation and set the result
        self.browser.quit()
        self.display.stop()

    def lang_xpath(self):
        """return a button xpath

        :lang: option languages
                'zh-CN'
                'zh-TW'
                'jp'
                'de'
                'fr'
        :returns: xpath of language 

        """
        lang = self._tar_lang
        if lang == 'zh-CN':
            return "(.//*[@id='LS_LangList']/table/tbody/tr[8]/td[1])[2]"
        elif lang == 'zh-TW':
            return "(.//*[@id='LS_LangList']/table/tbody/tr[9]/td[1])[2]"
        elif lang == 'jp':
            return "(.//*[@id='LS_LangList']/table/tbody/tr[8]/td[2])[2]"
        elif lang == 'de':
            return "(.//*[@id='LS_LangList']/table/tbody/tr[13]/td[2])[2]"
        elif lang == 'fr':
            return "(.//*[@id='LS_LangList']/table/tbody/tr[19]/td[2])[2]"

class GoogleTranslator(object):
    """
    create a class to translate text with google
    """
    def __init__(self, src_text, tar_lang='zh-CN'):
        self._src_text = src_text
        self._tar_lang = tar_lang
        self.trans = list()

    def translate(self):
        trans = GoogleTrans()
        translation = trans.detect(text=self._src_text[0])
        src_lang = translation.lang
        src_text = self._src_text
        tar_lang = self._tar_lang

        for sentense in src_text:
            if not re.match(RE_COMMA, sentense):
                translation = trans.translate(sentense, src=src_lang, dest=tar_lang)
                self.trans.append((sentense, translation.text))
            else :
                self.trans.append((sentense, sentense))

class article_splitor(object):

    """The class is used for spliting article"""

    def __init__(self, text):
        """Initilize the class

        :text: the source text
        :text_list: return text list splited by comma

        """
        self._text = text
        self.text_list = split_text()

    def split_text(self):
        """main split function
        :returns: TODO

        """
        text = self._text
        return re.split(RE_COMMA, text)
