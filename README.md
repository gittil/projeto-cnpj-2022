# PROJETO CNPJ 2022

Com o objetivo de praticar os conhecimentos obtidos em Python, SQL e Spark com PySpark, criei esse projeto para tratar os dados abertos da Receita Federal.


## Extraindo os Dados 
Os dados abertos da Receita Federal do Brasil podem ser obtidos nesse link abaixo:

https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj

Na estrutura completa, temos 10 arquivos com os dados básicos das empresas que formam uma tabela, mais 10 arquivos com os dados referentes ao estabalecimento (endereço, atividade, etc) que formam outra tabela e mais 10 arquivos com os dados dos sócios que formam a terceira tabela.

Essas 3 tabelas se relacionam pela chave CNPJ básico, que são os números do CNPJ antes da "/".

Se o link estiver quebrado, como geralmente está, dá pra ver os arquivos nesse outro: http://200.152.38.155/CNPJ/

![imagem do site da RFB](https://github.com/gittil/projeto-cnpj-2022/blob/main/imagens/tela-site-rfb.png)


O arquivo vem no formato .zip, então é só descompactar pra usar, porém, como o nome tem um "." bem no meio, no Windows ele não entende que é um CSV e você precisará renomear, tirando o "." e colocando no lugar certo ".csv".

No Linux foi tudo tranquilo e abriu o arquivo normalmente.

Os arquivos brutos extraídos foram colocados em uma pasta com o nome RAW. 

## Tratando os Dados

Na primeira parte do tratamento, iremos manipular os dados que se encontram nos 10 arquivos CSV´s dos estabelecimentos pois neles já temos as informações que precisamos e possuem mais de 51 milhões de registro pois são todas as empresas do Brasil, independente do segmento.

Após unificar esses 10 arquivos CSV's em um único DF, foi necessário um select para escolher quais seriam as colunas que seriam utilizadas no próximo passo do tratamento.

Foram retirados dados como telefone e email para não expor essas informações.

Nessa etapa iremos salvar os arquivos pré tratados em uma pasta chamada BRONZE.


## Carga dos Dados

loading...