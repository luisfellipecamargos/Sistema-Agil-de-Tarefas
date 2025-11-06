# Sistema Ágil de Tarefas

## Sobre o projeto

Este projeto simula o desenvolvimento de um sistema de gerenciamento de tarefas para uma startup de logística, aplicando metodologias ágeis e boas práticas de Engenharia de Software.

## Objetivo

Criar um sistema que permita acompanhar o fluxo de trabalho em tempo real, priorizar tarefas críticas e monitorar o desempenho da equipe.

## Metodologia

Utilizei a abordagem Kanban com GitHub Projects:
- Colunas: A Fazer, Em Progresso, Concluído
- Issues para tarefas
- Branches por funcionalidade
- Pull Requests para revisão
- GitHub Actions para testes automatizados

## Funcionalidades

- Criar, listar, editar e excluir tarefas
- Marcar como concluída
- Filtrar por prioridade (após mudança de escopo)

## Qualidade

- Testes automatizados com [Pytest/Jest]
- Pipeline com GitHub Actions
- Commits semânticos e frequentes

## Como rodar

```bash
git clone https://github.com/seu-usuario/techflow-task-manager.git
cd techflow-task-manager
npm install
npm start
npm test
