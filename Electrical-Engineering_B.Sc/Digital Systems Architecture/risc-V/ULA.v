module ULA(

	input  [7:0] SrcA, // operando A
	input  [7:0] SrcB, // operando B
	input  [2:0] ULAControl,
	
	output reg [7:0] ULAResult,
	output reg Z //flag
	
);
	
//logica da ULA
	always@(*)	begin
	  case(ULAControl)
			3'b000: ULAResult[7:0] = SrcA[7:0] + SrcB[7:0];
			3'b001: ULAResult[7:0] = SrcA[7:0] + ~SrcB[7:0] + 8'b1;
			3'b010: ULAResult[7:0] = SrcA[7:0] & SrcB[7:0];
			3'b011: ULAResult[7:0] = SrcA[7:0] | SrcB[7:0];
			3'b100: ULAResult[7:0] = SrcA[7:0] ^ SrcB[7:0]; // adição da XOR à ULA
			3'b101: ULAResult[7:0] = (SrcA[7:0] < SrcB[7:0]) ? 1 : 0;
			default: ULAResult[7:0] = 8'b0;
		
		endcase
		Z = (ULAResult == 0) ? 1 : 0; 
		
 	end
endmodule