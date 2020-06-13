import pandas as pd
def main():
  filename = './processed_csv/processed.csv'
  # Read the csv
  df = pd.read_csv(filename,index_col=False)

  # Remove the cols with small standard deviation
  df = df.loc[:, df.std() > 0.0]
  # Calculate the correlation
  df.to_csv(filename,index=False)

  filename = './test_processed/processed.csv'

   # Read the csv
  df = pd.read_csv(filename,index_col=False)

  # Remove the cols with small standard deviation
  df = df.loc[:, df.std() > 0.0]
  # Calculate the correlation
  df.to_csv(filename,index=False)

  
if __name__ == '__main__':
  main()