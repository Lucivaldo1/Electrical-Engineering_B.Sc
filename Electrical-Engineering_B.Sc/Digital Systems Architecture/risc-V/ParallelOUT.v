module ParallelOUT(
	input[7:0] RegData, Address,
	input EN, clk, rst, //ok
	output reg [7:0] DataOut
);
	always @(posedge clk or negedge rst) begin
    if (!rst) begin
        DataOut <= 8'b0;
    end
    else if (EN == 1 && Address == 8'hFF) begin
        DataOut <= RegData;
    end
end

		
endmodule