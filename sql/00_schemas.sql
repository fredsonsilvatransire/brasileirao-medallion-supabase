-- Arquitetura medalhão: um schema por camada.
create schema if not exists bronze;  -- dado bruto (texto), + metadados de carga
create schema if not exists silver;  -- dado tipado, limpo e modelado (dimensões e fatos)
create schema if not exists gold;    -- tabelas/visões prontas para o dashboard

-- Dashboard lê a Gold ao vivo pela Data API com a chave anon (somente leitura).
-- Bronze e Silver NÃO recebem grant para anon/authenticated.
grant usage on schema gold to anon, authenticated;
alter default privileges in schema gold grant select on tables to anon, authenticated;
-- Obs.: cada tabela da Gold deve ter RLS habilitado + policy de SELECT (criadas junto com as tabelas).
