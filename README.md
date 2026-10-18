# Policy Intelligence Platform

MVP de uma Plataforma Inteligente de Políticas Públicas Comparadas, voltada ao apoio à análise e à tomada de decisão na Casa Civil.

## Objetivo

A plataforma busca organizar, estruturar e comparar evidências de políticas públicas nacionais e internacionais, permitindo analisar:

- problema público;
- contexto;
- público-alvo;
- desenho da intervenção;
- implementação;
- método de avaliação;
- resultados;
- limitações;
- comparabilidade com o contexto de São Paulo.

## Escopo atual do MVP

Nesta primeira versão, o eixo ativo é:

**Educação → Ensino Médio → Evasão Escolar**

A arquitetura já prevê expansão futura para outros temas, como Saúde, Mobilidade, Gestão Pública, Desenvolvimento Urbano, Proteção Social, Energia, Saneamento, Transformação Digital, Clima, Desenvolvimento Econômico e Agricultura.

## Caso real utilizado no MVP

O primeiro caso validado é:

**PODER — Programa de Oportunidades y Desarrollo para Evitar Riesgos**

- País: México
- Região: Cidade do México
- Fonte: Banco Mundial
- Documento: Policy Research Working Paper 9085
- Ano: 2019
- Amostra: 5.274 estudantes
- Método: Randomized Control Trial (RCT)
- Intervenção: habilidades socioemocionais baseadas em CBT + tutoria de matemática
- Resultado: efeitos mistos, com baixa adesão e sem efeito robusto sobre a matrícula no ano seguinte

## Pipeline desenvolvido

PDF oficial  
→ Python  
→ extração automática de texto  
→ divisão em chunks  
→ prompt estruturado  
→ futura integração com LLM  
→ JSON estruturado  
→ validação humana  
→ base curada  
→ comparação entre casos

## Tecnologias

- Python
- PyMuPDF
- Google Colab
- HTML/CSS/JavaScript
- JSON
- GitHub

## Próximas etapas

- integrar LLM para extração semântica automática;
- automatizar busca de documentos em fontes externas;
- ampliar a base com casos de outros países;
- criar perfil de referência de São Paulo;
- desenvolver métricas de similaridade;
- integrar banco de dados;
- explorar Knowledge Graphs, redes e Process Mining.

## Estrutura do repositório

```text
app/
data/
  raw/
  curated/
notebooks/
src/
requirements.txt
README.md
