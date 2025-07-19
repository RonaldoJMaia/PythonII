SELECT nome_prato [Nome do prato], fun.nome [criador], ingredientes, modo_preparo [modo de preparo], categoria, tempo_preparo [tempo de preparo], rendimento FROM churras_prato chu
LEFT JOIN funcionario_funcionario fun ON chu.funcionario_id = fun.id   
WHERE nome_prato LIKE '%fraldinha%'


--INSERT INTO churras_prato (nome_prato, ingredientes, modo_preparo, tempo_preparo, rendimento, categoria, date_prato) VALUES
--('Picanha', 'Picanha bovina, Sal Grosso', 'Temperar com sal grosso e grelhar ao ponto desejado.', 30, 3, 'Carne Vermelha', '2025-06-27 14:00:00');

--SELECT * FROM churras_prato
--WHERE nome_prato LIKE '%fraldinha%'
