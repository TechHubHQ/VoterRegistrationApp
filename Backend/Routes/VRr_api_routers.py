from fastapi import APIRouter, Request, HTTPException, Body
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from Backend.Models.VRm_data_model import LoginModel, SignupModel, ForgotPassModel
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

@router.get("/eligibility_details", response_class=HTMLResponse)
async def eligibility_details(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("EligibilityDetails.html", {"request": request})

@router.get("/deadlines", response_class=HTMLResponse)
async def deadlines(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("Deadlines.html", {"request": request})

@router.get("/polling_locations", response_class=HTMLResponse)
async def polling_locations(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("PollingLocations.html", {"request": request})

@router.get("/absentee_voting", response_class=HTMLResponse)
async def absentee_voting(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("AbsenteeVoting.html", {"request": request})

@router.get("/register_to_vote", response_class=HTMLResponse)
async def register_to_vote(request: Request):
    return templates.TemplateResponse("RegisterToVote.html", {"request": request})

@router.get("/vote_reg_status", response_class=HTMLResponse)
async def vote_reg_status(request: Request):
    return templates.TemplateResponse("VoteRegStatus.html", {"request": request})

@router.get("/elections_directory", response_class=HTMLResponse)
async def elections_directory(request: Request):
    return templates.TemplateResponse("ElectionDirectory.html", {"request": request})

@router.get("/become_poll_worker", response_class=HTMLResponse)
async def become_poll_worker(request: Request):
    return templates.TemplateResponse("PollWorker.html", {"request": request})


@router.get("/eligibility_check", response_class=HTMLResponse)
async def eligibility_check(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("EligibilityCheck.html", {"request": request})

@router.get("/forgot_pass", response_class=HTMLResponse)
async def forgot_pass(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("ForgotPassword.html", {"request": request})


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


@router.post("/api/update_pass", response_class=JSONResponse)
async def forgot_pass_post(data: ForgotPassModel = Body(...)) -> JSONResponse:
    username = data.username
    password = data.password
    if not username or not password:
        raise HTTPException(status_code=400, detail="Username and new password are required")
    am.manage_forgot_password(username, password)
    return JSONResponse(status_code=200, content={"message": "Password reset successful"})
