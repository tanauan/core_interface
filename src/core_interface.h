#ifndef _SCGENMOD_core_interface_
#define _SCGENMOD_core_interface_

#include "systemc.h"

class core_interface : public sc_foreign_module
{
public:
    sc_in<sc_logic> clk_156;
    sc_in<sc_logic> clk_312;
    sc_in<sc_logic> rst_n;
    sc_in<sc_lv<8> > xgmii_rxc_0;
    sc_in<sc_lv<64> > xgmii_rxd_0;
    sc_in<sc_lv<8> > xgmii_rxc_1;
    sc_in<sc_lv<64> > xgmii_rxd_1;
    sc_in<sc_lv<8> > xgmii_rxc_2;
    sc_in<sc_lv<64> > xgmii_rxd_2;
    sc_in<sc_lv<8> > xgmii_rxc_3;
    sc_in<sc_lv<64> > xgmii_rxd_3;
    sc_out<sc_lv<128> > mac_data;
    sc_out<sc_logic> mac_is_sop;
    sc_out<sc_lv<6> > mac_is_eop;


    core_interface(sc_module_name nm, const char* hdl_name)
     : sc_foreign_module(nm),
       clk_156("clk_156"),
       clk_312("clk_312"),
       rst_n("rst_n"),
       xgmii_rxc_0("xgmii_rxc_0"),
       xgmii_rxd_0("xgmii_rxd_0"),
       xgmii_rxc_1("xgmii_rxc_1"),
       xgmii_rxd_1("xgmii_rxd_1"),
       xgmii_rxc_2("xgmii_rxc_2"),
       xgmii_rxd_2("xgmii_rxd_2"),
       xgmii_rxc_3("xgmii_rxc_3"),
       xgmii_rxd_3("xgmii_rxd_3"),
       mac_data("mac_data"),
       mac_is_sop("mac_is_sop"),
       mac_is_eop("mac_is_eop")
    {
        elaborate_foreign_module(hdl_name);
    }
    ~core_interface()
    {}

};

#endif

