onerror {resume}
quietly WaveActivateNextPane {} 0
add wave -noupdate -divider {FEED IN}
add wave -noupdate -expand -group IN /Top/feed_input/clock
add wave -noupdate -expand -group IN /Top/feed_input/reset_n
add wave -noupdate -expand -group IN /Top/feed_input/control_out_0
add wave -noupdate -expand -group IN /Top/feed_input/data_out_0
add wave -noupdate -expand -group IN /Top/feed_input/control_out_1
add wave -noupdate -expand -group IN /Top/feed_input/data_out_1
add wave -noupdate -expand -group IN /Top/feed_input/control_out_2
add wave -noupdate -expand -group IN /Top/feed_input/data_out_2
add wave -noupdate -expand -group IN /Top/feed_input/control_out_3
add wave -noupdate -expand -group IN /Top/feed_input/data_out_3
add wave -noupdate -expand -group IN /Top/feed_input/lanes
add wave -noupdate -divider {MAC INTERFACE}
add wave -noupdate -expand -group {CORE INTERFACE} /Top/core_interface/clk_156
add wave -noupdate -expand -group {CORE INTERFACE} /Top/core_interface/clk_312
add wave -noupdate -expand -group {CORE INTERFACE} /Top/core_interface/rst_n
add wave -noupdate -expand -group {CORE INTERFACE} -radix hexadecimal /Top/core_interface/xgmii_rxc_0
add wave -noupdate -expand -group {CORE INTERFACE} -radix hexadecimal /Top/core_interface/xgmii_rxd_0
add wave -noupdate -expand -group {CORE INTERFACE} -radix hexadecimal /Top/core_interface/xgmii_rxc_1
add wave -noupdate -expand -group {CORE INTERFACE} -radix hexadecimal /Top/core_interface/xgmii_rxd_1
add wave -noupdate -expand -group {CORE INTERFACE} -radix hexadecimal /Top/core_interface/xgmii_rxc_2
add wave -noupdate -expand -group {CORE INTERFACE} -radix hexadecimal /Top/core_interface/xgmii_rxd_2
add wave -noupdate -expand -group {CORE INTERFACE} -radix hexadecimal /Top/core_interface/xgmii_rxc_3
add wave -noupdate -expand -group {CORE INTERFACE} -radix hexadecimal /Top/core_interface/xgmii_rxd_3
add wave -noupdate -expand -group {CORE INTERFACE} -radix hexadecimal /Top/core_interface/mac_data
add wave -noupdate -expand -group {CORE INTERFACE} -radix hexadecimal /Top/core_interface/ctrl_mux_delay
add wave -noupdate -expand -group {CORE INTERFACE} -radix hexadecimal /Top/core_interface/ctrl_shift_reg
add wave -noupdate -expand -group {CORE INTERFACE} /Top/core_interface/shift_reg_out_0
add wave -noupdate -expand -group {CORE INTERFACE} /Top/core_interface/shift_reg_out_1
add wave -noupdate -expand -group {CORE INTERFACE} /Top/core_interface/shifter_out
add wave -noupdate -expand -group CONTROLLER /Top/core_interface/controller/clk
add wave -noupdate -expand -group CONTROLLER /Top/core_interface/controller/rst_n
add wave -noupdate -expand -group CONTROLLER -radix hexadecimal /Top/core_interface/controller/xgmii_rxc_0
add wave -noupdate -expand -group CONTROLLER -radix hexadecimal /Top/core_interface/controller/xgmii_rxd_0
add wave -noupdate -expand -group CONTROLLER -radix hexadecimal /Top/core_interface/controller/xgmii_rxc_1
add wave -noupdate -expand -group CONTROLLER -radix hexadecimal /Top/core_interface/controller/xgmii_rxd_1
add wave -noupdate -expand -group CONTROLLER -radix hexadecimal /Top/core_interface/controller/xgmii_rxc_2
add wave -noupdate -expand -group CONTROLLER -radix hexadecimal /Top/core_interface/controller/xgmii_rxd_2
add wave -noupdate -expand -group CONTROLLER -radix hexadecimal /Top/core_interface/controller/xgmii_rxc_3
add wave -noupdate -expand -group CONTROLLER -radix hexadecimal /Top/core_interface/controller/xgmii_rxd_3
add wave -noupdate -expand -group CONTROLLER -radix binary /Top/core_interface/controller/ctrl_delay
add wave -noupdate -expand -group CONTROLLER -radix binary /Top/core_interface/controller/shift_out
add wave -noupdate -expand -group CONTROLLER /Top/core_interface/controller/wen_fifo
add wave -noupdate -expand -group CONTROLLER -radix binary /Top/core_interface/controller/sop_location
add wave -noupdate -expand -group CONTROLLER -radix binary /Top/core_interface/controller/eop_location
add wave -noupdate -expand -group CONTROLLER -radix binary /Top/core_interface/controller/shift_calc
add wave -noupdate -expand -group CONTROLLER -radix binary /Top/core_interface/controller/shift_out_int
add wave -noupdate -expand -group CONTROLLER -radix binary /Top/core_interface/controller/shift_out_reg
add wave -noupdate -expand -group CONTROLLER -radix binary /Top/core_interface/controller/shift_out_reg_reg
add wave -noupdate -expand -group CONTROLLER /Top/core_interface/controller/wen_fifo_reg
add wave -noupdate -expand -group CONTROLLER /Top/core_interface/controller/wen_fifo_reg_reg
add wave -noupdate -expand -group {SHIFT REGISTER} /Top/core_interface/shift_reg/clk
add wave -noupdate -expand -group {SHIFT REGISTER} /Top/core_interface/shift_reg/rst_n
add wave -noupdate -expand -group {SHIFT REGISTER} -radix hexadecimal /Top/core_interface/shift_reg/xgmii_rxc_0
add wave -noupdate -expand -group {SHIFT REGISTER} -radix hexadecimal /Top/core_interface/shift_reg/xgmii_rxd_0
add wave -noupdate -expand -group {SHIFT REGISTER} -radix hexadecimal /Top/core_interface/shift_reg/xgmii_rxc_1
add wave -noupdate -expand -group {SHIFT REGISTER} -radix hexadecimal /Top/core_interface/shift_reg/xgmii_rxd_1
add wave -noupdate -expand -group {SHIFT REGISTER} -radix hexadecimal /Top/core_interface/shift_reg/xgmii_rxc_2
add wave -noupdate -expand -group {SHIFT REGISTER} -radix hexadecimal /Top/core_interface/shift_reg/xgmii_rxd_2
add wave -noupdate -expand -group {SHIFT REGISTER} -radix hexadecimal /Top/core_interface/shift_reg/xgmii_rxc_3
add wave -noupdate -expand -group {SHIFT REGISTER} -radix hexadecimal /Top/core_interface/shift_reg/xgmii_rxd_3
add wave -noupdate -expand -group {SHIFT REGISTER} -radix binary /Top/core_interface/shift_reg/ctrl
add wave -noupdate -expand -group {SHIFT REGISTER} -radix hexadecimal /Top/core_interface/shift_reg/reg_current_D
add wave -noupdate -expand -group {SHIFT REGISTER} -radix hexadecimal /Top/core_interface/shift_reg/reg_current_Q
add wave -noupdate -expand -group {SHIFT REGISTER} -radix hexadecimal /Top/core_interface/shift_reg/reg_previous_Q
add wave -noupdate -expand -group {SHIFT REGISTER} -radix hexadecimal /Top/core_interface/shift_reg/reg_delay_Q
add wave -noupdate -expand -group {SHIFT REGISTER} -radix hexadecimal /Top/core_interface/shift_reg/out_0
add wave -noupdate -expand -group {SHIFT REGISTER} -radix hexadecimal /Top/core_interface/shift_reg/out_1
add wave -noupdate -expand -group SHIFTER /Top/core_interface/shifter/clk
add wave -noupdate -expand -group SHIFTER /Top/core_interface/shifter/rst_n
add wave -noupdate -expand -group SHIFTER -radix hexadecimal /Top/core_interface/shifter/in_0
add wave -noupdate -expand -group SHIFTER -radix hexadecimal /Top/core_interface/shifter/in_1
add wave -noupdate -expand -group SHIFTER -radix binary /Top/core_interface/shifter/ctrl_reg_shift
add wave -noupdate -expand -group SHIFTER -radix hexadecimal /Top/core_interface/shifter/out_data
add wave -noupdate -expand -group FIFO /Top/core_interface/fifo/clk
add wave -noupdate -expand -group FIFO /Top/core_interface/fifo/rst_n
add wave -noupdate -expand -group FIFO -radix hexadecimal /Top/core_interface/fifo/write_en
add wave -noupdate -expand -group FIFO -radix hexadecimal /Top/core_interface/fifo/data_in
add wave -noupdate -expand -group FIFO -radix hexadecimal /Top/core_interface/fifo/read_en
add wave -noupdate -expand -group FIFO -radix hexadecimal /Top/core_interface/fifo/data_out
add wave -noupdate -expand -group FIFO -radix hexadecimal /Top/core_interface/fifo/Empty
add wave -noupdate -expand -group FIFO -radix hexadecimal /Top/core_interface/fifo/Full
add wave -noupdate -divider {DUMP OUT}
add wave -noupdate -group OUT /Top/dump_output/clock
add wave -noupdate -group OUT /Top/dump_output/reset_n
add wave -noupdate -group OUT /Top/dump_output/mac_data
add wave -noupdate -group OUT /Top/dump_output/file_name
add wave -noupdate -group OUT /Top/dump_output/dump_file
TreeUpdate [SetDefaultTree]
WaveRestoreCursors {{Cursor 1} {315590 ps} 0}
quietly wave cursor active 1
configure wave -namecolwidth 376
configure wave -valuecolwidth 243
configure wave -justifyvalue left
configure wave -signalnamewidth 0
configure wave -snapdistance 10
configure wave -datasetprefix 0
configure wave -rowmargin 4
configure wave -childrowmargin 2
configure wave -gridoffset 0
configure wave -gridperiod 1
configure wave -griddelta 40
configure wave -timeline 0
configure wave -timelineunits ns
update
WaveRestoreZoom {284907 ps} {329716 ps}
