# %%
import redis

# %%

class BidDataQueue:
    temp_db_name = "bid_queue"

    def __init__(self) -> None:
        self.r = redis.Redis(host="localhost", port=6379, db=0)

    def put(self, bid):
        """将 bid 添加到队列的右侧"""
        self.r.rpush(self.temp_db_name, bid)

    def get(self):
        """从队列的左侧提取并移除首个 bid"""
        bid = self.r.lpop(self.temp_db_name)

        if bid:
            return bid.decode()
        else:
            return None

    def remove(self, bid):
        """从队列中移除指定 bid"""
        self.r.lrem(self.temp_db_name, 0, bid)

    def get_all(self):
        """ 获取队列中所有元素 """
        bid_list = self.r.lrange(self.temp_db_name, 0, -1)
        return [bid.decode() for bid in bid_list]

    def is_in(self, bid):
        """ 判断某 bid 是否已在队列中 """
        bid_list = self.r.lrange(self.temp_db_name, 0, -1)
        return bid.encode("utf-8") in bid_list

    def __exit__(self, type, value, traceback):
        self.r.close()
        return False
    


# %%

bdq = BidDataQueue()

# %%

r = redis.Redis(host="localhost", port=6379, db=0)
temp_db_name = "bid_queue"

r.bgsave()
