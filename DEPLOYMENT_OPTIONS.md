# Opções de implantação - Portal do Candidato

## Estado atual

O portal é um frontend estático publicado em HTTPS. Enquanto a organização temporária estiver disponível, o portal tenta carregar o Consultor de Carreiras no Salesforce Agentforce. Se o runtime não responder, a interface alterna para uma demonstração determinística identificada como modo offline.

## Evidência e Evolução

A raiz do projeto contém o arquivo `agenteforce_pre_venda.yaml`, que serve como evidência histórica fiel do que foi implementado no hackathon.
A pasta `docs/evolucao/` contém o blueprint v2, que representa uma proposta futura de evolução e não a configuração implantada.
A diferença garante a rastreabilidade do projeto sem adulterar a versão histórica.

## Opção A - Portfólio estático atual

- Frontend: GitHub Pages.
- Runtime principal: Salesforce Agentforce temporário, quando disponível.
- Contingência: fallback determinístico no navegador.
- Uso: preservação imediata da demonstração e avaliação do projeto.

## Opção B - Agente externo com gateway

Arquitetura-alvo recomendada para a evolução fora da OrgFarm:

1. O portal envia a mensagem para uma API intermediária.
2. A API protege segredos, valida a entrada e controla a sessão.
3. O motor externo executa o comportamento do agente usando instruções e fontes autorizadas.
4. A resposta volta ao portal em um contrato estável.
5. Em indisponibilidade, o portal mantém o fallback determinístico.

A escolha do provedor, modelo, hospedagem e persistência ainda não foi fechada nesta fase.

## Opção C - Reconexão futura ao Salesforce

Quando existir uma organização Salesforce apropriada, o portal poderá voltar a usar Agentforce por configuração, sem reconstrução da interface. CORS, domínios autorizados, deployment, canal, versão ativa do agente e políticas de dados deverão ser revalidados.

## Requisitos comuns

- HTTPS público.
- Segredos fora do frontend.
- Mensagens de modo ao vivo e modo demonstração sem ambiguidade.
- Fontes oficiais acima da memória do modelo.
- Sem promessa de bolsa, preço, empregabilidade ou prazo sem fonte confiável.
- Registro de erros sem dados pessoais ou tokens.
- Testes em computador e celular.

