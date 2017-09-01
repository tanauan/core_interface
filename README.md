# core_interface
  This repository was created so we can verify the core_interface module isolated from
the original project (github.com/GuilhermeKorol/40GBE)

  Core_interface will act as a MII interface between the PCS and MAC modules.
  Basically, there are four 10GBE PCS on four XGMII interfaces to only one 40GBE mac.
Core_interface will gather the frame broken into the four lanes and store it into a dual-port
fifo so MAC can consume the frame at double the PCS frequency and bus width. The data stored
will only contain the payload, meaning no preamble, no SFD, and no IPG. The CRC field will be
kept along with data since MAC will check it later.
<pre>
                           __________________________________________
                          |                                          |
PCS_0 M  -------/-------> |                                          |
      I         8         |                                          |
      I  -------/-------> |                                          |
               64         |                                          |
                          |               CORE_INTERFACE             |
PCS_1 M  -------/-------> |                                          |
      I         8         |                                          |
      I  -------/-------> |                                          |-------/----> MAC
               64         |                                          |      128
                          |                                          |
PCS_2 M  -------/-------> |                                          |
      I         8         |                                          |
      I  -------/-------> |                                          |
               64         |                                          |
                          |                                          |
PCS_3 M  -------/-------> |                                          |
      I         8         |                                          |
      I  -------/-------> |                                          |
               64         |                                          |
                          |__________________________________________|

            at 156MHz                                                     at 312MHz
</pre>

## File structure:

|_ modelsim script
|_ modelsim wave files

src/
  |_ all VHDL and SystemC source files

test_cases/
  |_ Python script that generates test cases
  |_ Test cases temp files

teste_mesa/
  |_ Spread-sheet explaining how the shifters and regs work (trace-table)

dump/
  |_ Dump of the output interface

## Usage
1. Set the desired test case in the run.do script by altering the paremeter passed to dump_generator.py
2. Run "do run.do"
