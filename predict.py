import os
import sys
import joblib
import numpy as np
import pandas as pd


def run_prediction(
    input_file="employee_data.csv",
    output_file="prediction_results.csv",
    models_dir="models",
    data_dir="data",
):
    try:
        # Path file model & preprocessor
        preprocessor_path = os.path.join(models_dir, "preprocessor.joblib")
        model_path = os.path.join(models_dir, "model_svm.joblib")

        # Memuat model dan preprocessor
        preprocessor = joblib.load(preprocessor_path)
        model = joblib.load(model_path)
        print(
            f"-> Preprocessor dan Model SVM berhasil dimuat dari folder '{models_dir}'."
        )

        # Path file input & output
        input_csv_path = (
            input_file
            if os.path.dirname(input_file)
            else os.path.join(data_dir, input_file)
        )
        output_csv_path = (
            output_file
            if os.path.dirname(output_file)
            else os.path.join(data_dir, output_file)
        )

        # Membaca dataset input
        data = pd.read_csv(input_csv_path)
        print(
            f"-> Berhasil membaca data dari {input_csv_path} ({data.shape[0]} baris)."
        )

        # Menghapus kolom konstan jika ada
        drop_cols = [
            "EmployeeId",
            "EmployeeCount",
            "Over18",
            "StandardHours",
            "Attrition",
        ]
        cols_to_drop = [c for c in drop_cols if c in data.columns]
        features = data.drop(columns=cols_to_drop)

        # Transformasi fitur dan prediksi
        features_prep = preprocessor.transform(features)
        predictions = model.predict(features_prep)
        probabilities = model.predict_proba(features_prep)[:, 1]

        # Menyimpan hasil
        result_df = data.copy()
        result_df["Predicted_Attrition"] = predictions
        result_df["Attrition_Risk_Score"] = np.round(probabilities, 4)
        result_df["Risk_Category"] = np.where(
            result_df["Attrition_Risk_Score"] >= 0.5, "High Risk", "Low Risk"
        )

        # Memastikan folder ada sebelum menyimpan
        out_dir = os.path.dirname(output_csv_path)
        if out_dir:
            os.makedirs(out_dir, exist_ok=True)

        result_df.to_csv(output_csv_path, index=False)
        print(f"-> Prediksi selesai! Hasil telah disimpan ke file: {output_csv_path}")

    except Exception as e:
        print(f"Error saat menjalankan prediksi: {str(e)}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "employee_data.csv"

    run_prediction(input_file)
