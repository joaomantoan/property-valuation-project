from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingRegressor
from preprocessing import preprocessing
from model_config import model_params
import logging
import pickle


log_file_path = "logs/train.log"
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filemode="a",
)
logger = logging.getLogger(__name__)


def create_pipeline(categorical_features):
    """
    Builds a pipeline with preprocessing and model steps.

    Parameters:
    - categorical_features: list of categorical feature names.

    Returns:
    - pipeline: A scikit-learn Pipeline object.
    """
    preprocessor = preprocessing(categorical_features)

    # Defines the model and its hyperparameters
    model = GradientBoostingRegressor(**model_params)

    # Creates the pipeline
    pipeline = Pipeline(
        steps=[("preprocessor", preprocessor), ("model", model)]
    )

    return pipeline


def train_model(X_train, y_train, categorical_features):
    """
    Trains the pipeline on the given data.

    Parameters:
    - X_train: Features for training.
    - y_train: Target variable for training.
    - categorical_features: List of categorical feature names.

    Returns:
    - pipeline: The trained model pipeline.
    """
    logger.info("Starting model training...")

    try:
        pipeline = create_pipeline(categorical_features)
        pipeline.fit(X_train, y_train)

        # Dumps model pipeline into pickle file in the model directory
        with open("model/model_pipeline.pkl", "wb") as f:
            pickle.dump(pipeline, f)

        logger.info(
            "Model training completed and saved as model/model_pipeline.pkl"
        )

    except Exception as e:
        logger.error(f"Error during model training: {e}")
        raise

    return pipeline
