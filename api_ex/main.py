from fastapi import FastAPI,Query
import user
import item

app = FastAPI()

app.include_router(user.router)
app.include_router(item.router)