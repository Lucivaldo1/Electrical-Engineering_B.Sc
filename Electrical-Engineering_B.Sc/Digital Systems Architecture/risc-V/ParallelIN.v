module ParallelIN(
	input [7:0] MemData, Address,DataIn,
	output reg [7:0] RegData

);

always@(*) begin
	if(Address == 8'hFF)begin
			RegData = DataIn;
	end
	else begin
		RegData = MemData;
	end
	end
endmodule