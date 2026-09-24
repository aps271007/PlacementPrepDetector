from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.concurrency import run_in_threadpool

import document_reader
app = FastAPI()

@app.post("/Upload") #file upload and covert to markdown endpoint

async def parseResume(file: UploadFile = File(...)):    
    """Raw bytes cannot be passed as input for docling DocumentConverter """
    inputfile = await file.read()
    output ={}
    output = await run_in_threadpool (
        document_reader.fileconverter,
        inputfile,
        file.filename
    )
    await file.close()
    return {"filename": file.filename, "data": output}