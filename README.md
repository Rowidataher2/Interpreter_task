# Message Processor and KPI Management

This repository implements a message processing system and a Django-based KPI management system. The project is built to handle sensor data, process it based on equations defined in a configuration file, and store the results in a relational database. Additionally, it provides endpoints to manage Key Performance Indicators (KPIs) and their linkage to assets.

---

## Features

### 1. Message Processing System
- **Data Ingestion**: Reads messages from a text file at a frequency of 1 message every 5 seconds.
- **Equation Parsing and Interpretation**:
  - Supports arithmetic operations: `+`, `-`, `*`, `/`, `^`.
  - Supports regex-based matching using the `Regex` operator.
  - Example equations:
    - `ATTR + 50 * (ATTR / 10)` - Performs arithmetic calculations.
    - `Regex(ATTR, "^dog")` - Matches if the message value starts with `dog`.
- **Message Production**: Outputs processed messages in JSON format and stores them in a relational database.
- **Extensibility**: Built using SOLID principles to facilitate the addition of new operators, data sources, and sinks.
- **Unit Testing**: Includes unit tests for the main folders.

### 2. KPI Management System (Django Project)
- **KPI Models**:
  - Save KPI details such as name, expression, and description.
  - Maintain links between KPIs and `asset_id`.
- **API Endpoints**:
  - Create and list KPIs.
  - Link assets to KPIs.
- **Swagger Documentation**: Provides detailed API documentation.
- **Unit Testing**: Includes unit tests for all major components.

---

## Project Structure

### **Message Processor**
- **Folders**:
  - `engine`: Contains processing logic, including equation parsing and interpretation.
  - `ingestor`: Handles reading messages from text files.
  - `producer`: Manages database storage of processed messages.
  - `config`: Contains configuration files like `equation_config.json`.
- **Files**:
  - `main.py`: Main entry point for the message processing system.
  - `tokenizer.py`: Tokenizes equations for processing.
  - `messages.txt`: Sample text file containing input messages.
  - `message_processor.db`: SQLite database storing processed messages.

### **Django KPI Management**
- **Project**: `kpi_project`
  - **App**: `kpi`
    - `models.py`: Defines KPI and asset-link models.
    - `serializers.py`: Serializes models for API endpoints.
    - `urls.py`: Defines API routes.
    - `views.py`: Implements API logic.
- **Swagger**: Auto-generated API documentation.

---


### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the main:
   ```bash
   python main.py
   ```

5. Set up the Django project:
   ```bash
   cd kpi_project
   python manage.py migrate
   python manage.py runserver
   ```

6. Access the API documentation at:
   ```
   http://127.0.0.1:8000/docs/
   ```

---

## Usage

### Message Processor
- Place input messages in `messages.txt`.
- Define equations in `config/equation_config.json`.
- Run `main.py` to process messages and store results in `message_storage.db`.

### KPI Management
- Use the API to create, list, and link KPIs to assets.
- Example API requests:
  - **Create KPI**:
    ```json
    POST /api/kpis/
    {
      "name": "Example post KPI",
      "expression": "ATTR + 5",
      "description": "Calculates a simple KPI."
    }
    ```
  - **Link Asset to KPI**:
    ```json
    POST /api/kpis/link/
    {
      "kpi_id": 1,
      "asset_id": "123"
    }
    ```

----

## Extensibility

- **Add New Operators**:
  - Implement a new operator class in `engine/operators.py`.
  - Update the equation parser to handle the new operator.
- **Support New Data Sources/Sinks**:
  - Implement new ingestors in the `input_ingestor` folder.
  - Implement new producers in the `storage` folder.



---

## Authors
- [rowida taher]

