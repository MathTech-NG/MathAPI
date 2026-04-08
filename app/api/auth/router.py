from fastapi import APIRouter

from app.api.auth.schemas import AuthResponse, LoginRequest, RegisterRequest

router = APIRouter(prefix="/v1/auth", tags=["auth"])


@router.post("/register", response_model=AuthResponse)
def register(payload: RegisterRequest) -> AuthResponse:
    return AuthResponse(message=f"Registered {payload.email}")


@router.post("/login", response_model=AuthResponse)
def login(payload: LoginRequest) -> AuthResponse:
    return AuthResponse(message=f"Logged in {payload.email}")
