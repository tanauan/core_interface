f0  = open("dump/output.txt", "r")
f1  = open("test_cases/outt.txt", "r")
i0 = 0
i1 = 0
error = 0

for line0, line1 in zip(f0, f1):
    i0 = i0 + 1
    i1 = i1 + 1
    error = error + 1
    #if line0 == '0-00000-00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n':
        #i0 = i0 + 1
        #i1 = i1 - 1
        #error = error + 1
#    else:
#        if line0 != line1:
#            print "Error: MII_TX and MII_RX are different at line %d e %d!" % (i0, i1)
#            print "MII_TX line: ",line0,"MII_RX line: ",line1
#            print " "
#            error = error + 1;

#if not(error > 0):
    #print "[SCOREBOARD] dump_mii_tx == dump_mii_rx"
#else:
    print "[SCOREBOARD] %d errors founded!" %error
