
if [file exists work] {
    vdel -all
}
vlib work

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

##  ARGUMENTO 1 ################
#   case 9 = end lane0L start lane2L
#   case 10 = end lane0H start lane2H
#   case 11 = end lane1L start lane3L
#   case 12 = end lane1H start lane3H
################################

exec python ./test_cases/dump_generator.py 1 7

#########################################################################

vcom -novopt ./src/register.vhd
vcom -novopt ./src/defines.vhd
vcom -novopt ./src/control.vhd
vcom -novopt ./src/mii_shift_register.vhd
vcom -novopt ./src/mii_shifter.vhd
vcom -novopt ./src/ring_fifo.vhd
vcom -novopt ./src/core_interface.vhd

scgenmod core_interface > src/core_interface.h

sccom ./src/feed_input.cpp
sccom ./src/dump_output.cpp

sccom -g ./src/sc_tb_core_interface.cpp
sccom -link -B/usr/bin/

vsim -novopt work.Top -t 1ps

do wave.do
run 1000 ns
