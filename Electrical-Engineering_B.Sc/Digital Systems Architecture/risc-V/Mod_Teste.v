`default_nettype none //Comando para desabilitar declaração automática de wires
module Mod_Teste (
//Clocks
input CLOCK_27, CLOCK_50,
//Chaves e Botoes
input [3:0] KEY,
input [17:0] SW,
//Displays de 7 seg e LEDs
output [0:6] HEX0, HEX1, HEX2, HEX3, HEX4, HEX5, HEX6, HEX7,
output [8:0] LEDG,
output [17:0] LEDR,
//Serial
output UART_TXD,
input UART_RXD,
inout [7:0] LCD_DATA,
output LCD_ON, LCD_BLON, LCD_RW, LCD_EN, LCD_RS,
//GPIO
inout [35:0] GPIO_0, GPIO_1
);
assign GPIO_1 = 36'hzzzzzzzzz;
assign GPIO_0 = 36'hzzzzzzzzz;
assign LCD_ON = 1'b1;
assign LCD_BLON = 1'b1;
wire [7:0] w_d0x0, w_d0x1, w_d0x2, w_d0x3, w_d0x4, w_d0x5,
w_d1x0, w_d1x1, w_d1x2, w_d1x3, w_d1x4, w_d1x5;
LCD_TEST MyLCD (
.iCLK ( CLOCK_50 ),
.iRST_N ( KEY[0] ),
.d0x0(w_d0x0),.d0x1(w_d0x1),.d0x2(w_d0x2),.d0x3(w_d0x3),.d0x4(w_d0x4),.d0x5(w_d0x5),
.d1x0(w_d1x0),.d1x1(w_d1x1),.d1x2(w_d1x2),.d1x3(w_d1x3),.d1x4(w_d1x4),.d1x5(w_d1x5),
.LCD_DATA( LCD_DATA ),
.LCD_RW ( LCD_RW ),
.LCD_EN ( LCD_EN ),
.LCD_RS ( LCD_RS )
);
//---------- modifique a partir daqui --------

// --------- declarações ---------------//
/*
//assign LEDG[0] = KEY[1];

wire clock1Hz; //saida do divisor de frequência

wire [3:0] out; 

wire [7:0] outMux;

//assign LEDG[0] = clock1Hz;

//assign H0EX0 = SW[6:0];



// -=-=-=-=-=-=-= atividade 1 -=-=-=-=-=-= //

meuMux(.i0(SW[7:0]), .i1(SW[15:8]), .sel(SW[17]), .out(LEDR[7:0]));

// -=-=-=-=-=-=-= atividade 2 -=-=-=-=-=-= //

decoder(.i0(SW[11:8]), .out(HEX3[0:6]));

divisorFrequencia(.clockOriginal(CLOCK_50), .clock1Hz(clock1Hz));

//conta10(.clock(clock1Hz), .reset(KEY[1]), .out(out[3:0])); tirar comentario para mostrar contador

//liga a saída do contador na entrada do decodificador
decoder(.i0(out[3:0]), .out(HEX4[0:6]));

// sprint 3
RegisterFile r1(.wd3(SW[7:0]), 
.wa3(SW[16:14]), 
.we3(SW[17]), 
.clk(KEY[1]),
.ra1(SW[13:11]), 
.ra2(SW[10:8]), 
.rst(KEY[2]), 
.rd1(w_d0x0[7:0]), 
.rd2(w_d0x1[7:0]));

assign LEDG[8] = ~KEY[1];

decoder (.i0(SW[3:0]), .out(HEX0[0:6]));

decoder(.i0(SW[7:4]), .out(HEX1[0:6]));



// sprint 4

//fios ligados na ULA

wire [7:0] w_rd1srcA;

wire [7:0] w_srcB;

// saida do registrador

wire [7:0] w_rd2;

// saida da ULA

wire [7:0] w_ULAResultWd3;

//ligacoes no LCD:

assign w_d0x0 = w_rd1srcA;

assign w_d1x0 = w_rd2;

assign w_d1x1 = w_srcB;

assign w_d0x4 = w_ULAResultWd3;

assign LEDG[8] = ~KEY[1];

decoder (.i0(SW[3:0]), .out(HEX0[0:6]));

decoder(.i0(SW[7:4]), .out(HEX1[0:6]));

RegisterFile r2(.wd3(SW[7:0]), //ok
.wa3(SW[16:14]), //ok
.we3(1'b1), //ok 
.clk(KEY[1]),//ok
.ra1(SW[13:11]), 
.ra2(3'b010), 
.rst(KEY[2]), 
.rd1(w_rd1srcA),//ligar na entrada srcA da ULA 
.rd2(w_rd2)); // ligar no mux

meuMux(.i0(w_rd2), .i1(8'h07), .sel(SW[17]), .out(w_srcB));

ULA(.srcA(w_rd1srcA), 
.srcB(w_srcB), 
.Z(LEDG[0]), 
.ulaControl(SW[10:8]), 
.ulaResult(w_ULAResultWd3) );

TESTES NA PLACA: 
testes1 = ok

6_b = 110
3_b = 011
sel(mux) = 0
soma = 9
sub = 3
and = 2
or = 7
slt= 0


7_b = 111
sel(mux) = 1
soma = 13 = D
sub = -1 -> 00000001 -> 11111110 + 1 -> 11111111 = FF
and = 110 -> 6
or = 111 = 7
slt = 1

// sprint 5

// fios:

wire w_ULASrc, w_RegWrite;

wire [2:0] w_ULAControl;

wire [7:0] w_PCp4, w_PC, w_rd1SrcA, w_rd2, w_SrcB, w_ULAResultWd3;

wire [31:0] w_Inst;

//assign's

assign LEDR[2:0] = w_ULAControl[2:0];

assign LEDR[3] = w_ULASrc;

assign LEDR[4] = w_RegWrite;

assign LEDG[8] = ~KEY[1];
//assigns LCD
assign w_d0x4 = w_PC;

assign w_d0x5 = w_rd1SrcA;

assign w_d1x5 = w_SrcB;

//assign w_d1x4 = w_rd2;

//assign w_d0x3 = w_ULAResultWd3;



ProgramCounter(.clk(KEY[1]), .rst(KEY[2]),
.PC(w_PC), 
.PCin(w_PCp4));

InstructionMemory(.A(w_PC[7:0]), .RD(w_Inst[31:0]));

ULA adder4(.SrcA(w_PC), .SrcB(3'h4), 
.ULAControl(3'b000), .ULAResult(w_PCp4));

RegisterFile (.wd3(w_ULAResultWd3),
.wa3(w_Inst[11:7]), 
.we3(w_RegWrite), 
.clk(KEY[1]),
.ra1(w_Inst[19:15]), 
.ra2(w_Inst[24:20]), 
.rst(KEY[2]), 
.rd1(w_rd1SrcA),
.rd2(w_rd2),
.x0(w_d0x0), 
.x1(w_d0x1), 
.x2(w_d0x2), 
.x3(w_d0x3), 
.x4(w_d1x0),
.x5(w_d1x1), 
.x6(w_d1x2), 
.x7(w_d1x3)
);


meuMux(.i0(w_rd2),.i1(w_Inst[31:20]), 
.sel(w_ULASrc), .out(w_SrcB));

ULA(.SrcA(w_rd1SrcA), .SrcB(w_SrcB), //.SrcA(w_rd1SrcA), .SrcB(w_SrcB),
.ULAControl(w_ULAControl[2:0]), 
.ULAResult(w_ULAResultWd3));

decoder(.i0(w_Inst[3:0]),   .out(HEX0[0:6]));
decoder(.i0(w_Inst[7:4]),   .out(HEX1[0:6]));
decoder(.i0(w_Inst[11:8]),  .out(HEX2[0:6]));
decoder(.i0(w_Inst[15:12]), .out(HEX3[0:6]));
decoder(.i0(w_Inst[19:16]), .out(HEX4[0:6]));
decoder(.i0(w_Inst[23:20]), .out(HEX5[0:6]));
decoder(.i0(w_Inst[27:24]), .out(HEX6[0:6]));
decoder(.i0(w_Inst[31:28]), .out(HEX7[0:6]));

controlUnit(.Op(w_Inst[6:0]), 
.Funct3(w_Inst[14:12]), .Funct7(w_Inst[31:25]), 
.ULAControl(w_ULAControl[2:0]), 
.ULASrc(w_ULASrc), .RegWrite(w_RegWrite));



//sprint 6 


// fios durante a sprint 5

wire w_ULASrc, w_RegWrite;

wire [2:0] w_ULAControl;

wire [7:0] w_PCp4, w_PC, w_rd1SrcA, w_rd2, w_SrcB, w_ULAResult; //apenas mudei w_ULAResultWd3 para w_ULAResult

wire [31:0] w_Inst;

// fios adicionados na sprint 6 :

wire w_ImmSrc, w_MemWrite, w_ResultSrc, clock1Hz;
   
wire [7:0] w_Wd3, w_Imm, w_RData;


//assigns LEDs

assign LEDR[0] = w_ResultSrc;

assign LEDR[1] = w_MemWrite;

assign LEDR[4:2] = w_ULAControl[2:0];

assign LEDR[5] = w_ULASrc;

assign LEDR[7] = w_RegWrite;

assign LEDG[8] = ~KEY[1];

assign LEDR[8] = w_ImmSrc;

//assigns LCD

assign w_d0x4 = w_PC;

assign w_d0x5 = w_rd1SrcA;

assign w_d1x5 = w_SrcB;


divisorFrequencia(.clockOriginal(CLOCK_50), .clock1Hz(clock1Hz));

ProgramCounter(.clk(clock1Hz), .rst(KEY[2]),
.PC(w_PC), 
.PCin(w_PCp4));

InstructionMemory(.A(w_PC[7:0]), .RD(w_Inst[31:0]));

ULA adder4(.SrcA(w_PC), .SrcB(3'h4), 
.ULAControl(3'b000), .ULAResult(w_PCp4));

RegisterFile (.wd3(w_Wd3),
.wa3(w_Inst[11:7]), 
.we3(w_RegWrite), 
.clk(clock1Hz),
.ra1(w_Inst[19:15]), 
.ra2(w_Inst[24:20]), 
.rst(KEY[2]), 
.rd1(w_rd1SrcA),
.rd2(w_rd2),
.x0(w_d0x0), .x1(w_d0x1), 
.x2(w_d0x2), .x3(w_d0x3), 
.x4(w_d1x0), .x5(w_d1x1), 
.x6(w_d1x2), .x7(w_d1x3)
);

//mux cuja saída é entrada da ula
meuMux muxULASrc(.i0(w_rd2),.i1(w_Imm), 
.sel(w_ULASrc), .out(w_SrcB));

//mux cuja saída é entrada do outro MUX

meuMux MuxImmSrc(.i0(w_Inst[31:20]),.i1({ w_Inst[31:25], w_Inst[11:7]}), 
.sel(w_ImmSrc), .out(w_Imm));

//mux cuja saída é entrada do wd3

meuMux MuxResSrc(.i0(w_ULAResult),.i1(w_RData), 
.sel(w_ResultSrc), .out(w_Wd3));

ULA(.SrcA(w_rd1SrcA), .SrcB(w_SrcB), 
.ULAControl(w_ULAControl[2:0]), 
.ULAResult(w_ULAResult));

Datamemory(
.A(w_ULAResult), .WD(w_rd2), 
	.RD(w_RData), .WE(w_ResultSrc), 
	.rst(KEY[2]), .clk(clock1Hz));

decoder(.i0(w_Inst[3:0]),   .out(HEX0[0:6]));
decoder(.i0(w_Inst[7:4]),   .out(HEX1[0:6]));
decoder(.i0(w_Inst[11:8]),  .out(HEX2[0:6]));
decoder(.i0(w_Inst[15:12]), .out(HEX3[0:6]));
decoder(.i0(w_Inst[19:16]), .out(HEX4[0:6]));
decoder(.i0(w_Inst[23:20]), .out(HEX5[0:6]));
decoder(.i0(w_Inst[27:24]), .out(HEX6[0:6]));
decoder(.i0(w_Inst[31:28]), .out(HEX7[0:6]));

controlUnit(.Op(w_Inst[6:0]), 
.Funct3(w_Inst[14:12]), .Funct7(w_Inst[31:25]), 
.ResultSrc(w_ResultSrc), .MemWrite(w_MemWrite),
.ULAControl(w_ULAControl[2:0]), .ImmSrc(w_ImmSrc),
.ULASrc(w_ULASrc), .RegWrite(w_RegWrite));

//sprint 7:

// fios durante a sprint 5:

wire w_ULASrc, w_RegWrite;

wire [2:0] w_ULAControl;

wire [7:0] w_PCp4, w_PC, w_rd1SrcA, w_rd2, w_SrcB, w_ULAResult; //apenas mudei w_ULAResultWd3 para w_ULAResult

wire [31:0] w_Inst;

// fios adicionados na sprint 6:

wire  w_MemWrite, w_ResultSrc, clock1Hz;

wire [7:0] w_Wd3, w_Imm, w_RData;

// fios da sprint 7:

wire w_PCSrc, w_Zero, w_Branch;

wire [1:0] w_ImmSrc;

wire [7:0] w_ImmPC, w_PCn;

//assigns LEDs

assign LEDR[0] = w_Branch;

assign LEDR[1] = w_ResultSrc;

assign LEDR[2] = w_MemWrite;

assign LEDR[5:3] = w_ULAControl[2:0];

assign LEDR[6] = w_ULASrc;

assign LEDR[8:7] = w_ImmSrc[1:0];

assign LEDR[9] = w_RegWrite;

//check reset
assign LEDG[8] = ~KEY[1];

//assigns LCD

assign w_d0x4 = w_PC;

divisorFrequencia(.clockOriginal(CLOCK_50), .clock1Hz(clock1Hz));

ProgramCounter(.clk(clock1Hz), .rst(KEY[2]),
.PC(w_PC), 
.PCin(w_PCn));

InstructionMemory(.A(w_PC[7:0]), .RD(w_Inst[31:0]));

// PC + 4
ULA adder4(.SrcA(w_PC), .SrcB(3'h4), 
.ULAControl(3'b000), .ULAResult(w_PCp4));

// PC + imediato
ULA AdderImm(.SrcA(w_Imm), .SrcB(w_PC), 
.ULAControl(3'b000), .ULAResult(w_ImmPC));

RegisterFile (.wd3(w_Wd3),
.wa3(w_Inst[11:7]), 
.we3(w_RegWrite), 
.clk(clock1Hz),
.ra1(w_Inst[19:15]), 
.ra2(w_Inst[24:20]), 
.rst(KEY[2]), 
.rd1(w_rd1SrcA),
.rd2(w_rd2),
.x0(w_d0x0), .x1(w_d0x1), 
.x2(w_d0x2), .x3(w_d0x3), 
.x4(w_d1x0), .x5(w_d1x1), 
.x6(w_d1x2), .x7(w_d1x3)
);

// MULTIPLEXADORES:

//mux cuja saída é entrada da ula
meuMux muxULASrc(.i0(w_rd2),.i1(w_Imm), 
.sel(w_ULASrc), .out(w_SrcB));

//mux cuja saída é entrada do MUXULASrc

mux4p1 MuxImmSrc(	.i0(w_Inst[31:20]), .i1({w_Inst[31:25], w_Inst[11:7]}), 
	.i2({ w_Inst[7], w_Inst[30:25], w_Inst[11:8], 8'b0}),
	.sel(w_ImmSrc), .out(w_Imm));

//mux cuja saída é entrada do wd3

meuMux MuxResSrc(.i0(w_ULAResult),.i1(w_RData), 
.sel(w_ResultSrc), .out(w_Wd3));

// Mux do PC
meuMux MuxPCSrc (.i0(w_PCp4), .i1(w_ImmPC),
		.sel(w_Branch & w_Zero), .out(w_PCn));

ULA(.SrcA(w_rd1SrcA), .SrcB(w_SrcB), 
.ULAControl(w_ULAControl[2:0]), 
.ULAResult(w_ULAResult), .Z(w_Zero));

Datamemory(
.A(w_ULAResult), .WD(w_rd2), 
	.RD(w_RData), .WE(w_MemWrite), 
	.rst(KEY[2]), .clk(clock1Hz));

decoder(.i0(w_Inst[3:0]),   .out(HEX0[0:6]));
decoder(.i0(w_Inst[7:4]),   .out(HEX1[0:6]));
decoder(.i0(w_Inst[11:8]),  .out(HEX2[0:6]));
decoder(.i0(w_Inst[15:12]), .out(HEX3[0:6]));
decoder(.i0(w_Inst[19:16]), .out(HEX4[0:6]));
decoder(.i0(w_Inst[23:20]), .out(HEX5[0:6]));
decoder(.i0(w_Inst[27:24]), .out(HEX6[0:6]));
decoder(.i0(w_Inst[31:28]), .out(HEX7[0:6]));

controlUnit(.Op(w_Inst[6:0]), 
.Funct3(w_Inst[14:12]), .Funct7(w_Inst[31:25]), 
.ResultSrc(w_ResultSrc), .MemWrite(w_MemWrite),
.ULAControl(w_ULAControl[2:0]), .ImmSrc(w_ImmSrc),
.ULASrc(w_ULASrc), .RegWrite(w_RegWrite), .Branch(w_Branch));
*/
//sprint 8
//sprint 7: tentativa de corrigir a sprint 8

// fios durante a sprint 5:

wire w_ULASrc, w_RegWrite;

wire [2:0] w_ULAControl;

wire [7:0] w_PCp4, w_PC, w_rd1SrcA, w_rd2, w_SrcB, w_ULAResult; //apenas mudei w_ULAResultWd3 para w_ULAResult

wire [31:0] w_Inst;

// fios adicionados na sprint 6:

wire  w_MemWrite, w_ResultSrc, clock1Hz;

wire [7:0] w_Wd3, w_Imm, w_RData;

// fios da sprint 7:

wire w_PCSrc, w_Zero, w_Branch;

wire [1:0] w_ImmSrc;

wire [7:0] w_ImmPC, w_PCn;

wire [7:0] w_Address, w_DataOut, w_DataIn, w_RegData;


//assigns LEDs

assign LEDR[0] = w_Branch;

assign LEDR[1] = w_ResultSrc;

assign LEDR[2] = w_MemWrite;

assign LEDR[5:3] = w_ULAControl[2:0];

assign LEDR[6] = w_ULASrc;

assign LEDR[8:7] = w_ImmSrc[1:0];

assign LEDR[9] = w_RegWrite;

//check reset
assign LEDG[8] = ~KEY[1];

//assigns LCD

assign w_d0x4 = w_PC;
assign w_d1x4 = w_DataOut;

divisorFrequencia(.clockOriginal(CLOCK_50), .clock1Hz(clock1Hz));

ProgramCounter(.clk(clock1Hz), .rst(KEY[2]),
.PC(w_PC), 
.PCin(w_PCn));

InstructionMemory(.A(w_PC[7:0]), .RD(w_Inst[31:0]));

// PC + 4
ULA adder4(.SrcA(w_PC), .SrcB(3'h4), 
.ULAControl(3'b000), .ULAResult(w_PCp4));

// PC + imediato
ULA AdderImm(.SrcA(w_Imm), .SrcB(w_PC), 
.ULAControl(3'b000), .ULAResult(w_ImmPC));

RegisterFile (.wd3(w_Wd3),
.wa3(w_Inst[11:7]), 
.we3(w_RegWrite), 
.clk(clock1Hz),
.ra1(w_Inst[19:15]), 
.ra2(w_Inst[24:20]), 
.rst(KEY[2]), 
.rd1(w_rd1SrcA),
.rd2(w_rd2),
.x0(w_d0x0), .x1(w_d0x1), 
.x2(w_d0x2), .x3(w_d0x3), 
.x4(w_d1x0), .x5(w_d1x1), 
.x6(w_d1x2), .x7(w_d1x3)
);

// MULTIPLEXADORES:

//mux cuja saída é entrada da ula
meuMux muxULASrc(.i0(w_rd2),.i1(w_Imm), 
.sel(w_ULASrc), .out(w_SrcB));

//mux cuja saída é entrada do MUXULASrc

mux4p1 MuxImmSrc(	.i0(w_Inst[31:20]), .i1({w_Inst[31:25], w_Inst[11:7]}), 
	.i2({ w_Inst[7], w_Inst[30:25], w_Inst[11:8], 8'b0}),
	.sel(w_ImmSrc), .out(w_Imm));

//mux cuja saída é entrada do wd3

meuMux MuxResSrc(.i0(w_ULAResult),.i1(w_RegData), 
.sel(w_ResultSrc), .out(w_Wd3));

// Mux do PC
meuMux MuxPCSrc (.i0(w_PCp4), .i1(w_RegData),
		.sel(w_Branch & w_Zero), .out(w_PCn));

ULA(.SrcA(w_rd1SrcA), .SrcB(w_SrcB), 
.ULAControl(w_ULAControl[2:0]), 
.ULAResult(w_ULAResult), .Z(w_Zero));

Datamemory(
.A(w_ULAResult), .WD(w_rd2), 
	.RD(w_RData), .WE(w_MemWrite), 
	.rst(KEY[2]), .clk(clock1Hz));

decoder(.i0(w_Inst[3:0]),   .out(HEX0[0:6]));
decoder(.i0(w_Inst[7:4]),   .out(HEX1[0:6]));
decoder(.i0(w_Inst[11:8]),  .out(HEX2[0:6]));
decoder(.i0(w_Inst[15:12]), .out(HEX3[0:6]));
decoder(.i0(w_Inst[19:16]), .out(HEX4[0:6]));
decoder(.i0(w_Inst[23:20]), .out(HEX5[0:6]));
decoder(.i0(w_Inst[27:24]), .out(HEX6[0:6]));
decoder(.i0(w_Inst[31:28]), .out(HEX7[0:6]));

controlUnit(.Op(w_Inst[6:0]), 
.Funct3(w_Inst[14:12]), .Funct7(w_Inst[31:25]), 
.ResultSrc(w_ResultSrc), .MemWrite(w_MemWrite),
.ULAControl(w_ULAControl[2:0]), .ImmSrc(w_ImmSrc),
.ULASrc(w_ULASrc), .RegWrite(w_RegWrite), .Branch(w_Branch));

ParallelOUT(.RegData(w_rd2), .Address(w_ULAResult),
	.EN(w_MemWrite), .clk(clock1Hz), .rst(KEY[2]), //ok
	.DataOut(w_DataOut));

ParallelIN(.MemData(w_RData), .Address(w_ULAResult), .DataIn(SW[7:0]), .RegData(w_RegData));

endmodule