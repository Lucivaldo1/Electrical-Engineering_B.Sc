module Datamemory(

	input [7:0] A, WD, 
	output reg [7:0] RD,
	input WE, rst, clk
	
);
	integer i;
	//array 2d de memória
	//reg [7:0] memoria [7:0];
	// _ _ _ _ _ _ _ _ -> 2**8
	
	reg [7:0] memoria [255:0]; //8 bits de endereço 

	always@(posedge clk or negedge rst) begin
	
	if(!rst)begin
	for(i=0;i<256;i= i + 1)begin
		memoria[i] <= 8'b0;
		end
	end
	else if (WE)begin
		memoria[A] <= WD [7:0];
	end
	
	end
	
	// leitura
	
	always@(*)begin
	
		RD = memoria[A];
	end
endmodule
