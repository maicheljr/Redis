from datetime import datetime
from models.connection.redis_connection import RedisConnectionHandle
from models.redis_repository import RedisRepository
from configs.start_form import start_form



######################################################
# 1. Conectar ao banco de dados e buscar elementos

redis_conn = RedisConnectionHandle().connect()
redis_repository = RedisRepository(redis_conn)

data_atual = datetime.now()
data_formatada = data_atual.strftime('%Y-%m-%d')

## frutaas e prommoção
# redis_repository.insert_hash(data_formatada,"banana", 3.12)
# redis_repository.insert_hash(data_formatada,"morango", 312)
# redis_repository.insert_hash(data_formatada,"uva", 12.12)
hash_items = redis_conn.hgetall(data_formatada)
print(hash_items)

######################################################
# 2. Carregar dados ao formulario
python_dict = {}
for key, value in hash_items.items():
    python_dict[key.decode('utf-8')] = value.decode('utf-8')

print(python_dict)
start_form.load_info(python_dict)
#######################################################
# 3. Utilizar valor armazenado -> Ligar API

value = start_form.get_info('uva')
value2 = start_form.get_info('banana')
print(value)
print(value2)
