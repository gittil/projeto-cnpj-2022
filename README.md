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

Nossa estrutura de pasta local será a seguinte:

**RAW**: A pasta RAW receberá todos os dados brutos, da forma como eles são disponibilizados no site da RFB. Essa pasta servirá como uma Staging Area.

Link para o nbviewer: https://nbviewer.org/github/gittil/projeto-cnpj-2022/blob/main/01_extract_RAW.ipynb

**BRONZE**: A pasta BRONZE receberá os dados já no formato parquet com o minimo de tratamento, como por exemplo, nome nas colunas e drop em algumas colunas para não expor dados sensiveis como email e telefone.

**SILVER**: A pasta SILVER irá receber os dados refinados. Aqui faremos joins das tabelas que estão na pasta Bronze.

**GOLD**: A pasta GOLD irá receber os dados finais já com agregações, group by, entre outras informações que serão utilizadas na criação dos Dashboards e Reports.


## Carga dos Dados

loading...