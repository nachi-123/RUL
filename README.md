# RUL Prediction Project

This project predicts engine Remaining Useful Life (RUL) from NASA CMAPSS FD001 data.

## Workflow

1. Data ingestion: parse train/test text files and create processed CSVs.
2. Prepare base model: structural stage for parity with the reference project.
3. Training: fit a CNN-LSTM model and save model/scaler artifacts.
4. Evaluation: compute RMSE and MAE and save to scores.json.

## Run locally

1. Create/activate venv.
2. Install dependencies: `pip install -r requirements.txt`
3. Train and evaluate: `python main.py`
4. Run API: `python application.py`
5. Test full training pipeline stage-by-stage: `python test_pipeline.py`

## Render deployment

1. Deploy as a Web Service from this folder.
2. Build command: `pip install -r requirements.txt`
3. Start command: `gunicorn app:app --bind 0.0.0.0:$PORT`

The app serves JSON prediction endpoints at `/predict` and `/predictdata`.
