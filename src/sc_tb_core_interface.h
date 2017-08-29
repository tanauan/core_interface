#ifndef SC_TB_CORE_INTERFACE
#define sc_tb_core_interface


#include <systemc.h>
#include <stdio.h>

#include "dump_output.h"
#include "feed_input.h"

// VHDL MODULES
#include "core_interface.h"

SC_MODULE(Top) {
  sc_clock clk_156;
  sc_clock clk_161;

  sc_event reset_deactivation_event;

  sc_signal<sc_logic> iclock156;
  sc_signal<sc_logic> iclock161;
  sc_signal<sc_logic> reset;

  sc_signal<sc_lv<8>  >  xgmii_rxc_0;
  sc_signal<sc_lv<64> >  xgmii_rxd_0;
  sc_signal<sc_lv<8>  >  xgmii_rxc_1;
  sc_signal<sc_lv<64> >  xgmii_rxd_1;
  sc_signal<sc_lv<8>  >  xgmii_rxc_2;
  sc_signal<sc_lv<64> >  xgmii_rxd_2;
  sc_signal<sc_lv<8>  >  xgmii_rxc_3;
  sc_signal<sc_lv<64> >  xgmii_rxd_3;

  sc_signal<sc_lv<128> > mac_data;


  core_interface  * core_interface_inst;
  feed_input * feed_inst;
  dump_output * dump_inst;

  void clock_assign();
  void reset_generator();

  SC_CTOR(Top): clk_156("clk_156", 6.4, SC_NS, 0.5, 0.0, SC_NS, false),
               clk_161("clk_161", 6.2, SC_NS, 0.5, 0.0, SC_NS, false),
               iclock156("iclock156"), iclock161("iclock161"),
			         xgmii_rxc_0("xgmii_rxc_0"), xgmii_rxd_0("xgmii_rxd_0"),
			         xgmii_rxc_1("xgmii_rxc_1"), xgmii_rxd_1("xgmii_rxd_1"),
			         xgmii_rxc_2("xgmii_rxc_2"), xgmii_rxd_2("xgmii_rxd_2"),
			         xgmii_rxc_3("xgmii_rxc_3"), xgmii_rxd_3("xgmii_rxd_3") {

    // Creating instances
    core_interface_inst = new core_interface("core_interface","core_interface");
	  dump_inst = new dump_output("dump_output","dump/output.txt");
	  feed_inst = new feed_input("feed_input");

	  // feed_input connections
	  feed_inst->clock(iclock156);
	  feed_inst->reset_n(reset);
	  feed_inst->data_out_0(xgmii_rxd_0);
    feed_inst->control_out_0(xgmii_rxc_0);
    feed_inst->data_out_1(xgmii_rxd_1);
    feed_inst->control_out_1(xgmii_rxc_1);
    feed_inst->data_out_2(xgmii_rxd_2);
    feed_inst->control_out_2(xgmii_rxc_2);
    feed_inst->data_out_3(xgmii_rxd_3);
    feed_inst->control_out_3(xgmii_rxc_3);

    // core_interface connections
    core_interface_inst->clk_156(iclock156);
    core_interface_inst->clk_312(iclock161);
    core_interface_inst->rst_n(reset);
	  core_interface_inst->xgmii_rxc_0(xgmii_rxc_0);
	  core_interface_inst->xgmii_rxd_0(xgmii_rxd_0);
	  core_interface_inst->xgmii_rxc_1(xgmii_rxc_1);
	  core_interface_inst->xgmii_rxd_1(xgmii_rxd_1);
	  core_interface_inst->xgmii_rxc_2(xgmii_rxc_2);
	  core_interface_inst->xgmii_rxd_2(xgmii_rxd_2);
	  core_interface_inst->xgmii_rxc_3(xgmii_rxc_3);
	  core_interface_inst->xgmii_rxd_3(xgmii_rxd_3);
	  core_interface_inst->mac_data(mac_data);

	  // dump_output connections
	  dump_inst->clock(iclock161);
	  dump_inst->reset_n(reset);
	  dump_inst->mac_data(mac_data);

    SC_METHOD(clock_assign);
    sensitive << clk_156.signal();
    sensitive << clk_161.signal();
    dont_initialize();

    SC_METHOD(reset_generator);
    sensitive << reset_deactivation_event;
  }

  ~Top () {
    delete core_interface_inst;
	delete feed_inst;
	delete dump_inst;
  }

};

inline void Top::clock_assign()
{
  sc_logic clock_tmp156(clk_156.signal().read());
  iclock156.write(clock_tmp156);

  sc_logic clock_tmp161(clk_161.signal().read());
  iclock161.write(clock_tmp161);
}

inline void Top::reset_generator()
{
    static int first = 0;
    if (first == 0)
    {
        first ++;
        reset.write(SC_LOGIC_0);
        reset_deactivation_event.notify(35, SC_NS);

    }
    else{
        first ++;
        reset.write(SC_LOGIC_1);

    }

}

#endif
