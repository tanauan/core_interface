#############################################################################################

import random

cont_idle = 0
cont_data = 0
lane0 = 0
lane1 = 0
lane2 = 0
lane3 = 0
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

import sys
caseS = sys.argv[1]
caseE = sys.argv[2]
dump0 = open('test_cases/dump_mii_rx_0.txt', 'w')
dump1 = open('test_cases/dump_mii_rx_1.txt', 'w')
dump2 = open('test_cases/dump_mii_rx_2.txt', 'w')
dump3 = open('test_cases/dump_mii_rx_3.txt', 'w')
'''
dump0 = open('dump_mii_rx_0.txt', 'w')
dump1 = open('dump_mii_rx_1.txt', 'w')
dump2 = open('dump_mii_rx_2.txt', 'w')
dump3 = open('dump_mii_rx_3.txt', 'w')
'''
#####################  ROTINA DE IDLE INICIAL ###############################################
#############################################################################################

while cont_idle < 2:
    control = '11111111'
    lane0 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
    dump0.write(lane0)

    control = '11111111'
    lane1 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
    dump1.write(lane1)

    control = '11111111'
    lane2 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
    dump2.write(lane2)

    control = '11111111'
    lane3 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
    dump3.write(lane3)
    cont_idle += 1

while cont < 3:
########################### ENTRADA DO START ###################################################
################################################################################################
    if caseS == '1':
        control = '00000001'
        lane0 = control + "-" + PRE + SOP + "\n"
        dump0.write(lane0)

        control = '00000000'
        lane1 = control + "-" + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        dump1.write(lane1)

        control = '00000000'
        lane2 = control + "-" + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        dump2.write(lane2)

        control = '00000000'
        lane3 = control + "-" + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        dump3.write(lane3)

    if caseS == '2':
        control = '00011111'
        lane0 = control + "-" + PREL + SOP + IDLE + IDLE + IDLE + IDLE + "\n"
        dump0.write(lane0)

        control = '00000000'
        lane1 = control + "-" + DATA1 + DATA1 + DATA1 + DATA1 + PREH + "\n"
        dump1.write(lane1)

        control = '00000000'
        lane2 = control + "-" + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        dump2.write(lane2)

        control = '00000000'
        lane3 = control + "-" + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        dump3.write(lane3)

    if caseS == '3':
        control = '11111111'
        lane0 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump0.write(lane0)

        control = '00000001'
        lane1 = control + "-" + PRE + SOP + "\n"
        dump1.write(lane1)

        control = '00000000'
        lane2 = control + "-" + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        dump2.write(lane2)

        control = '00000000'
        lane3 = control + "-" + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        dump3.write(lane3)

    if caseS == '4':
        control = '11111111'
        lane0 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump0.write(lane0)

        control = '00011111'
        lane1 = control + "-" + PREL + SOP + IDLE + IDLE + IDLE + IDLE + "\n"
        dump1.write(lane1)

        control = '00000000'
        lane2 = control + "-" + DATA2 + DATA2 + DATA2 + DATA2 + PREH + "\n"
        dump2.write(lane2)

        control = '00000000'
        lane3 = control + "-" + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        dump3.write(lane3)

    if caseS == '5':
        control = '11111111'
        lane0 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump0.write(lane0)

        control = '11111111'
        lane1 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump1.write(lane1)

        control = '00000001'
        lane2 = control + "-" + PRE + SOP + "\n"
        dump2.write(lane2)

        control = '00000000'
        lane3 = control + "-" + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        dump3.write(lane3)

    if caseS == '6':
        control = '11111111'
        lane0 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump0.write(lane0)

        control = '11111111'
        lane1 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump1.write(lane1)

        control = '00011111'
        lane2 = control + "-" + PREL + SOP + IDLE + IDLE + IDLE + IDLE + "\n"
        dump2.write(lane2)

        control = '00000000'
        lane3 = control + "-" + DATA3 + DATA3 + DATA3 + DATA3 + PREH + "\n"
        dump3.write(lane3)

    if caseS == '7':
        control = '11111111'
        lane0 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump0.write(lane0)

        control = '11111111'
        lane1 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump1.write(lane1)

        control = '11111111'
        lane2 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump2.write(lane2)

        control = '00000001'
        lane3 = control + "-" + PRE + SOP + "\n"
        dump3.write(lane3)

    if caseS == '8':
        control = '11111111'
        lane0 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump0.write(lane0)

        control = '11111111'
        lane1 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump1.write(lane1)

        control = '11111111'
        lane2 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump2.write(lane2)

        control = '00011111'
        lane3 = control + "-" + PREL + SOP + IDLE + IDLE + IDLE + IDLE + "\n"
        dump3.write(lane3)

        control = '00000000'
        lane0 = control + "-" + DATA0 + DATA0 + DATA0 + DATA0 + PREH + "\n"
        dump0.write(lane0)

        control = '00000000'
        lane1 = control + "-" + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        dump1.write(lane1)

        control = '00000000'
        lane2 = control + "-" + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        dump2.write(lane2)

        control = '00000000'
        lane3 = control + "-" + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        dump3.write(lane3)

    if caseS == '9':
        control = '11111111'
        lane0 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + EOP + "\n"
        dump0.write(lane0)

        control = '11111111'
        lane1 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump1.write(lane1)

        control = '00000001'
        lane2 = control + "-" + PRE + SOP + "\n"
        dump2.write(lane2)

        control = '00000000'
        lane3 = control + "-" + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        dump3.write(lane3)

    if caseS == '10':
        control = '11110000'
        lane0 = control + "-" + IDLE + IDLE + IDLE + EOP + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        dump0.write(lane0)

        control = '11111111'
        lane1 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump1.write(lane1)

        control = '00011111'
        lane2 = control + "-" + PREL + SOP + IDLE + IDLE + IDLE + IDLE + "\n"
        dump2.write(lane2)

        control = '00000000'
        lane3 = control + "-" + DATA3 + DATA3 + DATA3 + DATA3 + PREH + "\n"
        dump3.write(lane3)

    if caseS == '11':
        control = '00000000'
        lane0 = control + "-" + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        dump0.write(lane0)

        control = '11111111'
        lane1 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + EOP + "\n"
        dump1.write(lane1)

        control = '11111111'
        lane2 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump2.write(lane2)

        control = '00000001'
        lane3 = control + "-" + PRE + SOP + "\n"
        dump3.write(lane3)

    if caseS == '12':
        control = '00000000'
        lane0 = control + "-" + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        dump0.write(lane0)

        control = '11110000'
        lane1 = control + "-" + IDLE + IDLE + IDLE + EOP + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        dump1.write(lane1)

        control = '11111111'
        lane2 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump2.write(lane2)

        control = '00011111'
        lane3 = control + "-" + PREL + SOP + IDLE + IDLE + IDLE + IDLE + "\n"
        dump3.write(lane3)

        control = '00000000'
        lane0 = control + "-" + DATA0 + DATA0 + DATA0 + DATA0 + PREH + "\n"
        dump0.write(lane0)

        control = '00000000'
        lane1 = control + "-" + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        dump1.write(lane1)

        control = '00000000'
        lane2 = control + "-" + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        dump2.write(lane2)

        control = '00000000'
        lane3 = control + "-" + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        dump3.write(lane3)

    ###################### PREENCHE COM DADOS ########################################################
##################################################################################################
    while cont_data < 5:

        control = '00000000'
        lane0 = control + "-" + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        dump0.write(lane0)

        control = '00000000'
        lane1 = control + "-" + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        dump1.write(lane1)

        control = '00000000'
        lane2 = control + "-" + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        dump2.write(lane2)

        control = '00000000'
        lane3 = control + "-" + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        dump3.write(lane3)
        cont_data += 1

########################### ENTRADA DO END ###################################################
################################################################################################
    if caseE == '1' or caseS == '9' or caseS == '10' or caseS == '11' or caseS == '12':
        control = '11111111'
        lane0 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + EOP + "\n"
        dump0.write(lane0)

        control = '11111111'
        lane1 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump1.write(lane1)

        control = '11111111'
        lane2 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump2.write(lane2)

        control = '11111111'
        lane3 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump3.write(lane3)

    if caseE == '2':
        control = '11110000'
        lane0 = control + "-" + IDLE + IDLE + IDLE + EOP + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        dump0.write(lane0)

        control = '11111111'
        lane1 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump1.write(lane1)

        control = '11111111'
        lane2 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump2.write(lane2)

        control = '11111111'
        lane3 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump3.write(lane3)

    if caseE == '3':
        control = '00000000'
        lane0 = control + "-" + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        dump0.write(lane0)

        control = '11111111'
        lane1 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + EOP + "\n"
        dump1.write(lane1)

        control = '11111111'
        lane2 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump2.write(lane2)

        control = '11111111'
        lane3 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump3.write(lane3)

    if caseE == '4':
        control = '00000000'
        lane0 = control + "-" + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        dump0.write(lane0)

        control = '11110000'
        lane1 = control + "-" + IDLE + IDLE + IDLE + EOP + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        dump1.write(lane1)

        control = '11111111'
        lane2 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump2.write(lane2)

        control = '11111111'
        lane3 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump3.write(lane3)

    if caseE == '5':
        control = '00000000'
        lane0 = control + "-" + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        dump0.write(lane0)

        control = '00000000'
        lane1 = control + "-" + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        dump1.write(lane1)

        control = '11111111'
        lane2 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + EOP + "\n"
        dump2.write(lane2)

        control = '11111111'
        lane3 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump3.write(lane3)

    if caseE == '6':
        control = '00000000'
        lane0 = control + "-" + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        dump0.write(lane0)

        control = '00000000'
        lane1 = control + "-" + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        dump1.write(lane1)

        control = '11110000'
        lane2 = control + "-" + IDLE + IDLE + IDLE + EOP + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        dump2.write(lane2)

        control = '11111111'
        lane3 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
        dump3.write(lane3)

    if caseE == '7':
        control = '00000000'
        lane0 = control + "-" + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        dump0.write(lane0)

        control = '00000000'
        lane1 = control + "-" + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        dump1.write(lane1)

        control = '00000000'
        lane2 = control + "-" + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        dump2.write(lane2)

        control = '11111111'
        lane3 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + EOP + "\n"
        dump3.write(lane3)

    if caseE == '8':
        control = '00000000'
        lane0 = control + "-" + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + DATA0 + "\n"
        dump0.write(lane0)

        control = '00000000'
        lane1 = control + "-" + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + DATA1 + "\n"
        dump1.write(lane1)

        control = '00000000'
        lane2 = control + "-" + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + DATA2 + "\n"
        dump2.write(lane2)

        control = '11110000'
        lane3 = control + "-" + IDLE + IDLE + IDLE + EOP + DATA3 + DATA3 + DATA3 + DATA3 + "\n"
        dump3.write(lane3)

#####################  ROTINA DE IDLE FINAL ###############################################
#############################################################################################
    cont_idle = 0
    while cont_idle < 3:
        if not caseS == '9':
            control = '11111111'
            lane0 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
            dump0.write(lane0)

            control = '11111111'
            lane1 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
            dump1.write(lane1)

            control = '11111111'
            lane2 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
            dump2.write(lane2)

            control = '11111111'
            lane3 = control + "-" + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + IDLE + "\n"
            dump3.write(lane3)
        cont_idle += 1
    cont += 1
    cont_idle = 0
    cont_data = 0

dump0.close()
dump1.close()
dump2.close()
dump3.close()
