from fastapi import WebSocket, WebSocketDisconnect
import numpy as np
import pandas as pd

df = pd.DataFrame(columns=["value"])

data_values = []

clients = []

async def send_statistics(websocket: WebSocket, df: pd.DataFrame):
    stats = {
        "mean": df['value'].mean(),
        "median": df['value'].median(),
        "std_dev": df['value'].std(),
        "percentiles": {
            "25th": df['value'].quantile(0.25),
            "50th": df['value'].quantile(0.5),
            "75th": df['value'].quantile(0.75),
        }
    }
    await websocket.send_json(stats)

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_json()
            value = data["value"]
            data_values.append(value)

            mean = np.mean(data_values)
            median = np.median(data_values)
            if len(data_values) > 1:
                std_dev = np.std(data_values, ddof=1)
            else:
                std_dev = 0

            percentiles = {
                "25th": np.percentile(data_values, 25),
                "50th": np.percentile(data_values, 50),
                "75th": max(data_values)
            }

            await websocket.send_json({
                "mean": mean,
                "median": median,
                "std_dev": std_dev,
                "percentiles": percentiles
            })
        except WebSocketDisconnect:
            break