from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse, StreamingResponse
from .models import DataPoint
from .utils import create_graph
import pandas as pd
import io
import base64

router = APIRouter()

@router.post("/upload-data/")
async def upload_data(data: list[DataPoint]):
    df = pd.DataFrame([d.model_dump() for d in data])
    mean_value = df['value'].mean()
    
    return {"mean": mean_value}

@router.post("/get-graph/")
async def get_graph(data: list[DataPoint], graph_type: str = "bar"):
    df = pd.DataFrame([d.model_dump() for d in data])
    
    try:
        img_base64 = create_graph(df, graph_type)
        image_bytes = base64.b64decode(img_base64)
        return StreamingResponse(io.BytesIO(image_bytes), media_type="image/png", headers={"Content-Disposition": "attachment; filename=graph.png"})
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/export-data/")
async def export_data(data: list[DataPoint], format: str = "csv"):
    df = pd.DataFrame([d.model_dump() for d in data])
    
    if format == "csv":
        output = io.StringIO()
        df.to_csv(output, index=False)
        output.seek(0)  # Reset buffer position
        return StreamingResponse(io.StringIO(output.getvalue()), media_type="text/csv", headers={"Content-Disposition": "attachment; filename=data.csv"})
    
    elif format == "json":
        return JSONResponse(content=df.to_dict(orient="records"), headers={"Content-Disposition": "attachment; filename=data.json"})
    
    else:
        raise HTTPException(status_code=400, detail="Invalid format. Use 'csv' or 'json'.")

@router.post("/statistics/")
async def calculate_statistics(data: list[DataPoint]):
    df = pd.DataFrame([d.model_dump() for d in data])
    
    statistics = {
        "mean": df['value'].mean(),
        "median": df['value'].median(),
        "std_dev": df['value'].std(),
        "percentiles": {
            "25th": df['value'].quantile(0.25),
            "50th": df['value'].quantile(0.5),
            "75th": df['value'].quantile(0.75),
        }
    }
    
    return statistics
