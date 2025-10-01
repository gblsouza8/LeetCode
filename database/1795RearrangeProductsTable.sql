# seleciona o id do produto
# em todas as linhas onde encontrar o id do produto adiciona a coluna 'store' com a string definida (store1,2,3)
# pega o valor que estava nos "stores" como price
# usando union all para fazer isso com as três colunas

select 
	product_id,
	'store1' as store,
    store1 as price
from products where store1 is not null
union all
select
	product_id,
    'store2' as store,
    store2 as price
from products where store2 is not null
union all
select
	product_id,
	'store3' as store,
    store3 as price
from products where store3 is not null
order by product_id;