#from fastapi import FastAPI
import fastapi
app = fastapi.FastAPI()

@app.get('/hello/{name}')
def get_hello(name: str):
    #return "hello "+name
    return {"name":name}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app, host="0.0.0.0", port=8082)

    