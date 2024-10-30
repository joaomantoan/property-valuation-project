import logging
from sklearn.compose import ColumnTransformer
from category_encoders import TargetEncoder

log_file_path = "logs/pipeline.log"
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filemode="a",
)

logger = logging.getLogger(__name__)


def preprocessing(categorical_cols):
    """
    Creates a preprocessing pipeline that applies target encoding to
    categorical features.

    Parameters:
    - categorical_cols: list of str, names of the categorical features.

    Returns:
    - preprocessor: A ColumnTransformer object that applies target encoding.
    """
    try:
        logger.info(
            "Creating preprocessing pipeline with\
                  target encoding for categorical columns"
        )
        preprocessor = ColumnTransformer(
            transformers=[
                ('categorical', TargetEncoder(), categorical_cols)
            ]
        )
        logger.info("Preprocessing pipeline created successfully.")
        return preprocessor
    except Exception as e:
        logger.error(f"Error creating preprocessing pipeline: {e}")
        raise
