# ELR Surveillance Analytics

This project demonstrates a simplified Electronic Laboratory Reporting (ELR) surveillance workflow. The analysis focuses on monitoring reporting volume across facilities and districts, evaluating reporting timeliness, and detecting unusual reporting patterns such as reporting dropouts and data dumps.

## Project Structure

```text
data/
  raw/                            
notebooks/             
src/                   
outputs/
  figures/             
  tables/                             
requirements.txt       
```

## Workflow

1. `src/utils.py` 
2. `src/preprocess.py` 
3. `src/volume_analysis.py` 



## Run

```bash
pip install -r requirements.txt
```

## Data Dictionary

| Field | Description |
| --- | --- |
| `msg_control_id` | Synthetic ELR message identifier |
| `result_id` | Synthetic lab result identifier |
| `facility_id` | Reporting facility key |
| `facility_name` | Reporting facility display name |
| `clia_id` | Synthetic CLIA-like laboratory identifier |
| `county` | Facility county |
| `district` | Public health district |
| `patient_race` | Patient race, with intentional missingness |
| `patient_ethnicity` | Patient ethnicity, with intentional missingness |
| `patient_phone` | Patient phone, with intentional missingness |
| `patient_address` | Patient address, with intentional missingness |
| `collection_date` | Specimen collection date |
| `created_date` | Result creation/reporting date |
| `delay_days` | Days between collection and reporting |

