import os, pickle, time, aiofiles


class AsyncRateLimiter:
    def __init__(self, storage_file="swibots.pkl"):
        self.storage_file = storage_file
        self.rate_limit_data = {}

    async def _load_data(self):
        if os.path.exists(self.storage_file):
            async with aiofiles.open(self.storage_file, "rb") as f:
                content = await f.read()
                self.rate_limit_data = pickle.loads(content)

    async def _save_data(self):
        async with aiofiles.open(self.storage_file, "wb") as f:
            await f.write(pickle.dumps(self.rate_limit_data))

    def limit(self, key: str, times: int, seconds: int):
        def decorator(func):
            async def async_wrapper(*args, **kwargs):
                current_time = time.time()

                await self._load_data()

                if key not in self.rate_limit_data:
                    self.rate_limit_data[key] = []

                self.rate_limit_data[key] = [
                    t for t in self.rate_limit_data[key] if current_time - t < seconds
                ]

                if len(self.rate_limit_data[key]) >= times:
                    raise RateLimitException(
                        f"Rate limit exceeded: {times} calls in {seconds} seconds"
                    )

                # Record the call
                self.rate_limit_data[key].append(current_time)
                await self._save_data()
                return await func(*args, **kwargs)

            return async_wrapper

        return decorator


class RateLimitException(Exception):
    pass
