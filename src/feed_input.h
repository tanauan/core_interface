#ifndef FEED_INPUT
#define FEED_INPUT

#include "systemc.h"
#include <sstream>
#include <string>
#include <iostream>
#include <fstream>
#include <time.h>

#define PICK_RANDOM_ORDER 0

#define TEST_CASE 3		// Specify the folder to get the files from

SC_MODULE(feed_input) {

  sc_in<sc_logic>   clock;
  sc_in<sc_logic>   reset_n;

  sc_out<sc_lv<64 > > data_out_0;
  sc_out<sc_lv<8 > >  control_out_0;
  sc_out<sc_lv<64 > > data_out_1;
  sc_out<sc_lv<8 > >  control_out_1;
  sc_out<sc_lv<64 > > data_out_2;
  sc_out<sc_lv<8 > >  control_out_2;
  sc_out<sc_lv<64 > > data_out_3;
  sc_out<sc_lv<8 > >  control_out_3;

  ifstream lanes[4];

  std::pair<std::string, std::string> splitHeaderBlock(std::string val) {
      std::string arg;
      std::string::size_type pos = val.find('-');
      if(val.npos != pos) {
          arg = val.substr(pos + 1);
          val = val.substr(0, pos);
      }
      return std::make_pair(val, arg);
  }


  void buffer_lanes() {

    std::pair<std::string, std::string> pr0;
    std::pair<std::string, std::string> pr1;
    std::pair<std::string, std::string> pr2;
    std::pair<std::string, std::string> pr3;

    std::string line0;
    std::string line1;
    std::string line2;
    std::string line3;

    sc_lv<8 >  control_out_0_int;
    sc_lv<64 > data_out_0_int;
    sc_lv<8 >  control_out_1_int;
    sc_lv<64 > data_out_1_int;
    sc_lv<8 >  control_out_2_int;
    sc_lv<64 > data_out_2_int;
    sc_lv<8 >  control_out_3_int;
    sc_lv<64 > data_out_3_int;

    if (reset_n == SC_LOGIC_1) {       // RESET ativo baixo
        if( lanes[0].is_open() ) {
          if( lanes[0] >> line0 ) {
			// parse <control>-<data>
            std::pair<std::string, std::string> pr0 = splitHeaderBlock(line0);
            control_out_0_int = pr0.first.c_str();
            data_out_0_int  = pr0.second.c_str();

            control_out_0 = control_out_0_int;
            data_out_0 = data_out_0_int;

            cout << "[FEED_INPUT 0] Control = " << control_out_0 << " Data = " << data_out_0 << endl;
          }
        } else {
          cout << "[FEED_INPUT 0]FALHOU lanes 0" << endl;
        }

        if( lanes[1].is_open() ) {
          if( lanes[1] >> line1 ) {
            std::pair<std::string, std::string> pr1 = splitHeaderBlock(line1);
            control_out_1_int = pr1.first.c_str();
            data_out_1_int  = pr1.second.c_str();

            control_out_1 = control_out_1_int;
            data_out_1 = data_out_1_int;

            cout << "[FEED_INPUT 1] Control = " << control_out_1 << " Data = " << data_out_1 << endl;
          }
        } else {
          cout << "[FEED_INPUT 1]FALHOU lanes 1" << endl;
        }

        if( lanes[2].is_open() ) {
          if( lanes[2] >> line2 ) {
            std::pair<std::string, std::string> pr2 = splitHeaderBlock(line2);
            control_out_2_int = pr2.first.c_str();
            data_out_2_int  = pr2.second.c_str();

            control_out_2 = control_out_2_int;
            data_out_2 = data_out_2_int;

            cout << "[FEED_INPUT 2] Control = " << control_out_2 << " Data = " << data_out_2 << endl;
          }
        } else {
          cout << "[FEED_INPUT 2]FALHOU lanes 2" << endl;
        }

        if( lanes[3].is_open() ) {
          if( lanes[3] >> line3 ) {
            std::pair<std::string, std::string> pr3 = splitHeaderBlock(line3);
            control_out_3_int = pr3.first.c_str();
            data_out_3_int  = pr3.second.c_str();

            control_out_3 = control_out_3_int;
            data_out_3 = data_out_3_int;

            cout << "[FEED_INPUT 3] Control = " << control_out_3 << " Data = " << data_out_3 << endl;
          }
        } else {
          cout << "[FEED_INPUT 3]FALHOU lanes 3" << endl;
        }
    } else {
	  // Write something invalid during reset
      control_out_0 = "11111111";
      data_out_0  = "0000000000000000000000000000000000000000000000000000000000000000";
      control_out_1 = "11111111";
      data_out_1  = "0000000000000000000000000000000000000000000000000000000000000000";
      control_out_2 = "11111111";
      data_out_2  = "0000000000000000000000000000000000000000000000000000000000000000";
      control_out_3 = "11111111";
      data_out_3  = "0000000000000000000000000000000000000000000000000000000000000000";
    }
  }


  SC_CTOR(feed_input) {

	if(TEST_CASE == 1) {
		lanes[0].open("sc1/dump_mii_rx_0.txt");
	}	else if(TEST_CASE == 2) {
    lanes[0].open("sc2/dump_mii_rx_0.txt");
  } else if(TEST_CASE == 3) {
    lanes[0].open("sc3/dump_mii_rx_0.txt");
  } else {
    lanes[0].open("sc4/dump_mii_rx_0.txt");
  }

  if (lanes[0].is_open()){
    cout << "[FEED_INPUT] File lanes[0].txt opened." << endl;
  } else {
    cout << "[FEED_INPUT] ERROR opening lanes[0].txt" << endl;
  }

	if(TEST_CASE == 1) {
		lanes[1].open("sc1/dump_mii_rx_1.txt");
	} else if(TEST_CASE == 2) {
    lanes[1].open("sc2/dump_mii_rx_1.txt");
  } else if(TEST_CASE == 3) {
    lanes[1].open("sc3/dump_mii_rx_1.txt");
  } else {
    lanes[1].open("sc4/dump_mii_rx_1.txt");
  }

	if (lanes[1].is_open()){
    cout << "[FEED_INPUT] File lanes[1].txt opened." << endl;
  } else {
    cout << "[FEED_INPUT] ERROR opening lanes[1].txt" << endl;
  }

	if(TEST_CASE == 1) {
		lanes[2].open("sc1/dump_mii_rx_2.txt");
	}	else if(TEST_CASE == 2) {
    lanes[2].open("sc2/dump_mii_rx_2.txt");
  } else if(TEST_CASE == 3) {
    lanes[2].open("sc3/dump_mii_rx_2.txt");
  } else {
    lanes[2].open("sc4/dump_mii_rx_3.txt");
  }
  if (lanes[2].is_open()){
    cout << "[FEED_INPUT] File lanes[2].txt opened." << endl;
  } else {
    cout << "[FEED_INPUT] ERROR opening lanes[2].txt" << endl;
  }

	if(TEST_CASE == 1) {
		lanes[3].open("sc1/dump_mii_rx_3.txt");
	}	else if(TEST_CASE == 2) {
    lanes[3].open("sc2/dump_mii_rx_3.txt");
  } else if(TEST_CASE == 3) {
    lanes[3].open("sc3/dump_mii_rx_3.txt");
  } else {
    lanes[3].open("sc4/dump_mii_rx_3.txt");
  }
  if (lanes[3].is_open()){
    cout << "[FEED_INPUT] File lanes[3].txt opened." << endl;
  } else {
    cout << "[FEED_INPUT] ERROR opening lanes[3].txt" << endl;
  }

    SC_METHOD(buffer_lanes);
    dont_initialize();
    sensitive<<clock.pos();
  }

  ~feed_input () {
    cout << "End of simulation!" << endl;
    for(int i=0; i < 4; i++) {
      lanes[i].close();
    }
  }

};
#endif
