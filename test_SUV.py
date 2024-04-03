# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 14:59:46 2024

@author: vidus
"""

import re

def Extract_SUV():
    
    with open("20200527152905.861802.ig.tum","r") as f:
        
        lines = f.read()
    
    results = re.findall("(M.*[^RC]SUVValue) = (\d+\.\d+)",lines)

if __name__ == "__main__":
    
    Extract_SUV