#############################################################################################

import random

cont_idle = 0
cont_data = 0
lane0 = 0
lane1 = 0
lane2 = 0
lane3 = 0
out0  = 0
control = '0'
caseS = '0'
caseE = '0'
teste = 0
cont = 0

##  ARGUMENTO 1 ################
#   case 1 = start lane0L
#   case 2 = start lane0H
#   case 3 = start lane1L
#   case 4 = start lane1H
#   case 5 = start lane2L
#   case 6 = start lane2H
#   case 7 = start lane3L
#   case 8 = start lane3H
################################
##  ARGUMENTO 2 ################
#   case 1 = end lane0L
#   case 2 = end lane0H
#   case 3 = end lane1L
#   case 4 = end lane1H
#   case 5 = end lane2L
#   case 6 = end lane2H
#   case 7 = end lane3L
#   case 8 = end lane3H
################################

##  ARGUMENTO 1 #################
##  ARGUMENTO 2 = 0 #############
#   case 9 = end lane0L start lane2L
#   case 10 = end lane0H start lane2H
#   case 11 = end lane1L start lane3L
#   case 12 = end lane1H start lane3H
################################


SOP   = '11111011'  # 0xFB  control = 1
EOP   = '11111101'  # 0xFD  control = 1
PRE   = '11010101010101010101010101010101010101010101010101010101'
PREL  = '010101010101010101010101'  # PARTE ALTA 24BITS
PREH  = '11010101010101010101010101010101'  # PARTE BAIXA 32BITS
SFD   = '10101011'

IDLE  = '00000111'  # 0x07 control = 1
DATA0 = '11010000'  # 0xD0 control = 0
DATA1 = '11010001'  # 0xD1 control = 0
DATA2 = '11010010'  # 0xD2 control = 0
DATA3 = '11010011'  # 0xD3 control = 0

calcEndop = '10000'

import sys
caseS = sys.argv[1]
caseE = sys.argv[2]

outt  = open('test_cases/outt.txt', 'w')
'''
outt  = open('outt.txt', 'w')
'''

#####################  ESCRITA DO ARQUIVO DE SAIDA ###############################################
##################################################################################################

if caseS == '1' and caseE == '1':
    while cont < 3:
        out0 = '1'+'-'+'10000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+calcEndop+'-' + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + EOP + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        cont += 1

if caseS == '1' and caseE == '2':
    while cont < 3:
        out0 = '1'+'-'+'10000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+calcEndop+'-' + IDLE + IDLE + IDLE + EOP + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        cont += 1

if caseS == '1' and caseE == '3':
    while cont < 3:
        out0 = '1'+'-'+'10000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+calcEndop+'-' + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + EOP + "\n"
        outt.write(out0)
        cont += 1

if caseS == '1' and caseE == '4':
    while cont < 3:
        out0 = '1'+'-'+'10000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+calcEndop+'-' + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + EOP + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        cont += 1

if caseS == '1' and caseE == '5':
    while cont < 3:
        out0 = '1'+'-'+'10000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+calcEndop+'-' + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + EOP + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 +"\n"
        outt.write(out0)
        cont += 1

if caseS == '1' and caseE == '6':
    while cont < 3:
        out0 = '1'+'-'+'10000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+calcEndop+'-' + IDLE + IDLE + IDLE + EOP + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 +"\n"
        outt.write(out0)
        cont += 1

if caseS == '1' and caseE == '7':
    while cont < 3:
        out0 = '1'+'-'+'10000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 +"\n"
        outt.write(out0)
        out0 = '0'+'-'+calcEndop+'-' + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + EOP + "\n"
        outt.write(out0)
        cont += 1

if caseS == '1' and caseE == '8':
    while cont < 3:
        out0 = '1'+'-'+'10000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 +"\n"
        outt.write(out0)
        out0 = '0'+'-'+calcEndop+'-' + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + EOP + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        cont += 1

if caseS == '2' and caseE == '1':
    while cont < 3:
        out0 = '1'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+calcEndop+'-' + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + EOP + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        cont += 1

if caseS == '2' and caseE == '2':
    while cont < 3:
        out0 = '1'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+calcEndop+'-' + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + EOP + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        cont += 1

if caseS == '2' and caseE == '3':
    while cont < 3:
        out0 = '1'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+calcEndop+'-' + IDLE + IDLE + IDLE + EOP + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        cont += 1

if caseS == '2' and caseE == '4':
    while cont < 3:
        out0 = '1'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+calcEndop+'-' + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + EOP + "\n"
        outt.write(out0)
        cont += 1

if caseS == '2' and caseE == '5':
    while cont < 3:
        out0 = '1'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+calcEndop+'-' + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + EOP + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        outt.write(out0)
        cont += 1

if caseS == '2' and caseE == '6':
    while cont < 3:
        out0 = '1'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+calcEndop+'-' + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + EOP + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        outt.write(out0)
        cont += 1

if caseS == '2' and caseE == '7':
    while cont < 3:
        out0 = '1'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+calcEndop+'-' + IDLE + IDLE + IDLE + EOP + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        outt.write(out0)
        cont += 1

if caseS == '2' and caseE == '8':
    while cont < 3:
        out0 = '1'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3  + "\n"
        outt.write(out0)
        out0 = '0'+'-'+calcEndop+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + EOP + "\n"
        outt.write(out0)
        cont += 1

if caseS == '3' and caseE == '1':
    while cont < 3:
        out0 = '1'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+calcEndop+'-' + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + EOP + "\n"
        outt.write(out0)
        cont += 1

if caseS == '3' and caseE == '2':
    while cont < 3:
        out0 = '1'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+calcEndop+'-' + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + EOP + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        cont += 1

if caseS == '3' and caseE == '3':
    while cont < 3:
        out0 = '1'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+calcEndop+'-' + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + EOP + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        cont += 1

if caseS == '3' and caseE == '4':
    while cont < 3:
        out0 = '1'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+calcEndop+'-' + IDLE + IDLE + IDLE + EOP + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        cont += 1

if caseS == '3' and caseE == '5':
    while cont < 3:
        out0 = '1'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+calcEndop+'-' + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE  + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + EOP + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE  + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        outt.write(out0)
        cont += 1

if caseS == '3' and caseE == '6':
    while cont < 3:
        out0 = '1'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+calcEndop+'-' + IDLE + IDLE  + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + EOP + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE  + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        outt.write(out0)
        cont += 1

if caseS == '3' and caseE == '7':
    while cont < 3:
        out0 = '1'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+calcEndop+'-' + IDLE + IDLE  + IDLE + IDLE + IDLE + IDLE + IDLE + EOP + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE  + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        outt.write(out0)
        cont += 1

if caseS == '3' and caseE == '8':
    while cont < 3:
        out0 = '1'+'-'+'10000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+calcEndop+'-' + IDLE + IDLE + IDLE + EOP + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE  + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        outt.write(out0)
        cont += 1

if caseS == '4' and caseE == '1':
    while cont < 3:
        out0 = '1'+'-'+'10000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'10000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+calcEndop+'-' + IDLE + IDLE + IDLE + EOP + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE  + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        outt.write(out0)
        cont += 1
#####################  CASOS MAIS ESPECIAIS ###############################################
##################################################################################################

if caseS == '9' and caseE == '0':
    out0 = '1'+'-'+'10000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
    outt.write(out0)
    out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
    outt.write(out0)
    out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
    outt.write(out0)
    out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
    outt.write(out0)
    out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
    outt.write(out0)
    out0 = '0'+'-'+calcEndop+'-' + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + EOP + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
    outt.write(out0)
    while cont < 3:
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+'00000'+'-' + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        outt.write(out0)
        out0 = '0'+'-'+calcEndop+'-' + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + EOP + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        outt.write(out0)

        cont += 1
################################################################################################################
outt.close()
