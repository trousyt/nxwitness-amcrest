from amcrest import AmcrestCamera, AmcrestError
from datetime import datetime, timezone
import asyncio
import os


def log(msg, level='INFO'):
    ts = datetime.now(timezone.utc).strftime('%d/%m/%Y %H:%M:%S')
    print(f'{ts} [{level}] {msg}')


camera = AmcrestCamera('192.168.4.74', 80, 'admin', 'testing123').camera
camera.software_information
camera.device_type.replace('type=', '').strip()


async def main():
    try:
        async for code, payload in camera.async_event_actions('All'):
            log(f'Code {code}: {str(payload)}')
            # break

    except AmcrestError as error:
        log(f'Amcrest error: {error}', level='ERROR')
        os._exit(1)

asyncio.run(main())
