from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.concurrency import run_in_threadpool

import to_markdown
from resume_extractor import extract_resume
from resume_schema import ResumeData
app = FastAPI()

@app.post("/Upload", response_model=ResumeData) #file upload and covert to markdown endpoint

async def parseResume(file: UploadFile = File(...)):    
    """Raw bytes cannot be passed as input for docling DocumentConverter """
    inputfile = await file.read()
    output ={}
    try:
        output = await run_in_threadpool (
            to_markdown.fileconverter,
            inputfile,
            file.filename
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File conversion failed: {e}") 
    finally:
        await file.close()
    try:
        structured_data = await run_in_threadpool(extract_resume, output)
        return structured_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Information extraction failed: {e}")