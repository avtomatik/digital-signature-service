class FakeRedis:
    def __init__(self) -> None:
        self.store = {}

    async def set(self, k, v) -> None:
        self.store[k] = v

    async def get(self, k):
        return self.store.get(k, None)
