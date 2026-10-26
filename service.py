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
        

        
async def add_item(name):
    try:
        conn = await connection_db()
        await conn.execute("""
        insert into items(name) values
        ($1)              
                    """,name)
        return True
        
    except Exception as Error:
        print(f"Add item Error: {Error}")
        return False
    finally:
        await conn.close()

