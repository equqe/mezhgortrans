import hashlib
import hmac
import logging

from data.buttons import WRITE_ADDRESS


def location_check(func):
    async def decorator(message, state=None):
        if not message.location:
            await message.answer(
                "В данный момент вы должны отправить геопозицию. "
                f"Только так мы можем с точностью определить ваше местоположение.\n\nВы можете нажать на кнопку «{WRITE_ADDRESS}» и ввести адрес вручную 😉"
            )
            return
        return await func(message, state)

    return decorator
