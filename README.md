# PROJETO CNPJ 2022

Com o objetivo de praticar os conhecimentos obtidos em Python, SQL e Spark com PySpark, criei esse projeto para tratar os dados abertos da Receita Federal.

Os dados podem ser obtidos no link abaixo:
https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj

Se o link estiver quebrado, como geralmente está, dá pra ver os arquivos nesse outro: http://200.152.38.155/CNPJ/

![imagem do site da RFB](https://github.com/gittil/projeto-cnpj-2022/blob/main/imagens/tela-site-rfb.png)


O arquivo vem no formato .zip, então é só descompactar pra usar, porém, como o nome tem um "." bem no meio, no Windows ele não entende que é um CSV e você precisará renomear, tirando o "." e colocando no lugar certo ".csv".

No Linux foi tudo tranquilo e abriu o arquivo normalmente.

Na primeira parte, iremos manipular os dados que se encontram em 10 arquivos CSV´s e possuem mais de 51 milhões de registro pois são todas as empresas do Brasil, independente do segmento.

Após organizar esses dados e realizar algumas limpezas e tratamentos, a saída será um arquivo parquet com todos os registros.

Após essa etapa passaremos o filtro por atividade (CNAE) para filtar apenas o segmento que desejamos.
 