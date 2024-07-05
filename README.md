# Router Manager -- FastAPI Dynamic CRUD Creator

This project implements a dynamic CRUD endpoint creator for web applications using FastAPI. It allows easily creating CRUD (Create, Read, Update, Delete) operations for different data entities efficiently and scalably.

## Features

- **Modular Design:** Uses modular classes and functions to dynamically generate CRUD routes.
- **Data Validation:** Utilizes Pydantic to define data schemas and validate inputs and outputs.
- **Exception Handling:** Implements structured exception handling to ensure consistent and appropriate responses to errors.
- **Secure Transactions:** Manages database transactions securely with SQLAlchemy.
- **Monitoring and Control:** Uses asynchronous functions and supervision to optimize CRUD operation performance.

## Example:

<img width="893" alt="Captura de pantalla 2024-06-29 170600" src="https://github.com/charlyperezk/router_manager/assets/118618975/d54480dd-fe50-4e89-b786-5d5bb01493c3">

### Team Crud Route Created

## Requirements

- Python 3.7 or higher
- Dependencies listed in `requirements.txt`

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/charlyperezk/router_manager
   cd router_manager

2. Install dependencies:

    pip install -r requirements.txt

3. Configure db:

    - Ensure you have an SQLite database or modify examples/database.py to suit your database environment.
    

4. Run the application:

    uvicorn main:app


The application will be available in `http://localhost:8000`

## Use

To add new CRUD entities:

### Example in `examples/team/public.py`
1. Define the schemas and database model.
2. Instantiate Entity with the objects created in step 1.
### Example in `examples/team/__init__.py`
3. Now you can create your GenericCrud instance for database operations.
4. Create your RouteManager object.
### Example in `main.py`
5. Add your CRUD router to your FastAPI object, using the crud_route property of your RouteManager object.

## Contribution

Contributions are welcome! If you want to improve this project, please send a pull request. If you encounter any issues, please create an issue.

## License

This project is licensed under the MIT License.
