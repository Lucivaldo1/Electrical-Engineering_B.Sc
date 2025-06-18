	module divisorFrequencia (
    input wire clockOriginal,         
    output reg clock1Hz 
);
    reg [24:0] contador; 
	 
	 initial begin
	 contador = 0;
	 end
	
    always @(posedge clockOriginal) begin       
          if (contador == 4999999) begin
               contador = 0;
               clock1Hz = ~clock1Hz;
            end 
			 else begin
                contador = contador + 1;
          end
    end
endmodule
