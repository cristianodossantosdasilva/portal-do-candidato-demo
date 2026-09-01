# Portal do Candidato - Demo

## Resumo Executivo
Este repositório é um ambiente demonstrativo isolado (público) que documenta e apresenta a interface de frontend projetada para o **Consultor de Carreiras UniCesumar**, um agente de inteligência artificial criado para o projeto **Marco Zero** durante o Hackathon Vitru 2026.

## Equipe e Contribuições
O Marco Zero foi desenvolvido por uma equipe multidisciplinar no Hackathon Vitru 2026. O trabalho reuniu contexto de negócio, análise de dados, modelagem de hipóteses, perspectiva do estudante e implementação técnica assistida por IA. Cristiano Silva foi responsável pela criação e configuração técnica dos dois agentes e pela base de conhecimento no Salesforce Agentforce, apoiado pelas contribuições complementares da equipe descritas nesta documentação.

### Integrantes da Equipe
- **[Victoria Suares](https://www.linkedin.com/in/victoria-suares/)**: Trouxe a perspectiva do aluno sobre dificuldades na graduação, no estudo e na permanência, e apoiou o conceito e desenvolvimento do agente de mentoria ocupacional, posteriormente apresentado como Consultor de Carreiras.
- **[Yasmin Baltieri](https://www.linkedin.com/in/yasminbaltieri/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3Bb93z3nWqTnGpeUV5z9qLPw%3D%3D)**: Atuou como madrinha do time; trouxe informações sobre o modelo de negócio da Vitru, contexto sobre os dados anonimizados ligados à dor explorada, e participou da análise dos dados.
- **[Yasmim Sobrinho](https://www.linkedin.com/in/yasmim-sobrinho-19aa14160/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3Bb93z3nWqTnGpeUV5z9qLPw%3D%3D)**: Apoiou a modelagem dos dados, ajudou a identificar possíveis causas de evasão e contribuiu com perspectiva estatística para as hipóteses.
- **[Eduardo Ferreira Mattos](https://www.linkedin.com/in/eduardo-ferreira-mattos/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3Bb93z3nWqTnGpeUV5z9qLPw%3D%3D)**: Apoiou a busca das possíveis causas de evasão e participou da análise dos dados.
- **[Cristiano Silva](https://github.com/cristianodossantosdasilva)**: Participou da análise dos dados com apoio de ferramentas de IA, identificou possíveis causas de evasão e dores da jornada do aluno, destacou a ausência de onboarding e dificuldades de navegação; além disso, implementou tecnicamente, criando e configurando os dois agentes e a base de conhecimento no Salesforce Agentforce com programação assistida por IA.

## Metodologia Assistida por IA
Este agente foi desenvolvido com programação assistida por inteligência artificial, desenvolvimento orientado por intenção e prototipação iterativa (vibe coding). O processo não consistiu em aceitar automaticamente código gerado. O desenvolvimento ocorreu em ciclos de intenção, geração assistida, revisão, testes, correção e validação humana.

**Origem das ferramentas de IA utilizadas:**
- **Microsoft Copilot, Antigravity e Gemini:** ferramentas pessoais pagas e utilizadas por Cristiano.
- **Kiro:** fornecido pela AWS durante o hackathon.
- **Claude:** cedido pela Salesforce somente para ajustes pontuais.
- **Salesforce Agentforce:** plataforma de implementação e orquestração dos agentes.

## Demo Online
- [Acessar Portal do Candidato (GitHub Pages)](https://cristianodossantosdasilva.github.io/portal-do-candidato-demo/)

## Evidência e Limitação
Os metadados exportados, os portais navegáveis e as capturas do Agentforce Builder comprovam a arquitetura e a implementação dos agentes. A execução automatizada dos cenários no Preview não foi preservada devido a limitações do ambiente de automação. O fallback público é uma simulação determinística da experiência e não equivale ao runtime do Agentforce nem a uma resposta de LLM em tempo real.

A implementação original utiliza uma org temporária do Salesforce Agentforce, ainda acessível no momento da preservação e sujeita a expiração futura.

**Nota técnica:** A substituição proposital do Org ID no código-fonte por medida de segurança impossibilita a conexão direta do widget Embedded Messaging de conectar na Org do Salesforce neste repositório. Por isso, a página adota explicitamente o modo offline/fallback para demonstração visual permanente.

## Arquitetura do Agente
*(Veja mais em [docs/ARQUITETURA_DO_AGENTE.md](docs/ARQUITETURA_DO_AGENTE.md))*
O agente ativo **Consultor de Carreiras (v7)** implementado:
1. Roteador Comercial
2. Consultoria e Quebra de Objeções
3. Fechamento de Matrícula
4. Foco na Venda (Off-Topic)

## Relação com o Agente Complementar
A jornada completa do estudante pode ser consultada no ambiente irmão:
- [Portal do Aluno (Especialista de Sucesso)](https://github.com/cristianodossantosdasilva/portal-aluno-demo)

## Licença e Uso
Este repositório contém artefatos de demonstração construídos durante o Hackathon Vitru 2026. Todos os direitos sobre a marca e o caso de uso pertencem à instituição. O código e a interface gráfica servem estritamente para propósitos de demonstração técnica de portfólio.

