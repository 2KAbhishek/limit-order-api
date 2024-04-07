<div align = "center">

<h1><a href="https://github.com/2kabhishek/limit-order-api">limit-order-api</a></h1>

<a href="https://github.com/2KAbhishek/limit-order-api/blob/main/LICENSE">
<img alt="License" src="https://img.shields.io/github/license/2kabhishek/limit-order-api?style=flat&color=eee&label="> </a>

<a href="https://github.com/2KAbhishek/limit-order-api/graphs/contributors">
<img alt="People" src="https://img.shields.io/github/contributors/2kabhishek/limit-order-api?style=flat&color=ffaaf2&label=People"> </a>

<a href="https://github.com/2KAbhishek/limit-order-api/stargazers">
<img alt="Stars" src="https://img.shields.io/github/stars/2kabhishek/limit-order-api?style=flat&color=98c379&label=Stars"></a>

<a href="https://github.com/2KAbhishek/limit-order-api/network/members">
<img alt="Forks" src="https://img.shields.io/github/forks/2kabhishek/limit-order-api?style=flat&color=66a8e0&label=Forks"> </a>

<a href="https://github.com/2KAbhishek/limit-order-api/watchers">
<img alt="Watches" src="https://img.shields.io/github/watchers/2kabhishek/limit-order-api?style=flat&color=f5d08b&label=Watches"> </a>

<a href="https://github.com/2KAbhishek/limit-order-api/pulse">
<img alt="Last Updated" src="https://img.shields.io/github/last-commit/2kabhishek/limit-order-api?style=flat&color=e06c75&label="> </a>

<h3>Order Book API in Python 📈💰</h3>

</div>

limit-order-api is an api that provides order book functionality for trading.

- Easy to use REST API.
- OpenAPI documentation included.
- Easy setup and package management with Poetry.
- Implemented with Test Driven Development (>90% Coverage).
- Fast and powerful CI with GitHub actions.

## ⚡ Setup

### ⚙️ Requirements

- Python 3.10+
- [Poetry](https://python-poetry.org/docs/) (run `curl -sSL https://install.python-poetry.org | python3 -`)

### 💻 Setup

Setting up limit-order-api is as simple as cloning and running the server.

```bash
git clone https://github.com/2kabhishek/limit-order-api
cd limit-order-api

# install dependencies
poetry install

# database migrations
poetry run alembic upgrade head

# run tests
poetry run pytest

# run server
poetry run uvicorn limit_order_api.main:app --reload
# or
poetry run dev
```

The Open API documentation is available at `http://localhost:8000/docs` once the server is running.

## 🚀 Usage

### 📦 More Commands

```bash
# create a new migration
poetry run alembic revision --autogenerate -m "migration message"

# migration history
poetry run alembic history

# run tests with coverage
poetry run pytest --cov=limit_order_api
```

## 🏗️ What's Next

### ✅ To-Do

- [ ] Add a trade execution and publisher system as a separate service.
- [ ] Setup docker compose for easy deployment and testing.

## 🧑‍💻 Behind The Code

### 🌈 Inspiration

Learning more about trading systems and trying out some python libs.

### 💡 Challenges/Learnings

- FastAPI with Poetry, Alembic, and SQLAlchemy was interesting to setup.

### 🧰 Tooling

- [dots2k](https://github.com/2kabhishek/dots2k) — Dev Environment
- [nvim2k](https://github.com/2kabhishek/nvim2k) — Personalized Editor

<hr>

<div align="center">

<strong>⭐ hit the star button if you found this useful ⭐</strong><br>

<a href="https://github.com/2KAbhishek/limit-order-api">Source</a>
| <a href="https://2kabhishek.github.io/blog" target="_blank">Blog </a>
| <a href="https://twitter.com/2kabhishek" target="_blank">Twitter </a>
| <a href="https://linkedin.com/in/2kabhishek" target="_blank">LinkedIn </a>
| <a href="https://2kabhishek.github.io/links" target="_blank">More Links </a>
| <a href="https://2kabhishek.github.io/projects" target="_blank">Other Projects </a>

</div>
