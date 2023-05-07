from fastapi import FastAPI
import uvicorn
import functions as ts
from statics import *

app = FastAPI()


@app.get("/product_recomendations/{gender}/{age}")
def get_recomendations(gender: GenderEnum, age: AgeEnum):
    return {"message": ts.age_plus_gender_recommendations(genders[gender], ages[age])}

@app.get("/product_recomendations/{category}")
def get_recomendations(category: CategoryEnum):
    return {"message": ts.product_category_recomendations(categories[category])}


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)