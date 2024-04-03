# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 14:59:46 2024

@author: vidus
"""

import re
import argparse
import numpy as np

parser = argparse.ArgumentParser(prog="TumFileReader",description="Read tum file")

parser.add_argument("file",help=".tum file name")

args = parser.parse_args()
file_name = args.file

def extract_SUV(chaine):
    
    SUV_values = re.findall("(M.*[^RC]SUVValue) = (\d+\.\d+)",chaine)
    
    return SUV_values 

def extract_UH(chaine):
    
    UH_values = re.findall("(M.*HUValue) = (\d+(\.\d+)?)",chaine)
    
    return UH_values 

def ouverture_fichier(fic):
    
    with open(fic,"r") as f:
        
        lines = f.read()
        
    return lines

def save_resultat(name,data_extract):
    
    """name : file name with .txt format
        data-extract : data to save in the txt file """
    
    with open(name,'w') as tx : 
        
        tx.writelines(data[0]+","+data[1]+"\n" for data in data_extract)


def Extract_SUV_UH():
    
    lines = ouverture_fichier(file_name)
    results_SUV = extract_SUV(lines)
    results_UH = extract_UH(lines)
    
    save_resultat("SUV_data.txt",results_SUV)
    save_resultat("UH_data.txt",results_UH)

    
if __name__ == "__main__":
    
    Extract_SUV_UH()
