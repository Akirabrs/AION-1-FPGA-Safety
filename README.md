# 🛡️ AION-1: Acelerador FPGA para Segurança de Fusão Nuclear

O **AION-1 Alpha** é um sistema de segurança crítica (Watchdog) baseado em hardware dedicado para reatores de fusão. O foco principal é a proteção contra disrupções plasmáticas através de uma resposta determinística ultra-rápida.

### 🛠️ Especificações Técnicas
* **Latência Determinística:** Resposta de hardware validada em **21 nanossegundos** para disparo de pulsos de segurança (`KILL_PULSE`).
* [cite_start]**Protocolo PSQ:** Protocolo de Sincronização Quântica (determinismo temporal) que reduz o *jitter* para menos de 2 µs, superando sistemas RTOS e Linux convencionais[cite: 215, 390, 397].
* **Arquitetura em 3 Camadas:** Integração entre Simulação Python, Firmware STM32 e Hardware Verilog RTL.
* **Segurança Crítica:** Projetado para monitorização de limites de estabilidade MHD com prioridade absoluta de execução.

### 📁 Estrutura de Pastas
* `/hardware`: Código Verilog RTL do núcleo PSQ e Testbenches.
* `/docs`: Roadmap da FEBRACE, logs de timing e diagramas de arquitetura.

### 🏆 Reconhecimento
Este projeto foi desenvolvido como parte da iniciativa **AION**, visando a implementação de padrões de segurança de nível industrial em cenários de energia limpa e soberania tecnológica.
