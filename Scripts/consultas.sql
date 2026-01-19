-- Todos os pedidos
SELECT * FROM operacao_shopee;

-- Pedidos em backlog
SELECT pedido_id, status, data_recebimento
FROM operacao_shopee
WHERE status = 'Backlog';

-- Ordenar por data
SELECT *
FROM operacao_shopee
ORDER BY data_recebimento;
