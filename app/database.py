from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

DATABASE_URL = "postgresql+asyncpg://ivan:2002@localhost/tareas_db"

engine = create_async_engine(DATABASE_URL, echo=True)

# Para sesiones asíncronas, es decir que no bloquean la ejecución
SessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
