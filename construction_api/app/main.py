from fastapi import FastAPI
from routers import contractors, objects, customers
from Tasks import complex_rest_api

app = FastAPI()

# Подключение роутеров
app.include_router(contractors.router, prefix="/contractors", tags=["Contractors"])
app.include_router(objects.router, prefix="/construction_objects", tags=["Construction Objects"])
app.include_router(customers.router, prefix="/customers", tags=["Customers"])

app.include_router(complex_rest_api.router, prefix="/advanced", tags=["Advanced Operations"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

