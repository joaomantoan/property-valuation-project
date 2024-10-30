import logging
from data_loader import load_train_data, load_test_data
from train import train_model
from evaluate import evaluate_model

log_file_path = "logs/pipeline.log"
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filemode="a",
)
logger = logging.getLogger(__name__)

categorical_cols = ["type", "sector"]
target = "price"


def main():
    """
    Main function to run the property valuation pipeline.
    Loads data, trains the model, and evaluates it.
    """
    try:
        # Load the data
        logger.info("Loading training and testing data...")
        train_data = load_train_data("data/train.csv")
        test_data = load_test_data("data/test.csv")

        features = [
            col for col in train_data.columns if col not in ['id', 'target']
        ]

        # Split features and target
        X_train = train_data[features]
        y_train = train_data[target]
        X_test = test_data[features]
        y_test = test_data[target]

        # Train the model
        logger.info("Training the model...")
        model = train_model(X_train, y_train, categorical_cols)

        # Evaluate the model
        logger.info("Evaluating the model...")
        metrics = evaluate_model(model, X_test, y_test)

        # Print the evaluation metrics
        logger.info("Evaluation Metrics:")
        for metric, value in metrics.items():
            logger.info(f"{metric}: {value}")

    except Exception as e:
        logger.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
