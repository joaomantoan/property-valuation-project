from db_connector import connect_to_db
import pandas as pd
import logging


log_file_path = "logs/pipeline.log"
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filemode="a",
)

logger = logging.getLogger(__name__)


def load_train_data(file_path: str):
    """
    Load training data from a specified CSV file.

    Parameters:
    - path: str, path to the training data CSV file.

    Returns:
    - DataFrame containing the training data.
    """
    try:
        logger.info(f"Loading training data from {file_path}...")
        data = pd.read_csv(file_path)
        logger.info("Training data loaded successfully.")
        return data
    except Exception as e:
        logger.error(f"Error loading training data: {e}")
        raise


def load_test_data(file_path: str):
    """
    Load test data from a specified CSV file.

    Parameters:
    - path: str, path to the test data CSV file.

    Returns:
    - DataFrame containing the test data.
    """
    try:
        logger.info(f"Loading test data from {file_path}...")
        data = pd.read_csv(file_path)
        logger.info("Test data loaded successfully.")
        return data
    except Exception as e:
        logger.error(f"Error loading test data: {e}")
        raise


def load_data_from_db(query):
    """
    Executes a query to retrieve data from a database.

    Connects to a PostgreSQL database using the `connect_to_db` function,
    executes the provided SQL query, retrieves all resulting data, and
    then closes the connection.

    Parameters:
    - query : str
        The SQL query to execute for data retrieval.

    Returns:
    - list
        A list of tuples, where each tuple represents a row of data fetched
        from the database.
    """

    connection = connect_to_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return data
    finally:
        connection.close()
