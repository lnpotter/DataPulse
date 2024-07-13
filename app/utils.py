import matplotlib.pyplot as plt
import io
import base64

def create_graph(df, graph_type):
    plt.figure(figsize=(10, 5))
    
    if graph_type == "bar":
        df.plot(kind='bar', x='label', y='value', legend=False)
    elif graph_type == "line":
        df.plot(kind='line', x='label', y='value', legend=False)
    elif graph_type == "pie":
        df.plot(kind='pie', y='value', labels=df['label'], autopct='%1.1f%%')
    else:
        raise ValueError("Invalid graph type.")

    plt.title('Value Chart')
    plt.xlabel('Label')
    plt.ylabel('Value')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    
    return base64.b64encode(buf.read()).decode('utf-8')
