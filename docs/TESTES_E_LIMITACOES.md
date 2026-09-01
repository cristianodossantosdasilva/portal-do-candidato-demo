# Testes e Limitações

## Ambientes e Avaliação
- O layout do Portal do Candidato foi validado de forma independente: estrutura HTML semântica, ícones dinâmicos Phosphor e responsividade Mobile First.
- O carregamento da janela de chat e das conversas foi testado em navegadores modernos.

## Integração ao Salesforce Agentforce
O portal adota uma estratégia **live-first**:

1. **Modo ao vivo:** Enquanto a org temporária do Salesforce Agentforce estiver ativa, o portal tenta carregar o agente original (Consultor de Carreiras v7) via Embedded Messaging. O widget exibirá a identificação de modo ao vivo.
2. **Fallback automático:** Se a org estiver indisponível, expirar ou o carregamento falhar, o portal alterna automaticamente para uma simulação determinística claramente identificada como demonstração offline. O fallback não equivale a uma resposta de um modelo de linguagem em tempo real.

## Limitações do Ambiente de Demonstração
- A org temporária está sujeita a expiração futura após o período de avaliação do Hackathon.
- A execução automatizada dos cenários no Preview não foi preservada devido a limitações do ambiente de automação.
- O fallback público é uma simulação determinística da experiência e não equivale ao runtime do Agentforce.

