// Módulo PSQ (Protocolo de Sincronização Quântica)
// Hardware de Segurança Crítica para Tokamak
module psq_core (
    input wire clk,
    input wire rst_n,
    input wire [15:0] z_pos,     // Posição Vertical
    input wire [15:0] q95_val,   // Fator de Segurança
    output reg kill_pulse,       // Gatilho de Disrupção
    output reg [1:0] status      // 00: OK, 11: PERIGO
);
    localparam MAX_Z = 16'h0033; // Limite de 20cm
    localparam MIN_Q = 16'h0200; // Limite q95 = 2.0

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            kill_pulse <= 0;
            status <= 2'b00;
        end else begin
            if (z_pos > MAX_Z || q95_val < MIN_Q) begin
                kill_pulse <= 1'b1; // DISPARAR SEGURANÇA
                status <= 2'b11;
            end else begin
                kill_pulse <= 1'b0;
                status <= 2'b00;
            end
        end
    end
endmodule
