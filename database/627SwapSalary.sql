update salary

# mudará sex quando sex for 'f' para 'm'
set sex = case when sex = 'f' then 'm'
# quando sex for 'm' mudará para 'f'
when sex = 'm' then 'f' 
end