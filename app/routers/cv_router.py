from datetime import datetime
import os
from fastapi import APIRouter, BackgroundTasks, Depends, Form,  Header,  Request, Response, HTTPException
from fastapi.security.api_key import APIKey
from fastapi.templating import Jinja2Templates
from fastapi import status
from weasyprint import HTML
from fastapi.responses import FileResponse
from ..utils.request_utility import RequestUtility

cv_router = APIRouter(
  prefix="/cv",
  tags=["CV"],
  responses={404: {"description": "Not found"}}
)

templates = Jinja2Templates(directory="app/templates")

def clear_file(file_paths: None):
  for file_path in file_paths:
    os.remove(file_path)

@cv_router.get("/")
def get_warranty(request: Request, background_tasks: BackgroundTasks):

  file_path = f'app/temp/warranty_{datetime.now()}.pdf'
  temp_file = [file_path]
  barcode_path: str = ""
  
  logo_pes = RequestUtility().get_static_base_url(request) + "profile5.jpg"
  css = RequestUtility().get_static_style_base_url(request) + "style_warranty.css"
  res = templates.TemplateResponse("cv.html", {"request": request,"logo_pes": logo_pes, 'css': css })
  html = HTML(string=res.body.decode("utf-8"))
  html.write_pdf(file_path)
  background_tasks.add_task(clear_file, temp_file)
  return FileResponse(file_path, filename = f"CV_{datetime.now()}.pdf", content_disposition_type='inline')
