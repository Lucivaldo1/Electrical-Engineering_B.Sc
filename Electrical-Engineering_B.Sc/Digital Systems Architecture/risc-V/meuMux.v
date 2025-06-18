module meuMux(
	input[7:0] i0, i1,
	input sel,
	output reg[7:0] out

);
	// se sel igual a 1, out igual a i1. Se sel igual a 0, out igual a 0.
	always @(sel) begin
	
		if (sel == 1)
			out = i1;
		else
			out = i0;
	end
endmodule

module meuMux_TB;

	// sinais
	
	reg [7:0] i0, i1;
	
	reg sel;
	
	wire [7:0] out;
	
	// chamando modulo do mux
	meuMux
	
	meuMux_TB(.i0(i0), .i1(i1), .sel(sel), .out(out));
	
	
	initial 
	begin
	// teste 1
	i0=8'h0F; i1=8'hF0; sel=1'b0; #10;
	// teste 2
	i0=8'h0F; i1=8'hF0; sel=1'b1; #10;
	// teste 3
	i0=8'h0F; i1=8'hFA; sel=1'b1; #10;
	// teste 4
	i0=8'hBF; i1=8'hFA; sel=1'b1; #10;
	end
endmodule
	
/*	
	A = 1010 -> 10
	B = 1011 -> 11
	C = 1100 -> 12
	D = 1101 -> 13
	E = 1110 -> 14
	F = 1111 -> 15
  	
*/
