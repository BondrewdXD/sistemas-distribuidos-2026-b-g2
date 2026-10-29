# Attack Surface Map - Telemed-IA

## 1. Data Flow Diagram

```mermaid
flowchart LR
    %% Usuarios
    U1[Paciente]
    U2[Médico]

    %% Fronteras y Componentes
    subgraph Internet ["TB1: Internet Zone"]
        App[Frontend Web/Mobile]
    end

    subgraph DMZ ["TB2: Gateway Zone"]
        GW[API Gateway]
    end

    subgraph Backend ["TB3: Backend Microservices Zone"]
        AuthSvc[Auth Service]
        ApptSvc[Appointment Service]
        MedSvc[Medical Service]
        AISvc[AI Agent Pre-consultation]
        NotifSvc[Notification Service]
    end

    subgraph DataStores ["TB4: Data Zone"]
        DB_User[(Patient DB)]
        DB_Med[(Medical DB)]
        DB_Appt[(Appointments DB)]
        MQ[(Message Broker)]
    end

    %% Flujos
    U1 -->|HTTPS| App
    U2 -->|HTTPS| App
    App -->|HTTPS / JWT| GW

    GW --> AuthSvc
    GW --> ApptSvc
    GW --> MedSvc
    GW --> AISvc

    AuthSvc -->|SQL| DB_User
    ApptSvc -->|SQL| DB_Appt
    MedSvc -->|SQL| DB_Med
    AISvc -->|API| MedSvc

    ApptSvc -->|AMQP| MQ
    MQ --> NotifSvc

    %% Destacar la frontera propia
    style DB_Med fill:#f96,stroke:#333,stroke-width:4px
    style MedSvc fill:#f96,stroke:#333,stroke-width:4px
```

**Note:** My claimed trust boundary is TB4 (Backend -> Database), specifically between the `Medical Service` and the `Medical DB`.

---

## 2. Asset Inventory

| Asset | Where it lives | Classification |
|---|---|---|
| Patient Vitals (HU-012, HU-014) | Medical  DB | Confidential |
| Medical Care Summary PDFs (HU-016) | Medical  DB | Confidential |
| Patient Credentials / Auth Tokens | Users DB | Restricted |
| Appointment Schedules | Appointments DB | Internal |
| AI Pre-consultation Symptoms (HU-006) | AI Service / Transit | Confidential |

---

## 3. Entry Points of My Boundary (Backend to Database)

| Entry Point | Type | Who calls it | Authentication Today |
|---|---|---|---|
| `GET /api/v1/medical/{id}/summary` | REST Endpoint | Medical Service | JWT (Gateway validates, service trusts) |
| `POST /api/v1/medical/vitals` | REST Endpoint | Medical Service | JWT (Gateway validates, service trusts) |
| `SELECT/INSERT` on `public` | Database Port (e.g., 5432) | Medical Service | DB User/Password via environment variables |