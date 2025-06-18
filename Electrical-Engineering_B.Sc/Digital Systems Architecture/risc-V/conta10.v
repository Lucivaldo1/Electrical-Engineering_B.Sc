module conta10(
		input clock, reset,
		
		output reg [3:0] out
);

	/*while clock^ == True 
		
		if reset == true
			out = 0
		else if out == 9
			out = 0
		else
			out += 1
		
	*/
	always @ (posedge clock) begin 
		if(~reset) begin 
			out = 4'b0000;
	end 
		else begin 
			if (out == 4'b1001)begin
				out = 4'b0000;
				end
				else begin
					out = out + 1;
				end
		end
end 
endmodule