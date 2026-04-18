import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load
file_path = "lending_club_loan_two.csv"

# Load the latest version
df = kagglehub.dataset_load(
  KaggleDatasetAdapter.PANDAS,
  "jeandedieunyandwi/lending-club-dataset",
  file_path
)

print(df.columns)