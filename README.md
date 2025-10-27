# API Testing Framework

A comprehensive APB´ing framework built with FastAPI and PyTest. This project includes a simple User Management API and a robust test automation suite.

## Features

- **FastAPI Application**: User management with CRUD operations
- **PyTest Framework**: Comprehensive test suite
- **Docker Support**: Containerized deployment
- **Test Reporting**: HTML reports generation
- **Logging**: Comprehensive logging system
- **Configurable**: Environment based configuration

## Project Structure

```
api-testing-framework/
├── app/
│   ├── __init__.py
│   └── main.py
├── core/
│   ├── __init__.py
│   ├── api_client.py
│   ├── assertions.py
│   └── user_service.py
├── config/
│   ├── __init__.py
│   └── settings.py
├── data/
│   └── test_data.json
├── tests/
│   ├── __init__.py
│   └── test_user_crud.py
├── utils/
│   ├── __init__.py
│   ├── data_loader.py
│   └── logger.py
├── reports/
│   └── (empty - for generated reports)
├── conftest.py
├── pytest.ini
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── README.md
└── flow_diagram.png

```

## Getting Started

### Prerequisites

- Python 3.9+
- Docker & Docker Compose (optional)

### Installation

1. Clone the repository
```bash
git clone https://github.com/your_repo/api-testing-framework
cd api-testing-framework
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Copy environment variables
```bash
cp .env.example .env
```

### Running the API

**Locally**:
```bash
python app/main.py
```

**With Docker**:
```bash
docker-compose up api
```

API will be available at http://localhost:8000

### Running Tests

**Locally**:
```bash
pytest tests/ -v --html=reports/html/report.html --self-contained-html
```

**With Docker**:
```bash
docker-compose up tests
```

## API Endpoints

- `GET /` - Health check
- `POST /users/` - Create a new user
- `GET /users/` - Get all users
- `GET /users/{user_id}` - Get user by ID- `PUT /users/{user_id}` - Update user
- `DELETE /users/{user_id}` - Delete user

## Test Features

- **Smoke Tests**: Basic API functionality
â”API validation
- **Negative Testing**: Error handling
- **Data Driven**: JSON based test data
- **Reporting**: HTML test reports
- **Logging**: Comprehensive logging

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

This project is licensed under the MIT License.
