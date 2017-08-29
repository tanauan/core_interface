library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
 
entity fifo_circular is
	Generic (
		constant DATA_WIDTH  : positive := 256;	--largura
		constant FIFO_DEPTH	: positive :=  1280  --profundidade
	);
	Port ( 
		clk      : in  std_logic;
		rst_n	 : in  std_logic;
		write_en : in  std_logic;
		data_in	 : in  std_logic_vector (DATA_WIDTH - 1 downto 0);
		read_en	 : in  std_logic;
		data_out : out std_logic_vector (DATA_WIDTH - 1 downto 0);
		Empty	 : out std_logic;
		Full	 : out std_logic
	);
end fifo_circular;
 
architecture Behavioral of fifo_circular is
 
begin
 
	-- Memory Pointer Process
	fifo_proc : process (clk)
		type FIFO_Memory is array (0 to FIFO_DEPTH - 1) of std_logic_vector (DATA_WIDTH - 1 downto 0);
		variable Memory : FIFO_Memory;
		
		variable Head : natural range 0 to FIFO_DEPTH - 1;	
		variable Tail : natural range 0 to FIFO_DEPTH - 1;	
		
		variable Looped : boolean;
	begin
		if rising_edge(clk) then
			if rst_n = '0' then
				Head := 1;
				Tail := 1;
				
				Looped := false;
				
				Full  <= '1';
				Empty <= '0';
			else
				if (read_en = '1') then
					if ((Looped = true) or (Head /= Tail)) then
						-- Update data output
						data_out <= Memory(Tail);
						
						-- Update Tail pointer as needed
						if (Tail = FIFO_DEPTH - 1) then
							Tail := 0;
							
							Looped := false;
						else
							Tail := Tail + 1;
						end if;
						
						
					end if;
				end if;
				
				if (write_en = '1') then
					if ((Looped = false) or (Head /= Tail)) then
						-- Write Data to Memory
						Memory(Head) := data_in;
						
						-- Increment Head pointer as needed
						if (Head = FIFO_DEPTH - 1) then
							Head := 0;
							
							Looped := true;
						else
							Head := Head + 1;
						end if;
					end if;
				end if;
				
				-- Update Empty and Full flags
				if (Head = Tail) then
					if Looped then
						Full <= '1';
					else
						Empty <= '1';
					end if;
				else
					Empty	<= '0';
					Full	<= '0';
				end if;
			end if;
		end if;
	end process;
		
end Behavioral;