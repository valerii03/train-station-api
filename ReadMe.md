# 🚆 Train Station API

Train Station API is a Django REST Framework project for managing railway stations, routes, trains, journeys, crews, and ticket orders.

The API allows authenticated users to book train tickets and manage their own orders while administrators can manage the railway system through the API and Django Admin.

---

# Features

- JWT Authentication
- User registration
- User profile management
- Admin panel
- CRUD operations for:
  - Stations
  - Routes
  - Train Types
  - Trains
  - Crew members
  - Journeys
  - Orders
  - Tickets
- Users can access only their own orders
- Search support
- Pagination
- Swagger/OpenAPI documentation
- Ticket validation

---

# Technologies

- Python 3.12
- Django
- Django REST Framework
- Simple JWT
- drf-spectacular
- SQLite
- Django Filter

---

# Installation

Clone repository

```bash
git clone https://github.com/valerii03/train-station-api.git
cd train-station-api
```

Create virtual environment

```bash
python -m venv .venv
```

Activate virtual environment

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Apply migrations

```bash
python manage.py migrate
```

Create superuser

```bash
python manage.py createsuperuser
```

Run server

```bash
python manage.py runserver
```

---

# Authentication

Register

```
POST /api/user/register/
```

Get JWT Token

```
POST /api/user/token/
```

Request body

```json
{
    "username": "admin",
    "password": "your_password"
}
```

Response

```json
{
    "refresh": "...",
    "access": "..."
}
```

Use token

```
Authorization: Bearer <access_token>
```

---

# API Endpoints

## Stations

```
/api/station/stations/
```

## Routes

```
/api/station/routes/
```

## Train Types

```
/api/station/train-types/
```

## Trains

```
/api/station/trains/
```

## Crew

```
/api/station/crew/
```

## Journeys

```
/api/station/journeys/
```

## Orders

```
/api/station/orders/
```

---

# API Documentation

Swagger UI

```
/api/doc/
```

OpenAPI Schema

```
/api/schema/
```

---

# Project Structure

```
train_station/
│
├── accounts/
├── station/
├── train_station/
├── manage.py
├── requirements.txt
└── README.md
```

---

# Database

The project contains models for:

- User
- Station
- Route
- TrainType
- Train
- Crew
- Journey
- Order
- Ticket

A database diagram is attached to the Pull Request.

---

# Permissions

Anonymous users:

- Read public data

Authenticated users:

- Create and manage their own orders

Admin users:

- Full CRUD access

---

# Author

Valerii Ivasyk

GitHub:

https://github.com/valerii03