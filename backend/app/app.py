from fastapi import FastAPI, UploadFile, HTTPException
import pandas as pd
from sklearn.linear_model import LinearRegression

def create_app() -> FastAPI:
    app = FastAPI()

    @app.post("/upload")
    async def upload_dataset(file: UploadFile):
        if not file.filename.endswith(".csv"):
            raise HTTPException(status_code=400, detail="Only CSV files allowed")

        df = pd.read_csv(file.file)
        return {"rows": len(df), "columns": list(df.columns)}

    @app.post("/run-model")
    async def run_model():
        model = LinearRegression()
        X = [[1], [2], [3]]
        y = [2, 4, 6]
        model.fit(X, y)

        return {
            "coef": model.coef_[0],
            "intercept": model.intercept_
        }

    return app
