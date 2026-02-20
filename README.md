# FLEXT dbt LDIF

Projeto dbt para modelagem analitica de dados extraidos de arquivos LDIF.

Descricao oficial atual: "FLEXT dbt LDAP - dbt Models for LDIF Data Transformation".

## O que este projeto entrega

- Padroniza transformacoes de dados de diretorio em SQL.
- Entrega marts para analise de consistencia e migracao.
- Estrutura camada de dados para indicadores operacionais.

## Contexto operacional

- Entrada: dados LDIF em staging.
- Saida: modelos dbt analiticos do dominio LDIF.
- Dependencias: pipeline de ingestao LDIF e ambiente dbt.

## Estado atual e risco de adocao

- Qualidade: **Alpha**
- Uso recomendado: **Nao produtivo**
- Nivel de estabilidade: em maturacao funcional e tecnica, sujeito a mudancas de contrato sem garantia de retrocompatibilidade.

## Diretriz para uso nesta fase

Aplicar este projeto somente em desenvolvimento, prova de conceito e homologacao controlada, com expectativa de ajustes frequentes ate maturidade de release.
