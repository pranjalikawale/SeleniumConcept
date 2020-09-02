from selenium import webdriver
from collections import Counter 
import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestForNewsHeadline():

    def test_for_news_headline(self,initialize_driver):
        self.driver=initialize_driver
        while True:
            try:
                # Define an element that you can start scraping when it appears
                # If the element appears after 5 seconds, break the loop and continue
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "storylink")))
                break
            except TimeoutException:
                # If the loading took too long, print message and try again
                print("Loading took too much time!")
            
        try:
            #headline
            headline_list=[]
            headline_webelement=[]
            headline_webelement=self.driver.find_elements_by_class_name("storylink")
            for item in headline_webelement:
                headline_list.append(item.text)
            headline_word_list = str(headline_list).replace(',', '').replace('\'','').split()
            most_common_headline_word_list=[word for word, word_count in Counter(headline_word_list).most_common(1)]
            print(most_common_headline_word_list[0])

            while True:
                try:
                    # Define an element that you can start scraping when it appears
                    # If the element appears after 5 seconds, break the loop and continue
                    WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "score")))
                    break
                except TimeoutException:
                    # If the loading took too long, print message and try again
                    print("Loading took too much time!")

            #point or score
            score=[]
            score_webelement=[]
            score_webelement=self.driver.find_elements_by_class_name("score")
            for item in score_webelement:
                score.append(item.text)
            score_point_list = str(score).replace(',', '').replace('\'','').replace('points','').replace('[','').replace(']','').split()
            score_point_list=list(map(int,score_point_list)) 
            print(max(score_point_list))

            #dictionary
            dic_news_headlines={}
            dic_news_headlines = dict(zip(headline_list, score_point_list)) 
            dic_news_headlines_max = max(dic_news_headlines, key=dic_news_headlines.get) 
            print(dic_news_headlines_max) 
        except NoSuchElementException as exception:
            print("Element not found and test failed")
        

