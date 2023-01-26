from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from weasyprint import HTML, CSS, Attachment, default_url_fetcher
from fastapi.responses import FileResponse
from datetime import datetime
from .utils.request_utility import RequestUtility
import io
from .routers.cv_router import cv_router

app = FastAPI()

file_path = f'app/temp/warranty.pdf'

templates = Jinja2Templates(directory="app/templates")

app.include_router(cv_router)

@app.get("/root")
async def root():
    return {"message": "Hello World"}   

# @app.get("/")
# async def cv(request: Request):
#     temp_file_path = file_path
#     url = request.base_url._url
#     css = RequestUtility.get_static_base_url(request)+"styles.css"
#     css = CSS(filename='app/static/styles.css')
#     image = Attachment(filename='app/static/profile.jpg')
#     res = templates.TemplateResponse("cv.html", {"request": request,'url': url, 'css': css})
#     html = HTML(string=res.body.decode("utf-8"))    
#     pdf = html.write_pdf(temp_file_path)
#     return FileResponse(temp_file_path, filename = f"Warranty.pdf", media_type="application/pdf")


# @app.get("/asd")
# def get_warranty(request: Request):

#   file_path = f'app/temp/cv.pdf'  
#   logo_pes = RequestUtility().get_static_base_url(request) + "logo_pes.png"
#   css = RequestUtility().get_static_style_base_url(request) + "style_warranty.css"
#   res = templates.TemplateResponse("cv.html", {"request": request,"logo_pes": logo_pes, 'css': css })
#   html = HTML(string=res.body.decode("utf-8"))    
#   html.write_pdf(file_path)
#   return FileResponse(file_path, filename = f"CV.pdf", content_disposition_type="inline")

app.mount("/static", StaticFiles(directory="app/static"), name="static")