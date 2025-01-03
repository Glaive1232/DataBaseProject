from fastapi import FastAPI
from routers import contractors, objects, customers

app = FastAPI()

# Подключение роутеров
app.include_router(contractors.router, prefix="/contractors", tags=["Contractors"])
app.include_router(objects.router, prefix="/objects", tags=["Construction Objects"])
app.include_router(customers.router, prefix="/customers", tags=["Customers"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

