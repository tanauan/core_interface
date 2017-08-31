#############################################################################################
cont_idle=0
cont_data=0
lane0=0
lane1=0
lane2=0
lane3=0
control = '0'
case =3
n=3


import sys
case = sys.argv[1]

#   case 1 = start lane0H
#   case 2 = start lane0L
#   case 3 = start lane1H
#   case 4 = start lane1L
#   case 5 = start lane2H
#   case 6 = start lane2L
#   case 7 = start lane3H
#   case 8 = start lane3L

SOP =  '11111011' #0xFB  control = 1
EOP =  '11111101' #0xFD  control = 1
PRE =  '10101010101010101010101010101010101010101010101010101011' #0xaaaaaaaaaaaaa8 control = 1111111
DATA = '11001100' #0xCC control = 0
IDLE = '00000111' #0x07 control = 1

dump0 = open('test_cases/dump_mii_rx_0.txt', 'w')
dump1 = open('test_cases/dump_mii_rx_1.txt', 'w')
dump2 = open('test_cases/dump_mii_rx_2.txt', 'w')
dump3 = open('test_cases/dump_mii_rx_3.txt', 'w')

#####################  ROTINA DE IDLE INICIAL ###############################################
#############################################################################################

while   (cont_idle <= 2):

    control = '11111111'
    lane0 = control+"-"+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+"\n"
    dump0.write(lane0)

    control = '11111111'
    lane1 = control+"-"+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+"\n"
    dump1.write(lane1)

    control = '11111111'
    lane2 = control+"-"+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+"\n"
    dump2.write(lane2)

    control = '11111111'
    lane3 = control+"-"+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+"\n"
    dump3.write(lane3)
    cont_idle=cont_idle+1


########################### ENTRADA DO START ###################################################
################################################################################################
if (case == '1'):
    control = '11111111'
    lane0 = control+"-"+SOP+PRE+"\n"
    dump0.write(lane0)

    control = '00000000'
    lane1 = control+"-"+DATA+DATA+DATA+DATA+DATA+DATA+DATA+DATA+"\n"
    dump1.write(lane1)

    control = '00000000'
    lane2 = control+"-"+DATA+DATA+DATA+DATA+DATA+DATA+DATA+DATA+"\n"
    dump2.write(lane2)

    control = '00000000'
    lane3 = control+"-"+DATA+DATA+DATA+DATA+DATA+DATA+DATA+DATA+"\n"
    dump3.write(lane3)

if(case == '3'):
    control = '11111111'
    lane0 = control+"-"+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+"\n"
    dump0.write(lane0)

    control = '11111111'
    lane1 = control + "-" + SOP + PRE + "\n"
    dump1.write(lane1)

    control = '11111111'
    lane2 = control+"-"+DATA+DATA+DATA+DATA+DATA+DATA+DATA+DATA+"\n"
    dump2.write(lane2)

    control = '11111111'
    lane3 = control+"-"+DATA+DATA+DATA+DATA+DATA+DATA+DATA+DATA+"\n"
    dump3.write(lane3)

if(case == '5'):
    control = '11111111'
    lane0 = control+"-"+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+"\n"
    dump0.write(lane0)

    control = '11111111'
    lane1 = control+"-"+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+"\n"
    dump1.write(lane1)

    control = '11111111'
    lane2 = control + "-" + SOP + PRE + "\n"
    dump2.write(lane2)

    control = '00000000'
    lane3 = control+"-"+DATA+DATA+DATA+DATA+DATA+DATA+DATA+DATA+"\n"
    dump3.write(lane3)

if(case == '7'):
    control = '11111111'
    lane0 = control+"-"+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+"\n"
    dump0.write(lane0)

    control = '11111111'
    lane1 = control+"-"+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+"\n"
    dump1.write(lane1)

    control = '11111111'
    lane2 = control+"-"+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+"\n"
    dump2.write(lane2)

    control = '11111111'
    lane3 = control + "-" + SOP + PRE + "\n"
    dump3.write(lane3)



###################### PREENCHE COM DADOS ########################################################
##################################################################################################
while   (cont_data <= 5):

    control = '00000000'
    lane0 = control+"-"+DATA+DATA+DATA+DATA+DATA+DATA+DATA+DATA+"\n"
    dump0.write(lane0)

    control = '00000000'
    lane1 = control+"-"+DATA+DATA+DATA+DATA+DATA+DATA+DATA+DATA+"\n"
    dump1.write(lane1)

    control = '00000000'
    lane2 = control+"-"+DATA+DATA+DATA+DATA+DATA+DATA+DATA+DATA+"\n"
    dump2.write(lane2)

    control = '00000000'
    lane3 = control+"-"+DATA+DATA+DATA+DATA+DATA+DATA+DATA+DATA+"\n"
    dump3.write(lane3)
    cont_data=cont_data+1


########################### ENTRADA DO END ###################################################
################################################################################################
if(case == '1'):
    control = '00000000'
    lane0 = control+"-"+DATA+DATA+DATA+DATA+DATA+DATA+DATA+DATA+"\n"
    dump0.write(lane0)

    control = '00000000'
    lane1 = control+"-"+DATA+DATA+DATA+DATA+DATA+DATA+DATA+DATA+"\n"
    dump1.write(lane1)

    control = '00000000'
    lane2 = control+"-"+DATA+DATA+DATA+DATA+DATA+DATA+DATA+DATA+"\n"
    dump2.write(lane2)

    control = '00000001'
    lane3 = control+"-"+DATA+DATA+DATA+DATA+DATA+DATA+DATA+EOP+"\n"
    dump3.write(lane3)

if(case== '3'):
    control = '00000000'
    lane0 = control + "-" + DATA + DATA + DATA + DATA + DATA + DATA + DATA + DATA + "\n"
    dump0.write(lane0)

    control = '00000000'
    lane1 = control + "-" + DATA + DATA + DATA + DATA + DATA + DATA + DATA + DATA + "\n"
    dump1.write(lane1)

    control = '00000000'
    lane2 = control + "-" + DATA + DATA + DATA + DATA + DATA + DATA + DATA + DATA + "\n"
    dump2.write(lane2)

    control = '00000001'
    lane3 = control + "-" + DATA + DATA + DATA + DATA + DATA + DATA + DATA + EOP + "\n"
    dump3.write(lane3)

#####################  ROTINA DE IDLE INICIAL ###############################################
#############################################################################################
cont_idle = 0
while   (cont_idle <= 8):

    control = '11111111'
    lane0 = control+"-"+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+"\n"
    dump0.write(lane0)

    control = '11111111'
    lane1 = control+"-"+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+"\n"
    dump1.write(lane1)

    control = '11111111'
    lane2 = control+"-"+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+"\n"
    dump2.write(lane2)

    control = '11111111'
    lane3 = control+"-"+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+IDLE+"\n"
    dump3.write(lane3)
    cont_idle=cont_idle+1

dump0.close()
dump1.close()
dump2.close()
dump3.close()
