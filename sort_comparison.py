# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 15:44:55 2020

@author: ardaegeunlu
"""

import re

def LCCSortComparison(call1, call2):
    
    preCutter1, postCutter1 = SeperateViaCutter(call1)
    preCutter2, postCutter2 = SeperateViaCutter(call2)
    
    preCutterComp = PreCutterComparison(preCutter1, preCutter2)
    
    if preCutterComp != 0:
        return preCutterComp
    else:
        return PostCutterComparison(postCutter1, postCutter2)
        
    
# Seperate the string into two parts at the cutter    
def SeperateViaCutter(callno):
    
    # the cutter is a DOT FOLLOWED BY A LETTER
    cutter = re.search('\.\D+', callno)
    if cutter != None:
        return callno[:cutter.start()], callno[cutter.start()+1:]
    
    else:
        return callno, ''
    
# The cutter is generally made of two parts, a combination of letters, followed by a decimal
# There are occasional irregularities, date, vol., edition etc. which normally should be after
# cutter are sometimes before the cutter. (perhaps clerical errors?)

def SeperatePreCutterToParts(callno):
    
    # find the decimal numbers span
    parts = re.search('[-+]?\d*\.\d+|\d+', callno)
    
    if parts == None:
        return callno, 0
    else:
        
        spaceSplitParts = IsPreCutterSpaced(callno[parts.start():])
        
        # uncommon-irregular format ------
        # if there is white space before the cutter, date or vol. it is
        # probably because they are placed pre-cutter
        # throw away non-digits and merge
        if len(spaceSplitParts) > 1:
            
            return callno[:parts.start()], float(''.join([s for s in callno[parts.start():] if s.isdigit()]))
        else:
            return callno[:parts.start()], float(callno[parts.start():parts.end()])

# refer to above method
def IsPreCutterSpaced(part):
    
    return part.split()

# compare string parts lexicographically, compare floats in regular manner
def PreCutterComparison(call1, call2):
    
    lex1, num1 = SeperatePreCutterToParts(call1)
    lex2, num2 = SeperatePreCutterToParts(call2)
    
    if lex1 < lex2:
        
        return -1
    
    elif lex1 > lex2:
        
        return 1
    
    else:
        # lexical parts are same, compare decimals
        
        if num1 < num2:
            return -1
        elif num1 > num2:
            return 1
        else:
            return 0
    
# compare initial letter groups, then compare the rest of the string
# char by char, digits take precendence in the latter part

def PostCutterComparison(call1, call2):
    
    lex1, rest1 = SeperatePostCutterToParts(call1)
    lex2, rest2 = SeperatePostCutterToParts(call2)
    
    if lex1 < lex2:
        
        return -1
    
    elif lex1 > lex2:
        
        return 1
    
    else:
        
        # this split is necessary to seperate the vol/edition parts which come after a spacing
        pieces1 = rest1.split(' ', 1)
        pieces2 = rest2.split(' ', 1)
        
        for a, b in zip(pieces1[0], pieces2[0]):
            if not str.isdigit(a) and str.isdigit(b):
                return -1
            elif str.isdigit(a) and not str.isdigit(b):
                return 1
            else:
                if a > b:
                    return 1
                elif a < b:
                    return -1
                # else continue the loop
        
        if len(pieces1[0]) > len(pieces2[0]):
            return 1
        elif len(pieces1[0]) < len(pieces2[0]):
            return -1
        
        if len(pieces1) > 1 and len(pieces2) > 1:
                
            num_data1 = ''.join([s for s in pieces1[1] if s.isdigit() and ord(s) < 128])
            num_data2 = ''.join([s for s in pieces2[1] if s.isdigit() and ord(s) < 128])
            
            if len(num_data1) > 0 and len(num_data2) > 0:
                num_data_1 = int(num_data1)
                num_data_2 = int(num_data2)  
                
                
                if num_data_1 > num_data_2:
                    # print(num_data1 + '>' + num_data2)
                    return 1
                elif num_data_1 < num_data_2:
                    # print(num_data1 + '<' + num_data2)
                    return -1

        # if still havent returned, one of the strings have expired
        # the shorter string should sort first
            
        if len(rest1) > len(rest2):
            return 1
        else:
            return -1
            
    
# the two parts are initial letter group followed by digits and possibly chars again
# eg. callno = QA1.A123B2 post-cutter = A123B2, A is letter group 123B2 is the rest.
def SeperatePostCutterToParts(callno):
    
    cutter = re.search('\D+', callno)
    
    if cutter != None:
        
        lexPart = callno[cutter.start():cutter.end()]
        rest = callno[cutter.end():]
    
        return lexPart, rest
    
    else:
        return callno, ''
    
    


    
