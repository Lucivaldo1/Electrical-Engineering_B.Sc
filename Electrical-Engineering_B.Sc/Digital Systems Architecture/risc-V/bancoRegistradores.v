module RegisterFile(
	input [7:0] wd3,      // determina qual registrador será utilizado
	input [2:0] wa3,      // endereço de escrita     
	input we3,           // enable de escrita     
	input clk,                
	input [2:0] ra1,     // endereço do reg 1      
	input [2:0] ra2,      // endereço do reg2
	input rst,                 
	output reg [7:0] rd1, rd2, x0, x1, x2, x3, x4, x5, x6, x7
);

    
    reg [7:0] registrador [7:0]; 
    
    initial begin
        registrador[0] = 8'b0;
        registrador[1] = 8'b0;
        registrador[2] = 8'b0;
        registrador[3] = 8'b0;
        registrador[4] = 8'b0;
        registrador[5] = 8'b0;
        registrador[6] = 8'b0;
        registrador[7] = 8'b0;
    end
		//escrita
		always @(posedge clk or negedge rst) begin
			if (!rst) begin //botão normalmente fechado, aperta -> recebe 0->reseta de forma sincrona
            registrador[0] = 8'b0;
            registrador[1] = 8'b0;
            registrador[2] = 8'b0;
            registrador[3] = 8'b0;
            registrador[4] = 8'b0;
            registrador[5] = 8'b0;
            registrador[6] = 8'b0;
            registrador[7] = 8'b0;
        end 
			
        else if (we3 == 1/*wa3 && wd3 != 3'b000*/) begin //evita escrever em 0
            registrador[wa3] <= wd3; //passa Sw[7:0] para wa3 ()
				end
    end// end always
	 //leitura
	 /*o valor do registrador de índice ra1 é disponibilizado de forma contínua na saída rd1
	 assim como o registrador de índice ra2 na saída rd2. always@(*)
	 */
	 /*always@(*) begin
	 
	 case(ra1)
		3'b000: rd1 = registrador[0];
		3'b001: rd1 = registrador[1];
		3'b010: rd1 = registrador[2];
		3'b011: rd1 = registrador[3];
		3'b100: rd1 = registrador[4];
		3'b101: rd1 = registrador[5];
		3'b110: rd1 = registrador[6];
		3'b111: rd1 = registrador[7];
		default: rd1 = 8'b00000000;
		endcase
	 end
	 
	 	always@(*) begin
	 
	 case(ra2)
		3'b000: rd2 = registrador[0];
		3'b001: rd2 = registrador[1];
		3'b010: rd2 = registrador[2];
		3'b011: rd2 = registrador[3];
		3'b100: rd2 = registrador[4];
		3'b101: rd2 = registrador[5];
		3'b110: rd2 = registrador[6];
		3'b111: rd2 = registrador[7];
		default: rd2 = 8'b00000000;
		endcase
	 end*/
	
	// para visualização dos registradores no LCD
   	always@(*) begin
			rd1 = registrador[ra1];
			rd2 = registrador[ra2];
			x0 = registrador[0];
			x1 = registrador[1];
			x2 = registrador[2];
			x3 = registrador[3];
			x4 = registrador[4];
			x5 = registrador[5];
			x6 = registrador[6];
			x7 = registrador[7];
	end

endmodule
