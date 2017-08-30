library ieee;
  use ieee.std_logic_1164.all;
  use IEEE.std_logic_unsigned.all;
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
    data_in	  : in  std_logic_vector (WIDTH - 1 downto 0);
    data_out  : out std_logic_vector (WIDTH - 1 downto 0);
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

  signal push : std_logic;  -- wen reg
  signal pop  : std_logic;  -- ren reg

  signal last_op : std_logic; -- 1 - last operation = write / 0 - last operation = read
begin

  data_out <= mem(conv_integer(r_ptr)) when pop = '1' else (others=>'0');
  mem(conv_integer(w_ptr)) <= data_in when push = '1' else (others=>'0');
  -- Pode ser em um process, mas geraria reg para todo barramento

  sync: process(clk, rst_n)
  begin
    if rst_n = '0' then
      w_ptr <= (others=>'0');
      r_ptr <= (others=>'0');
      last_op <= '0';
      elsif clk'event and clk = '1' then
        if wen = '1' then                 -- Does not check full, will overwrite
          push <= '1';
          w_ptr <= w_ptr + 1;
          last_op <= '1';
        else
          push <= '0';
        end if;

        if ren = '1' then               -- Does not check empty, will underwrite
          pop <= '1';
          r_ptr <= r_ptr + 1;
          last_op <= '0';
        else
          pop <= '0';
        end if;
    end if;
  end process;

  comb: process(pop,push)
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
