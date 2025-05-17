-- seed.sql

-- Clientes
INSERT INTO clientes (nome, email, cidade, saldo) VALUES
('Ana Souza', 'ana@gmail.com', 'São Paulo', 5000.00),
('Bruno Lima', 'bruno.lima@gmail.com', 'Rio de Janeiro', 1500.00),
('Carlos Pereira', 'carlosp@hotmail.com', 'Belo Horizonte', 800.00),
('Daniela Rocha', 'dani.rocha@outlook.com', 'Porto Alegre', 3200.00),
('Eduardo Gomes', 'eduardo.g@gmail.com', 'Curitiba', 10000.00);

-- Produtos
INSERT INTO produtos (nome, categoria, preco, estoque) VALUES
('Notebook', 'Eletrônicos', 3500.00, 10),
('Smartphone', 'Eletrônicos', 2500.00, 15),
('Fone de Ouvido', 'Acessórios', 200.00, 50),
('Mouse Wireless', 'Acessórios', 150.00, 30),
('Smartwatch', 'Eletrônicos', 1200.00, 20),
('Tablet', 'Eletrônicos', 1800.00, 12),
('Teclado Mecânico', 'Acessórios', 600.00, 10);

-- Transações
INSERT INTO transacoes (cliente_id, produto_id, data, quantidade) VALUES
(1, 1, '2024-01-10 10:00:00', 1),  -- Ana comprou Notebook
(1, 3, '2024-01-15 15:20:00', 2),  -- Ana comprou 2 Fones
(2, 2, '2024-02-01 11:30:00', 1),  -- Bruno comprou Smartphone
(3, 4, '2024-02-03 09:45:00', 1),  -- Carlos comprou Mouse
(4, 5, '2024-03-10 14:00:00', 1),  -- Daniela comprou Smartwatch
(4, 3, '2024-03-12 16:30:00', 1),  -- Daniela comprou Fone
(5, 6, '2024-04-05 17:15:00', 2),  -- Eduardo comprou 2 Tablets
(5, 7, '2024-04-07 13:00:00', 1);  -- Eduardo comprou Teclado
