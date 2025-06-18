module InstructionMemory(
	input [7:0] A,
	output reg [31:0] RD

);

always@(*)begin
	case(A)
		8'h00: RD = 32'h00100193;
		8'h04: RD = 32'h0ff00083;
		8'h08: RD = 32'h0011f133;
		8'h0C: RD = 32'h003122b3;
		8'h10: RD = 32'h0e500fa3;
		8'h14: RD = 32'hfe0008e3;
	
	   default: RD = 32'h0;
		/*
		8'h00: RD = 32'h0ff00083;
		8'h04: RD = 32'h0e100fa3;
		8'h08: RD = 32'hfe000ce3;
		//teste par ou impar
		addi x3, x0, 1 #x3 = 1
		init:
		lb x1, 0xFF(x0) #x1 = parallel in
		and x2,x3,x1 # x2 = 1 and entrada
		slt x5,x2,x3 # se x2<x3, x5 = 1 (par)
		beq x0, x0, init #j init
		8'h00: RD = 32'h00100193;
		8'h04: RD = 32'h0ff00083;
		8'h08: RD = 32'h0011f133;
		8'h0C: RD = 32'h003122b3;
		8'h10: RD = 32'hfe0008e3;;
		*/
		/*
		8'h04: RD = 32'h00900113;
		8'h08: RD = 32'h00208133;
		8'h0C: RD = 32'h0020f1b3;
		8'h10: RD = 32'h0020e233;
		8'h14: RD = 32'h0041a2b3;
		8'h18: RD = 32'h40520333;
		default: RD = 32'h00000000;
		
		//assembler risc V online utilizado: https://riscvasm.lucasteske.dev/#
		8'h00: RD = 32'h0ab00093;
		8'h04: RD = 32'h00100523;
		8'h08: RD = 32'h00a00103;
		8'h0C: RD = 32'h002005a3;
		8'h10: RD = 32'h00b00183;
		8'h14: RD = 32'h00300623;
		8'h18: RD = 32'h00c00203;
		default: RD = 32'h00000000;
		
		//sprint 7
		8'h00: RD = 32'h00700093;
		8'h04: RD = 32'h00300193;
		8'h08: RD = 32'hfff00113;
		8'h0C: RD = 32'h00110113;
		8'h10: RD = 32'h003123b3;
		8'h14: RD = 32'hfe208ae3;
		8'h18: RD = 32'hfe000ae3;
		
		*/
		endcase
		
end
endmodule