import json

import aio_pika

from app.core.config import settings


class RabbitMQService:
    def __init__(self, amqp_url: str):
        self.amqp_url = amqp_url
        self.connection = None
        self.channel = None

    async def connect(self):
        """Establish connection to RabbitMQ."""
        self.connection = await aio_pika.connect_robust(self.amqp_url)
        self.channel = await self.connection.channel()

    async def disconnect(self):
        """Close the connection to RabbitMQ."""
        if self.connection:
            await self.connection.close()

    async def publish_message(self, queue_name: str, message: dict):
        """Send a message to a specific queue."""
        if not self.channel:
            await self.connect()

        queue = await self.channel.declare_queue(  # noqa: F841
            queue_name, durable=True
        )
        message_body = aio_pika.Message(
            body=json.dumps(message).encode(),
            delivery_mode=2,  # persistent message
        )
        await self.channel.default_exchange.publish(
            message_body, routing_key=queue_name
        )

        print(f"Sent message to queue '{queue_name}': {message}")

    async def consume_messages(self, queue_name: str, callback):
        """Consume messages from a specific queue."""
        if not self.channel:
            await self.connect()

        queue = await self.channel.declare_queue(queue_name, durable=True)
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    await callback(message)


rabbitmq_service = RabbitMQService(settings.mq_url)
