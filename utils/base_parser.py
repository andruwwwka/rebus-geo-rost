import re
from abc import ABCMeta, abstractmethod

from xlrd import open_workbook


class BaseXlsParser():
    __metaclass__ = ABCMeta

    def __init__(self):
        self.is_living = re.compile('(.*?)жил(.*?)дом(.*?)')
        self.is_reconstruct = re.compile('(.*?)рек(.*?)')
        self.is_rebuild = re.compile('(.*?)восст(.*?)')
        self.is_personal = re.compile('(.*?)инд(.*?)')
        self.not_living = re.compile('(.*?)пристройка(.*?)')
        self.is_road = re.compile('(.*?)дорога(.*?)')
        self.is_sport = re.compile('(.*?)комплекс(.*?)')

    @property
    @abstractmethod
    def sheet_index(self):
        # raise NotImplementedError
        return 1

    @property
    @abstractmethod
    def registry_type(self):
        # raise NotImplementedError
        return 'building'

    def good_address(self, address):
        is_living = self.is_living.search(address)
        is_reconstruct= self.is_reconstruct.search(address.lower())
        is_rebuild = self.is_rebuild.search(address.lower())
        is_personal = self.is_personal.search(address.lower())
        not_living = self.not_living.search(address.lower())
        is_road = self.is_road.search(address.lower())
        is_sport = self.is_sport.search(address.lower())
        return is_living and not is_reconstruct and not is_rebuild and not is_personal and not not_living \
               and not is_road and not is_sport

    def read(self, filename='../data/Reestr-vydanyh-razesheniy-160419.xls'):

        book = open_workbook(filename)
        sheet = book.sheet_by_index(self.sheet_index)
        for row_index in range(1, sheet.nrows):
            address = sheet.cell(row_index, 2).value
            if address and self.good_address(address):
                # print(sheet.cell(row_index, 0))
                # print(sheet.cell(row_index, 1))
                print(sheet.cell(row_index, 2).value)
        return None

BaseXlsParser().read()
