import re
from lxml import etree
import requests
import time
import global_var

class BoardsCrawler:
    domain = 'http://www.newsmth.net/'

    base_url = domain + '/nForum/section/{}?ajax'

    def __init__(self, interval = 1):
        self.interval = interval

    def get_board_of_section(self, section_idx):
        url = self.base_url.format(section_idx)
        response = requests.get(url, headers = global_var.newsmth_headers)
        time.sleep(self.interval)
        self.content = response.text
        self.tree = etree.HTML(self.content)

    def get_board_list(self, etr_obj = None ):
        if etr_obj is None:
            etr_obj = self.tree
        elements = etr_obj.xpath('//table[@class="board-list corner"]/tbody/tr')
        boards = []
        for element in elements:
            board = {}
            columns = element.xpath('td')
            if len(columns) == 1:
                break
            board['board_url'] = columns[0].xpath('a')[0].attrib['href']
            board['board_title'] = columns[0].xpath('a')[0].text

            if len(columns[1].xpath('a')) == 0:
                url = self.domain + board['board_url']
                response = requests.get(url, headers = global_var.newsmth_headers)
                child_board_etree = etree.HTML(response.text)
                boards.append(self.get_board_list(child_board_etree))
                continue

            board['manager_url'] = columns[1].xpath('a')[0].attrib['href']
            board['manager_id'] = columns[1].xpath('a')[0].text
            board['num_topics'] = columns[5].text
            board['num_posts'] = columns[6].text
            boards.append(board)
            
        return boards

if __name__ == '__main__':
    boards = []
    bc = BoardsCrawler()
    for i in range(0,10):
        bc.get_board_of_section(i)
        boards += bc.get_board_list()
        print(boards)
        break