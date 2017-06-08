import jieba
import re
from collections import Counter

class Stutter(object):

    """Init the stutter
        This stutter class is built to handle with the 
       chinese text segmentation with the jieba Chinese
       word segmentation module.

    """

    def __init__(self, text, word_list):
        """init the stutter class

        :text_list: the text list 
        :word_list: the key word list which needs to be count

        """
        self._text_list = self.split_article(text)
        self._word_list = word_list
        
    def statistics(self):
        """count the number of each Chinese word

        :full_list: the full list returned by split function
        :returns: a dict that contains Chinese word and repeated times

        """
        item_list = list()
        for i in self._word_list:
            jieba.add_word(i)
        for item in full_list:
            cut_list = jieba.lcut(item)
            item_list += cut_list
        statistics = dict(Counter(item_list))
        statistics_copy = statistics.copy()
        for key, value in statistics_copy.items():
            if len(key) < 2:
                del statistics[key]
        statistics = sorted(statistics.items(), key=lambda d:d[1], reverse=True)
        return statistics[0:10]

    def split_article(text):
        """Split the Chinese text into the list,
        for Chinese stutter.

        :text: the full text from the file
        :returns: text in list format

        """
        full_list = re.split('\n|。|!|！|\.', text)

        return full_list
