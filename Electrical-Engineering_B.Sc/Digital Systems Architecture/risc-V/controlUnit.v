// control unit antiga
module controlUnit(
	input [6:0] Op,
	input [2:0] Funct3,
	input [6:0] Funct7,
	
	output reg [2:0] ULAControl,
	output reg ULASrc,
	output reg RegWrite, MemWrite, ResultSrc, Branch,
	output reg [1:0] ImmSrc
);

	always@(*)begin
		
		// todas as operaçoes menos sub e addi
		if (Op == 7'b0110011)begin
		RegWrite = 1;
		ULASrc = 0;
		ImmSrc = 0;
		ULASrc = 0;
		MemWrite = 0;
		ResultSrc = 0;
		Branch = 0;
		case(Funct7)
			7'b0000000: begin case(Funct3)
				3'b000: ULAControl = 3'b000;
				3'b111: ULAControl = 3'b010;
				3'b110: ULAControl = 3'b011;
				3'b010: ULAControl = 3'b101;
				3'b100: ULAControl = 3'b100; //xor
				default: ULAControl = 3'b000;
			endcase
			end
			//sub
			7'b0100000: if(Funct3 == 3'b000) begin
					ULAControl = 3'b001;
					RegWrite = 1;
					ULASrc = 0;
					ImmSrc = 0;
					ULASrc = 0;
					MemWrite = 0;
					ResultSrc = 0;
					Branch = 0;
				end
			default: ULAControl = 3'b001;
		endcase
		end
		//addi
		else if (Op == 7'b0010011)begin
			RegWrite = 1;
			ULAControl = 3'b000;
			ULASrc = 1;
			ImmSrc = 0;
			ULASrc = 1;
			ULAControl = 3'b000;
			MemWrite = 0;
			ResultSrc = 0;
			Branch = 0;
		end
		//lb
		else if (Op == 7'b0000011)begin
			RegWrite = 1;
			ImmSrc = 0;
			ULASrc = 1;
			ULAControl = 3'b000;
			MemWrite = 0;
			ResultSrc = 1;
			Branch = 0;
		end
		//sb
		else if (Op == 7'b0100011)begin 
			RegWrite = 0;
			ImmSrc = 1;
			ULASrc = 1;
			ULAControl = 3'b000;
			MemWrite = 1;
			ResultSrc = 0; 
			Branch = 0;
		end
		//beq
		else if (Op == 7'b1100011)begin 
			RegWrite = 0;
			ImmSrc = 2'b10;
			ULASrc = 0;
			ULAControl = 3'b001;
			MemWrite = 0;
			Branch = 1;
			ResultSrc = 0; 
		end
	end
endmodule