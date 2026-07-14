# ADR-001: Fondazione tecnica di VoltyCode

- Stato: approvato
- Data: 2026-07-14

## Decisione

VoltyCode utilizza:

- Flutter per Windows e iOS
- FastAPI per il backend
- PostgreSQL e pgvector tramite Supabase
- Supabase Auth, Storage e Realtime
- Railway per il deployment del backend
- Redis per cache e attività asincrone
- GitHub Actions per integrazione continua

## Vincoli

Il client non comunica direttamente con i provider AI. Tutte le richieste passano
attraverso il backend e il futuro AI Gateway.

Le credenziali non devono essere committate nel repository.
