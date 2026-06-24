import pandas as pd
import logging

logging.basicConfig(
    filename='automation_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    data = pd.read_csv("sample_data.csv")

    print("Input Data:")
    print(data)

    average = data['Marks'].mean()
    maximum = data['Marks'].max()
    minimum = data['Marks'].min()

    report = {
        'Average': [average],
        'Maximum': [maximum],
        'Minimum': [minimum]
    }

    report_df = pd.DataFrame(report)

    print("\nSummary Report:")
    print(report_df)

    report_df.to_csv("summary_report.csv", index=False)

    logging.info("Summary report generated successfully.")

except FileNotFoundError:
    print("CSV file not found.")

except Exception as e:
    print("Error:", e)

OUTPUT:
Input Data:
      Name  Marks
0     John     85
1     Emma     90
2    David     78
3   Sophia     92
4  Michael     88

Summary Report:
   Average  Maximum  Minimum
0     86.6       92       78