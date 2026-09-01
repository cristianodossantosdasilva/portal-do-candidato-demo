# Testes e Limitações

## Ambientes e Avaliação
- O layout do Portal foi validado de forma independente: estrutura HTML semântica, ícones dinâmicos Phosphor e responsividade Mobile First.
- O carregamento da janela de chat e das conversas foi testado em navegadores modernos.

## Conexão ao Salesforce e Limitações
- **Org Expirável:** A implementação original utiliza uma org temporária do Salesforce Agentforce, ainda acessível no momento da preservação e sujeita a expiração futura.
- **Fallback Estático:** Em caso de falha de carregamento do widget (devido à omissão de identificadores para segurança ou org inativa), a página ativa o modo fallback. Este modo apresenta a mesma janela com mensagens pré-renderizadas, permitindo que os avaliadores naveguem e compreendam a experiência idealizada. O fallback público é uma simulação determinística da experiência e não equivale ao runtime do Agentforce nem a uma resposta de LLM em tempo real.

