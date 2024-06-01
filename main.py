#from fastapi import FastAPI
import fastapi
app = fastapi.FastAPI()

@app.get('/hello/{name}')
def get_hello(name: str):
    #return "hello "+name
    return {"name":name}

@app.delete("/delete")
def delete_data():
    return {"status":'deleted successfully'}

@app.delete("/delete/{name}/{age}")
def delete_name(name, age):
    return{"Status": "deleted: "+name, "age":age, "code":200}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app, host="0.0.0.0", port=8082)



    