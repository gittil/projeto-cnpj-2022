def converter_coluna(dataframe, nome_col, novotipo):
    """Função para converter uma coluna no DF

    Args:
        dataframe (dataframe): passamos nesse parâmetro o nome do DF que será alterado a coluna 
        nome_col (nome da coluna): passamos nesse parâmetro qual a coluna que do DF que irá receber a alterção
        novoTipo (novo tipo): passamos nesse parâmetro qual o novo tipo que a coluna irá receber

    Returns:
        DF: retorna o DF com as colunas alteradas
    """
    for nome in nome_col:
        dataframe = dataframe.withColumn(nome,dataframe[nome].cast(novotipo))
    return dataframe 



