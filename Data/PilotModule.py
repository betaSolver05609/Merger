# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 21:51:32 2019

@author: Someindra Kumar Singh
"""
from Merger import MergerThroughFileName;


def main():
    SourceFolder=input('Enter Source Folder Path: ')
    OutputFileName=input('Enter Op File Name: ')
    m=MergerThroughFileName(SourceFolder, OutputFileName)
    m.MergeFilesHorizantally();
    

if __name__=='__main__':
    main();
