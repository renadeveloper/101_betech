📝 **README - Estatísticas do Brasileirão Série A de 2003 a 2019**

Este código em Python permite analisar os dados dos times que participaram do campeonato nos anos de 2003 a 2019, fornecendo estatísticas como gols pró e contra, saldo de gols, gols marcados como mandante e visitante, total de gols, além da quantidade de vitórias, empates e derrotas de cada equipe.

Este projeto foi desenvolvido como Projeto Final da disciplina Lógica de Programação II do curso de Python e Ciência de Dados <BeTech> by Braskem em parceria com a Ada Tech com o objetivo de aplicar os conhecimentos ensinados durante a disciplina e mostrar a utilização das bibliotecas e técnicas aprendidas. Portanto, o foco principal está na implementação das funcionalidades propostas e não na análise completa de todo o conjunto de dados.

## ✅ Pré-requisitos

Antes de executar o código, certifique-se de que você tenha o Python instalado em seu sistema. Este projeto foi desenvolvido utilizando a versão 3.7.3, mas é compatível com versões mais recentes. Além disso, você precisará ter os seguintes arquivos na mesma pasta:

- `main.py`
- `campeonato-brasileiro-full.csv`
- `funcoes_validacao.py`
- `funcoes_impressao.py`
- `funcoes_calculo.py`
- `funcoes_input.py`
- `funcao_loop_principal.py`

## ⚙️ Como executar o código

1. Abra um terminal ou prompt de comando.
2. Navegue até a pasta onde você salvou os arquivos do projeto.
3. Digite o seguinte comando no terminal:

```python
python main.py
```

4. Aguarde até que o código seja executado.

## 📚 Bibliotecas utilizadas

Este projeto utiliza apenas a biblioteca CSV, que é uma biblioteca nativa do Python e não requer instalação adicional.

## 📂 Manipulação de arquivos

O código lê os dados dos times a partir de um arquivo CSV chamado `campeonato-brasileiro-full.csv` que contém as informações necessárias para calcular as estatísticas dos times. Para a correta execução do código, certifique-se de que esse arquivo esteja presente na mesma pasta do código.

Este arquivo é uma fração de um conjunto de dados maior disponível no Kaggle, nesse [link](https://www.kaggle.com/datasets/adaoduque/campeonato-brasileiro-de-futebol). Devido ao calendário de jogos depois pandemia, que difere do padrão, e considerando o escopo deste projeto, optei por utilizar apenas uma parte dos dados disponíveis, a fim de facilitar o tratamento e o foco no aprendizado dos conceitos ensinados durante o curso. Caso deseje explorar o conjunto de dados completo, você pode baixá-lo do Kaggle e adaptar o código para tratar o conjunto completo.

## :mag_right: Sobre o critério de avaliação

Neste projeto final, foram utilizados os seguintes critérios de avaliação:

- **Dicionários e Tuplas**: O projeto faz amplo uso de dicionários e tuplas nas funções `obter_estatisticas` e `imprimir_estatisticas` sendo o uso do dicionários voltado para acessar o arquivo por meio da função `DictReader` da biblioteca CSV. Já a tupla foi utilizada para retorno entre as funções citadas anteriormente.

- **Funções**: O projeto envolve a criação e uso de várias funções que foram criadas principalmente para organização, pois o código não exige reuso. Apenas uma função foi criada visando o reuso de código, a função `volta_para_inicio_arquivo` cuja função é retornar o ponteiro do arquivo para o início após cada leitura.  

- **Manipulação de arquivos**: O código realiza a leitura de dados do arquivo CSV `campeonato-brasileiro-full.csv` para acessar as informações sobre os times e partidas do campeonato brasileiro. Esses dados são lidos enquanto dicionários por meio da função `DictReader` da biblioteca CSV. A partir da leitura enquanto dicionário, fica mais fácil obter as estatísticas e cálculos necessários.

- **Tratamento de exceções**: Foi utilizado o tratamento de exceções nas funções `imprimir_estatisticas`, `obter_time` e `obter_ano` para evitar que houvesse erro por divisão por zero no cálculo de médias de gols e para que as entradas de time e ano fossem, respectivamente, alphanuméricos sem acentose dígitos. Ainda há mais um tratamento de exceção por tecla de interrupção do usuário.

Não foram utilizados os conceitos de lambda, map, reduce e filter devido à natureza e complexidade das operações realizadas. O escopo do projeto exigiu um processamento mais abrangente e estruturado dos dados, tornando outras abordagens mais adequadas para lidar com as manipulações necessárias.

## 🏁 Conclusão

O objetivo desse repositório é destacar o trabalho que realizei, mostrar as técnicas e conceitos que aprendi e servir como referência para mim e para outras pessoas interessadas em Python e Ciência de Dados. Fique à vontade para explorar o repositório, verificar os códigos e arquivos disponíveis e me contatar, se surgirem dúvidas. 

