from connection import *      
from datetime import *


async def get_user_by_id(user_id):
    try:
        conn = await connection_db()
        use = await conn.fetchrow("""
        select * from rentals where user_id = $1
                     """, str(user_id))
        return use
    except Exception as Error:
        print(f"Get user by id Error: {Error}")
    finally:
        await conn.close()
        

    