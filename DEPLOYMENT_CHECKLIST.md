# Checklist de implantação e validação

## Antes da publicação

- [ ] Incluir validação de hash (SHA-256) do YAML histórico e rastreabilidade da evidência fiel frente à evolução.

- [ ] Confirmar que o repositório de trabalho é `portal-do-candidato-demo`.
- [ ] Confirmar branch e HEAD de origem.
- [ ] Confirmar working tree limpa antes das alterações.
- [ ] Validar que não há tokens, senhas, cookies, chaves privadas ou arquivos `.env` versionados.
- [ ] Validar URLs e identificadores públicos necessários ao modo live-first.
- [ ] Confirmar que o fallback está identificado como demonstração determinística.

## Portal

- [ ] Carregar `index.html` por servidor HTTP local.
- [ ] Validar CSS, JavaScript, ícones e fontes.
- [ ] Validar o guia "Como testar o agente".
- [ ] Validar o indicador de agente ao vivo.
- [ ] Validar alternância para o modo offline quando o runtime não responder.
- [ ] Testar em visualização de computador e celular.

## Agente de pré-venda

- [ ] Responder em português do Brasil.
- [ ] Usar contexto disponível antes de perguntar.
- [ ] Fazer somente perguntas que mudem a orientação ou o próximo passo.
- [ ] Consultar fonte autorizada para curso, metodologia, preço, bolsa e regra.
- [ ] Não prometer emprego, renda ou resultado.
- [ ] Não criar escassez ou urgência sem evidência oficial.
- [ ] Entregar contexto factual no handoff para o pós-venda.

## Publicação

- [ ] Revisar `git diff` integralmente.
- [ ] Executar varredura por segredos e identificadores não autorizados.
- [ ] Registrar arquivos criados e alterados.
- [ ] Criar commit específico somente após aprovação.
- [ ] Confirmar o HEAD remoto e a publicação HTTPS.

