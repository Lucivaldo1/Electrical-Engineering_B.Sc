module ProgramCounter(
	input clk,
	input rst,
	input [7:0] PCin,
	
	output reg [7:0] PC

);
	initial begin
	PC [7:0] = 8'b0;
	end
	
	always@(posedge clk or negedge rst) begin
		
		if(!rst)begin
		PC [7:0] <= 8'b00000000;
		end
		else begin
			PC <= PCin;
		end
	
	end
endmodule