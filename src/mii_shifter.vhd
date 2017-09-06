library ieee;
  use ieee.std_logic_1164.all;

entity mii_shifter is
  port(
  -- INPUTS
      clk             : in std_logic;
      rst_n           : in std_logic;
      in_1            : in std_logic_vector(255 downto 0);
      in_0            : in std_logic_vector(255 downto 0);

  --CTRL
      ctrl_reg_shift  : in std_logic_vector(2 downto 0);

  --OUTPUTS
      out_data        : out std_logic_vector(255 downto 0)
      );
end entity;

architecture behav_mii_shifter of mii_shifter is

  begin

    out_data <= in_1(255 downto 0)                          when ctrl_reg_shift = "000" else
                in_0( 31 downto 0)  & in_1(255 downto  32)  when ctrl_reg_shift = "001" else

                in_0( 63 downto 0)  & in_1(255 downto  64)  when ctrl_reg_shift = "010" else
                in_0( 95 downto 0)  & in_1(255 downto  96)  when ctrl_reg_shift = "011" else

                in_0( 127 downto 0) & in_1(255 downto 128) when ctrl_reg_shift = "100" else
                in_0(  95 downto 0) & in_1(255 downto 96)  when ctrl_reg_shift = "101" else

                in_0( 63 downto 0)  & in_1(255 downto 64)  when ctrl_reg_shift = "110" else
                in_0( 31 downto 0)  & in_1(255 downto 32)  when ctrl_reg_shift = "111";

  end behav_mii_shifter;
