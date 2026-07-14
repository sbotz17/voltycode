# VoltyCode

VoltyCode è un workspace di sviluppo multipiattaforma assistito da AI, progettato
per Windows e iPhone.

## Componenti

- `apps/backend`: API FastAPI
- `apps/mobile`: applicazione Flutter
- `apps/dashboard`: dashboard futura
- `packages`: librerie condivise
- `infrastructure`: configurazioni cloud e deployment
- `docs`: documentazione tecnica

## Avvio backend

```bash
cd apps/backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
set -e

mkdir -p apps/backend/app/api/v1
mkdir -p apps/backend/app/core
mkdir -p apps/backend/app/db
mkdir -p apps/backend/tests
mkdir -p .github/workflows
mkdir -p docs/architecture

touch apps/backend/app/__init__.py
touch apps/backend/app/api/__init__.py
touch apps/backend/app/api/v1/__init__.py
touch apps/backend/app/core/__init__.py
touch apps/backend/app/db/__init__.py

cat > apps/backend/requirements.txt <<'EOF'
fastapi>=0.115,<1.0
uvicorn[standard]>=0.34,<1.0
sqlalchemy[asyncio]>=2.0,<3.0
asyncpg>=0.30,<1.0
pydantic-settings>=2.7,<3.0
alembic>=1.14,<2.0
httpx>=0.28,<1.0
python-jose[cryptography]>=3.3,<4.0
pytest>=8.3,<9.0
pytest-asyncio>=0.25,<1.0
ruff>=0.9,<1.0
