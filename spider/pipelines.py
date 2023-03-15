# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import openpyxl
from itemadapter import ItemAdapter


class SpiderPipeline:
    # def __init__(self):
    #     self.wb = openpyxl.Workbook()
    #     self.ws = self.wb.active
    #     self.ws.title = 'Top250'
    #     self.ws.append(('title', 'rating_num', 'mold', 'duration', ))
    #
    # def close_spider(self, spider):
    #     self.wb.save('data.xlsx')

    def process_item(self, item, spider):
        # title = item.get('title', '')
        # rating_num = item.get('rating_num', '')
        # mold = item.get('mold', '')
        # duration = item.get('duration', '')
        #
        # self.ws.append((title, rating_num, mold, duration, ))
        return item
