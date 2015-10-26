#encoding:utf-8

'''
Created on 2015年10月19日

@author: weiqinmeng
'''

import os

class Tss():
    def osPath(self):
        self.osPaths = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir,os.pardir))
        self.r = 'r'
        print self.r + "'" + os.path.join(self.osPaths,'chromedriver.exe') + "'"
        



t = Tss()
t.osPath()

# class Student(object):
#     
#     @property
#     def score(self):
#         
#         return self._score
#     
#     @score.setter
#     def score(self,value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value >100:
#             raise ValueError("score must between 0 ~ 100!")
#         self._score = value
# 
# 
# s = Student()
# s.score = 80
# print s.score