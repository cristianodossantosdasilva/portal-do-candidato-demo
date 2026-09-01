# Arquitetura do Agente: Consultor de Carreiras UniCesumar

## Identificação
- **Papel:** Consultoria de vendas, pré-ingresso e matrícula.
- **Versão Ativa e Validada:** v7 (confirmada e imutável no Backup Bruto do Agent Builder).

## Tópicos e Capabilities
- O agente baseia-se num Copilot (LLM baseada na configuração Einstein) com roteamento para 4 habilidades/sub-agentes (topics):
  
  1. **Roteador Comercial:** Avalia a intenção inicial do usuário e o redireciona imediatamente.
  2. **Consultoria e Quebra de Objeções:** Sub-agente que orienta sobre cursos, flexibilidade de horários, verifica a disponibilidade, preenche variáveis de intenção (course_interest, main_goal, availability) e eleva o nível de "aquecimento" do candidato.
  3. **Fechamento de Matrícula:** Sub-agente transacional que envia links de fechamento simplificados (URL direta para matrícula) reforçando o senso de oportunidade.
  4. **Foco na Venda:** Sub-agente focado em off-topics (conversa fora do foco). Realiza o bloqueio amigável de outros assuntos para reconduzir à finalização da venda.

## Conhecimento (RAG)
O agente pesquisa em dados oficiais e em artigos parametrizados para responder dúvidas de cursos, carga horária e mensalidade (Ação `AnswerQuestionsWithKnowledge`).

## Esclarecimento sobre metadados
A estrutura acima reflete com fidelidade o comportamento ativo e a extração consolidada no ambiente do Agent Builder para este Hackathon. Eventuais duplicidades (como off-topics duplicados presentes nos esboços em TXT) não existem na versão v7 ativada.

