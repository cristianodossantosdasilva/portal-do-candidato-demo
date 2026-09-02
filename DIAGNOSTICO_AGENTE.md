# Diagnóstico do Consultor de Carreiras

## Papel

O Portal do Candidato representa o agente de pré-venda da Jornada de Ingresso. O objetivo é orientar uma escolha consciente e facilitar o próximo passo comercial sem bloquear a decisão do candidato.

## Estado preservado

- A página pública contém indicação de agente ao vivo quando o Embedded Messaging inicializa.
- A página contém instruções para avaliadores e identificação explícita do modo offline.
- O fallback determinístico preserva a demonstração quando o runtime temporário estiver indisponível.
- O repositório contém documentação específica de arquitetura, testes e limitações.

## Dependência atual

A experiência generativa atual depende da organização temporária usada no hackathon. A indisponibilidade ou expiração desse ambiente não deve quebrar o portal, mas impede respostas generativas em tempo real.

## Lacuna de evolução

Ainda não existe gateway nem motor externo integrado. A próxima fase deverá definir o contrato de API, a política de sessão, as fontes autorizadas, os limites de consumo, a observabilidade e o comportamento de fallback.

## Guardrails obrigatórios

- Não inventar preço, bolsa, desconto, prazo, nota institucional ou condição de matrícula.
- Não criar urgência artificial nem alegar escassez sem fonte oficial.
- Não prometer emprego, renda ou empregabilidade.
- Não diagnosticar vocação, personalidade ou condição pessoal.
- Não repetir perguntas já respondidas com confiança.
- Não afirmar que uma ação foi concluída sem retorno real da integração.
- Encaminhar exceções e decisões não autorizadas para atendimento humano.

## Rastreabilidade de Artefatos

- **Evidência Histórica**: O YAML histórico fiel (`agenteforce_pre_venda.yaml`) está na raiz para comprovar a implementação original.
- **Evolução**: O blueprint v2 em `docs/evolucao/` detalha a proposta futura para resolver lacunas e remover restrições identificadas (ex: mitigar pressão comercial), sem alterar a evidência do que foi entregue.
