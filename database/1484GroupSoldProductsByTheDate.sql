

# seleciona sell_date e conta os produtos distintos como num_sold
select  sell_date, count(distinct product) as num_sold,
    # concatena cada produto desse dia em um grupo, separado por ',' como se fosse uma lista como products
	group_concat(distinct product order by product ASC separator ',') as products
    from activities

    # agrupa pelas datas
    GROUP BY sell_date;