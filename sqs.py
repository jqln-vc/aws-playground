import boto3

# usando o boto3 com o Amazon SQS (Simple Queue Service)

# obtendo o recurso SQS
sqs = boto3.resource('sqs')

# iterando sobre as filas existentes
def get_all_queues():
    print("Listando todas as filas:")
    queues = [queue.url for queue in sqs.queues.all()]
    for queue in queues:
        print(queue)
    
    return queues

queues_urls = get_all_queues()


# acessando uma fila
fila = sqs.get_queue_by_name(QueueName='Fila.fifo')
print(fila)

# enviando um batch de mensagens | lista com JSON
response = fila.send_message(
    MessageBody='Testando',
    MessageDeduplicationId='001',
    MessageGroupId='123',
    MessageAttributes={
        'Author': {
            'StringValue': 'jqln-vc',
            'DataType': 'String'
        }
    }
)

print(response)





