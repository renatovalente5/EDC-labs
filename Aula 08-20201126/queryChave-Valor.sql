--exercicio e)
-- a
SELECT P_NOME.Value AS  Nome,
       P_EMAIL.Value AS Email
FROM  Objetos AS P_NOME,
      Objetos AS P_EMAIL
WHERE
    P_NOME.ID in (SELECT ID From Objetos WHERE Key == 'Tipo' and value=='Pessoa')
    AND P_NOME.ID == P_EMAIL.ID
    AND P_NOME.Key == 'Nome'
    AND P_EMAIL.key == 'Email'
    AND P_NOME.ID IN (SELECT ID from Objetos WHERE Key=='Evento_ID');
