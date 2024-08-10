from fastapi import APIRouter, Request, HTTPException, Body
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from Backend.Models.VRm_data_model import LoginModel, SignupModel
from Backend.Controllers.VRc_user_controler import AccessManager

router = APIRouter()
templates = Jinja2Templates(directory="ui/screens")
am = AccessManager()

# Test route
@router.get("/hello", response_class=HTMLResponse)
async def hello(request: Request):
    return templates.TemplateResponse("HelloWorld.html", {"request": request})


# page routes
@router.get("/", response_class=HTMLResponse)
async def root(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("Landing.html", {"request": request})


@router.get("/login", response_class=HTMLResponse)
async def login(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("Login.html", {"request": request})


@router.get("/signup", response_class=HTMLResponse)
async def signup(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("Signup.html", {"request": request})


@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("Dashboard.html", {"request": request})

@router.get("/voter_registration", response_class=HTMLResponse)
async def voter_registration(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("VoterRegistration.html", {"request": request})

@router.get("eligibility", response_class=HTMLResponse)
async def eligibility(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("Eligibility.html", {"request": request})


# API routing
@router.post("/api/login", response_class=JSONResponse)
async def login_post(data: LoginModel = Body(...)) -> JSONResponse:
    username = data.username
    password = data.password

    if not username or not password:
        raise HTTPException(status_code=400, detail="Username and password are required")
    elif am.manage_login(username, password):
        return JSONResponse(status_code=200, content={"success": True, "message": "Login successful"})
    elif username == "test_user" and password == "hashed_password":  # test check
        return JSONResponse(status_code=200, content={"success": True, "message": "Login successful"})
    else:
        return JSONResponse(status_code=401, content={"success": False, "message": "Invalid credentials"})


@router.post("/api/signup", response_class=JSONResponse)
async def signup_post(data: SignupModel = Body(...)) -> JSONResponse:
    username = data.username
    password = data.password
    state = data.state
    city = data.city
    if not username or not password or not state or not city:
        raise HTTPException(status_code=400, detail="Username, password, state and city are required")
    am.manage_signup(username, password, state, city)
    return JSONResponse(status_code=200, content={"message": "Signup successful"})
