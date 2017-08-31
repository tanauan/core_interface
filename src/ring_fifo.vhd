library ieee;
  use ieee.std_logic_1164.all;
  use ieee.std_logic_unsigned.all;
  use ieee.numeric_std.all;

entity ring_fifo is
	generic (
		WIDTH  : integer := 256;
    N      : integer := 5;
    DEPTH  : integer := 32 -- where DEPTH = 2^N
	);
	port (
		clk       : in  std_logic;
		rst_n	    : in  std_logic;
    data_in	  : in  std_logic_vector (WIDTH-1 downto 0);
    data_out  : out std_logic_vector (WIDTH-1 downto 0);
    wen       : in  std_logic;
		ren	      : in  std_logic;
		empty	    : out std_logic;
		full	    : out std_logic
	);
end ring_fifo;

architecture behav of ring_fifo is
  type MEM_type is array (DEPTH-1 downto 0) of std_logic_vector(WIDTH-1 downto 0);
  signal mem : MEM_type;

  signal w_ptr : std_logic_vector(N-1 downto 0);
  signal r_ptr : std_logic_vector(N-1 downto 0);

  signal last_op : std_logic; -- 1 - last operation = write / 0 - last operation = read
begin

  sync: process(clk, rst_n)
  begin
    if rst_n = '0' then
      mem   <= (others=>(others=>'0'));
      data_out <= (others=>'0');
      w_ptr <= (others=>'0');
      r_ptr <= (others=>'0');
      last_op <= '0';
    elsif clk'event and clk = '1' then
        if wen = '1' then                 -- Does not check full, will overwrite
          mem(conv_integer(w_ptr)) <= data_in;
          w_ptr <= w_ptr + 1;
          last_op <= '1';
        end if;

        if ren = '1' then               -- Does not check empty, will underwrite
          data_out <= mem(conv_integer(r_ptr));
          r_ptr <= r_ptr + 1;
          last_op <= '0';
        end if;
    end if;
  end process;

  comb: process(w_ptr,r_ptr,last_op)
  begin
    if w_ptr = r_ptr then
      if (last_op = '1') then
        full <= '1';
        empty <= '0';
      else
        full <= '0';
        empty <= '1';
      end if;
    else
      full <= '0';
      empty <= '0';
    end if;
  end process;

end behav;
