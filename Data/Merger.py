# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 21:16:28 2019

@author: Dell inspiron
"""
import pandas as pd
import glob
import os;

class MergerThroughFileName(object):
    def __init__(self,source, nof='Output.xls'):
        self.SourceFolder=source
        self.NameOfOutputFile=nof
    def MergeFilesHorizantally(self):
        df=pd.DataFrame();
        os.chdir(self.SourceFolder)
        LIST_OF_FILE=glob.glob('*');
        print(LIST_OF_FILE)
        for f in LIST_OF_FILE:
            data=pd.read_excel(f)
            df=df.append(data)
        df.to_excel(self.NameOfOutputFile)
    
        
        
#Path=r'C:\Users\Dell inspiron\Desktop\Prod\Data'
#OpFile='Output.xls'

#m=MergerThroughFileName(Path, OpFile);
#m.MergeFilesHorizantally();