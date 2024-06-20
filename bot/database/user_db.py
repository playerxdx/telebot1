import motor.motor_asyncio
from info import DATABASE_URL

class Database:
    
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users
        self.config_col  = self.db.config
        
    def new_user(self, id, name):
        return dict(
            id=id,
            name=name,
            message_count = None,
            is_ban = False
        )
    
    async def add_user(self, id, name):
        user = self.new_user(id, name)
        await self.col.insert_one(user)
    
    async def is_user_exist(self, id):
        user = await self.col.find_one({'id': int(id)})
        return bool(user)
   
    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count
    
    async def get_all_users(self):
        return self.col.find({})
    
    async def delete_user(self, user_id):
        await self.col.delete_many({'id': int(user_id)})   

    def create_config_data(
            self,
            afk_status=False,
            last_seen=False):
        
        return  {
            'afk_status': afk_status,
            'last_seen': last_seen
        }
    
    async def update_config_value(self, key, value):
        try:
            await self.config_col.update_one({}, {'$set': {key: value}}, upsert=True)

        except Exception as e:
            print(f"An error occurred: {e}")

    async def get_config_value(self, key):
        configuration = await self.config_col.find_one({})
        if not configuration:
            await self.config_col.insert_one(self.create_config_data())
            configuration = await self.config_col.find_one({})
        return configuration.get(key, False)
        
db = Database(DATABASE_URL, "Telebot")