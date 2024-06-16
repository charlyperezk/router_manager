from fastapi import FastAPI
import implementations.payment_methods as payment_methods


app = FastAPI()
app.include_router(payment_methods.route_manager.crud_route)
