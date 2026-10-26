from dotenv import load_dotenv
import asyncpg
import os

load_dotenv()
pasw  = os.getenv("PASSWORD_DB")


async def connection_db():
    try:
        conn = await asyncpg.connect(
            host="localhost",
            port=5432,
            user="postgres",
            database="exam_db",
            password=pasw
        )
        return conn
    except Exception as Error:
        print(f"Connection Error: {Error}")
        
        
async def create_table():
    try:
        conn = await connection_db()
        await conn.execute("""
Create table if not exists items (
    id serial primary key,
    name varchar(200),
    is_rented boolean default false,
    created_at timestamp default now()
);
    
Create table if not exists rentals (
    id serial primary key,
    user_id bigint,
    item_id int references items(id),
    rented_at timestamp,
    due_date timestamp,
    returned_at timestamp,
    late_fee int default 0
)
""")
        print("Table created")
    except Exception as Error:
        print(f"Create Error: {Error}")
    finally:
        await conn.close()
        