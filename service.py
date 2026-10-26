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



async def get_items():
    try:
        conn = await connection_db()
        data = await conn.fetch("""
        select * from items
        where is_rented = false;
                        """,)
        return data
    except Exception as Error:
        print(f"Get item Error: {Error}")
        return False
    finally:
        await conn.close()
        
        
async def rent(item_id, user_id):
    try:
        conn = await connection_db()
        item = await conn.fetchrow("""
            select * from items
            where id = $1 and is_rented = false
        """, item_id)
        if not item:
            return False
        rented_at = datetime.now()
        due_date = rented_at + timedelta(days=7)

        await conn.execute("""
            insert into rentals (user_id, item_id, rented_at, due_date)
            values ($1, $2, $3, $4)
        """, user_id, item_id, rented_at, due_date)

        await conn.execute("""
            update items
            set is_rented = true
            where id = $1
        """, item_id)

        return True

    except Exception as Error:
        print(f"Rent item Error: {Error}")
        return False

    finally:
            await conn.close() 
            
