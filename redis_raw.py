''' Comandos Redis Básicos '''
import redis

redis_connection = redis.Redis(host='localhost', port=6379, db=0)

# Chave Valor
redis_connection.set('chave1','valor1')
valor = redis_connection.get('chave1').decode("utf-8")
redis_connection.delete('chave1')

# Hash
redis_connection.hset('meu_hash','nome','maichel')
redis_connection.hset('meu_hash','idade',39)
redis_connection.hset('meu_hash','cidade','passo fundo')
nome = redis_connection.hget('meu_hash','nome').decode("utf-8")
redis_connection.hdel('meu_hash','cidade')

# Exists
chave1 = redis_connection.exists('chave1')
hash_key = redis_connection.exists('meu_hash')
field_key = redis_connection.hexists('meu_hash', 'nome')

print(chave1)
print(hash_key)
print(field_key)
