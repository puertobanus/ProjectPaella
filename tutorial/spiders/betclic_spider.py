# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy,psycopg2


from tutorial.items import BetclicItem

class BetclicSpider(scrapy.Spider):
    name = "betclic"
    allowed_domains = ["betclic.fr"]
    start_urls = [
        "https://www.betclic.fr/football/ligue-1-e4",
      #  "https://www.betclic.fr/football/angl-premier-league-e3",
    ]

    def parse(self, response):
        conn = psycopg2.connect(database="postgres", user="postgres", password="Martin00")
        print "XXXXXXXXXXXXXXXX1"
        # tu vois ce changement? (lundi aprem)
        print conn
        print "XXXXXXXXXXXXXXX2"
        cur = conn.cursor()
        #cur.execute("CREATE TABLE test2 (id serial PRIMARY KEY, num integer, data varchar);")
        print "XXXXXXXXXXXXXXX3"
        cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",(100, "abc'def"))
        print "XXXXXXXXXXXXXXX4"
        cur.execute("SELECT * FROM test;")
        print cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

    #    print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
     #   for day in response.xpath('.//div[@class="entry day-entry grid-9 nm"]'):
      #      print day.xpath('.//time/@datetime').extract()
       #     for hour in day.xpath('.//div[@class="schedule clearfix"]'):
        #        print hour.xpath('.//div[@class="hour"]/text()').extract()
         #       for game in hour.xpath('.//div[@class="match-entry clearfix CompetitionEvtSpe "]'):
          #          print game.xpath('.//div[@class="match-name"]/a/text()').extract()
           #         print game.xpath('.//div[@class="match-odd"]/span/text()').extract()
            #print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            






# response.xpath('//div/@data-track-event-name').extract()
#         print sel.xpath('.//div/@data-track-event-name').extract()
# entry day-entry grid-9 nm
# schedule clearfix
# "match-entry clearfix CompetitionEvtSpe "
# match-odds
     #  print response.__class__
      # print sel.__class__
      # for i in range(1,6):
      #      match = sel[i].xpath('//div/@data-track-event-name').extract()
      #    
  #      match = sel.xpath('//div/@data-track-event-name').extract()
   #     print match
