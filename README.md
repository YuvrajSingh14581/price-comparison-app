ProPrice — Full-Stack Price Comparison App

ProPrice is a self-contained full-stack price comparison application built for the Stage 2 take-home assignment.

A signed-in user can search for something they want to buy, compare normalized prices across multiple mocked sources, identify the cheapest deal, see the best way to pay using seeded card reward rates, and save comparisons securely to their own account.

No real retailer integrations are required. The application uses a small seeded/mock dataset as specified by the assignment.

✨ Features

Price comparison

Search for a product/category such as groceries

Returns normalized deals from 3–4 mocked sources

Shows:

Store/source

Product name

Current price

Original price

Currency

Availability

Product URL

Automatically identifies and highlights the cheapest deal

Best way to pay

The backend contains a small seeded list of cards and reward rates.

For every available deal, the application calculates:

Savings = deal price × reward rate
Effective price = deal price − savings

The option with the lowest effective price is returned as the single Best way to pay recommendation.

Authentication

Email/password registration

Email/password login

Password hashing

JWT-based authentication

Authenticated /auth/me endpoint

Protected API requests

Saved comparisons

Signed-in users can save a comparison

Users can list their saved comparisons

Ownership is enforced by the backend using the authenticated user's ID

A user cannot access another user's saved comparisons

UI states

The frontend is designed to handle:

Loading

Error

Empty results

Input validation

Search results

Saved comparisons

🏗️ Tech Stack

Frontend

React

Vite

TypeScript

Tailwind CSS

Backend

Python

FastAPI

SQLAlchemy

Pydantic

JWT authentication

pwdlib / Argon2 password hashing

Database

PostgreSQL

psycopg2-binary

📁 Project Structure

price-comparison-app/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   │
│   │   ├── db/
│   │   │   ├── base.py
│   │   │   ├── database.py
│   │   │   └── init_db.py
│   │   │
│   │   ├── models/
│   │   │   ├── product.py
│   │   │   ├── store.py
│   │   │   ├── price.py
│   │   │   ├── price_history.py
│   │   │   ├── user.py
│   │   │   └── comparison.py
│   │   │
│   │   ├── routes/
│   │   │   ├── products.py
│   │   │   ├── stores.py
│   │   │   ├── prices.py
│   │   │   ├── deals.py
│   │   │   ├── auth.py
│   │   │   └── comparisons.py
│   │   │
│   │   ├── schemas/
│   │   └── services/
│   │
│   ├── create_tables.py
│   ├── requirements.txt
│   └── .env
│
└── frontend/
    ├── src/
    ├── public/
    ├── package.json
    └── ...

🚀 Getting Started

1. Clone the repository

git clone https://github.com/YuvrajSingh14581/price-comparison-app.git
cd price-comparison-app

Backend Setup

2. Open the backend

cd backend

3. Create and activate a virtual environment

Windows PowerShell

python -m venv venv
.\venv\Scripts\Activate.ps1

If the virtual environment already exists:

.\venv\Scripts\Activate.ps1

macOS/Linux

python3 -m venv venv
source venv/bin/activate

4. Install dependencies

pip install -r requirements.txt

The backend uses FastAPI, SQLAlchemy, PostgreSQL, JWT, and password hashing dependencies.

5. Configure environment variables

Create:

backend/.env

Example:

DATABASE_URL=postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/price_comparison

JWT_SECRET_KEY=replace-with-a-long-random-secret
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=60

Environment variables

Variable

Purpose

DATABASE_URL

PostgreSQL database connection

JWT_SECRET_KEY

Secret used to sign JWT access tokens

JWT_ALGORITHM

JWT signing algorithm

JWT_ACCESS_TOKEN_EXPIRE_MINUTES

Access-token lifetime

Never commit real secrets or passwords to GitHub.

6. Create the database

Create a PostgreSQL database matching the name in DATABASE_URL.

For example:

CREATE DATABASE price_comparison;

Make sure PostgreSQL is running before starting the backend.

7. Create database tables

From the backend directory:

python create_tables.py

Expected output:

Database tables created successfully!

The application creates tables for:

Users

Products

Stores

Prices

Price history

Saved comparisons

8. Start the FastAPI server

From backend:

uvicorn app.main:app --reload

The API will normally be available at:

http://127.0.0.1:8000

FastAPI's interactive API documentation is available at:

http://127.0.0.1:8000/docs

🔐 Authentication Flow

The application uses JWT bearer authentication.

Register

POST /auth/register

Example request:

{
  "email": "user@example.com",
  "password": "your-password"
}

The response contains an access token and user information.

Login

POST /auth/login

Example:

{
  "email": "user@example.com",
  "password": "your-password"
}

Use the returned token for protected endpoints:

Authorization: Bearer <access_token>

Current user

GET /auth/me

The backend obtains the user ID from the JWT rather than trusting a user ID supplied by the client.

🔎 Deal Search

The deal search endpoint uses a seeded/mock dataset representing multiple sources.

Example:

GET /deals/search?q=groceries

The response contains normalized deals and identifies:

cheapest_deal
best_payment

Example concept:

Amazon       ₹1050
Flipkart      ₹996  ← cheapest
Blinkit      ₹1020
Zepto        ₹1010

If a reward card makes another option cheaper after rewards, the backend returns that option as the best way to pay.

Example:

Flipkart + HDFC Millennia Card
Normal price:    ₹996.00
Reward:           5%
Savings:         ₹49.80
Effective price: ₹946.20

💾 Saved Comparisons

Saved comparisons are associated with the authenticated user.

The ownership model is:

JWT
 ↓
authenticated user
 ↓
current_user.id
 ↓
Comparison.user_id

The backend filters saved comparisons using the authenticated user's identity.

This prevents a user from simply changing a user_id query parameter to access another user's data.

📡 Main API Areas

Area

Purpose

/auth/register

Create an account

/auth/login

Sign in

/auth/me

Get current authenticated user

/products

Product management/search

/stores

Store/source management

/prices

Price management

/deals/search

Search normalized mocked deals

/comparisons

Save/list authenticated user's comparisons

For the complete interactive API, run the backend and open:

http://127.0.0.1:8000/docs

🎨 Frontend Setup

From the project root:

cd frontend

Install dependencies:

npm install

Start the Vite development server:

npm run dev

The frontend will display the local development URL provided by Vite.

If the frontend uses a configurable API URL, set it in the frontend environment file according to the variable expected by the current Vite configuration.

The frontend communicates with the FastAPI backend running on port 8000.

🧪 Suggested Manual Test Flow

After starting both frontend and backend:

1. Create an account

Register with a new email and password.

2. Sign in

Login using the same credentials.

3. Search

Search for:

groceries

4. Verify deals

Confirm that multiple mocked sources are displayed.

5. Verify cheapest deal

The cheapest result should be clearly highlighted.

6. Verify best payment

Confirm that a single best payment recommendation is shown with the effective price.

7. Save the comparison

Save the current comparison while authenticated.

8. View saved comparisons

Confirm that the saved comparison appears for the current user.

9. Ownership test

Create/login as a second user and confirm that the first user's saved comparisons are not visible.

10. Authentication test

Try accessing protected endpoints without a token and confirm that the API rejects the request.

🎯 Assignment Requirements Coverage

Requirement

Implementation

Search normalized results

Mocked deal search in FastAPI

At least 3 sources

Amazon, Flipkart, Blinkit, Zepto

Cheapest highlighted

Backend calculates cheapest deal

Best way to pay

Seeded card/reward calculation

Save comparison

Comparison model + protected endpoint

Own saved comparisons only

user_id derived from JWT

Email sign-in

Register/login endpoints

Strict ownership

Backend authorization

Validation

Pydantic/FastAPI validation

Loading/error/empty states

Frontend state handling

Responsive UI

React/Tailwind implementation

README

This document

🧠 Design Decisions & Tradeoffs

Mocked retailer data

Real retailer APIs were intentionally not integrated because the assignment explicitly requires a self-contained application with a seeded dataset.

This keeps the project deterministic and easy to run and evaluate.

JWT authentication

JWT bearer tokens provide a simple stateless authentication mechanism suitable for this take-home application.

Password hashing

Passwords are never stored directly. Only password hashes are persisted in PostgreSQL.

Backend ownership enforcement

Ownership is enforced on the backend instead of relying on frontend filtering. The authenticated user's identity is obtained from the JWT.

Seeded rewards

Card reward rates are intentionally small and deterministic. This makes the "best way to pay" calculation easy to understand and test.

SQLAlchemy

SQLAlchemy provides the database abstraction and keeps the data model separated from the API layer.

🔒 Security Notes

Before production deployment:

Use a strong randomly generated JWT secret.

Never commit .env files containing real credentials.

Restrict CORS to trusted frontend origins.

Use HTTPS.

Add rate limiting for authentication endpoints.

Add database migrations such as Alembic instead of relying on table creation for schema changes.

Store tokens using a production-appropriate authentication strategy.

📌 Development Notes

This project intentionally keeps the architecture small:

React frontend
      ↓
FastAPI API
      ↓
SQLAlchemy
      ↓
PostgreSQL

The backend is separated into:

routes → API endpoints
schemas → request/response validation
models → database models
services → business logic
core → configuration/security
db → database setup

This structure keeps authentication, database access, and deal/reward logic separated without introducing unnecessary infrastructure.

👨‍💻 Author

Yuvraj Singh

B.Tech — Computer Science & Engineering
GLA University

GitHub: YuvrajSingh14581

📄 License

This project was created as a take-home assignment / demonstration project.
