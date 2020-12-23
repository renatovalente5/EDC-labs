-- a)
SELECT P.*
    FROM Pessoa P
    WHERE Evento_ID NOT NULL;

-- b)
SELECT E.NOME, E.Data, E.Inicio, E.Descricao, E.Nome AS LOCAL
    FROM Evento AS E, LOCAL AS L    -- podemos fazer com Join ou junção de tabelas
    WHERE E.Local_ID == L.ID;

-- c)
SELECT e.*
    FROM Evento e JOIN Local l on e.Local_ID = l.ID
    where l.Nome = "UA";

-- d)
SELECT *
    FROM Evento e
    where e.Data >= '2017-09-25';

-- e)
SELECT p.Nome, p.Email
    FROM Pessoa p JOIN Evento E ON E.ID = p.Evento_ID
    where E.Nome = 'Abertura UA';

-- f)
SELECT p.Nome, p.Email
    FROM Pessoa p JOIN Evento E ON E.ID = p.Evento_ID JOIN Local L ON L.ID = E.Local_ID
    where E.Nome = 'Abertura UA' AND e.Data >= '2017-09-20';
