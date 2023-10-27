from fastapi import APIRouter

router = APIRouter(prefix='/auth', tags=['authentication', 'authorization'])


@router.post("/signin")
def signin():
    return {"message": "signin"}


@router.post('/signup')
def signup():
    return {"message": "signup"}


@router.get('/refresh')
def refresh():
    return {"message": "refresh"}
