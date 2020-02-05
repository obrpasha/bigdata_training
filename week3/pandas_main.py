import pandas as pd

DATA_FILE = "Automobile_data.csv"


def head_tail():
  try:
    df = pd.read_csv(DATA_FILE)
    print("Head:\n {}".format(df.head()))
    print("Tail:\n {}".format(df.head()))
  except BaseException as ex:
    print("Error: {}".format(ex))


def print_null_info():
  try:
    df = pd.read_csv(DATA_FILE)
    print("Nulls info: {}".format(df.isnull().sum()))
  except BaseException as ex:
    print("Error: {}".format(ex))


def fill_na():
  try:
    df = pd.read_csv(DATA_FILE)
    df.fillna("N/A", inplace=True)
    na_price_df = df[(df["price"] == "N/A")]
    print("Fill N/A:\n{}".format(na_price_df))
  except BaseException as ex:
    print("Error: {}".format(ex))


def most_expensive_car():
  try:
    df = pd.read_csv(DATA_FILE)

    max_row = df.loc[df["price"].idxmax()]

    company_name = max_row["company"]
    price = max_row["price"]

    print("Company: {} Price: {}".format(company_name, price))
  except BaseException as ex:
    print("Error: {}".format(ex))


def all_toyotas():
  try:
    df = pd.read_csv(DATA_FILE)
    toyotas = df[(df["company"] == "toyota")]

    print("Toyotas:\n {}".format(toyotas))
  except BaseException as ex:
    print("Error: {}".format(ex))


def count_per_company():
  try:
    df = pd.read_csv(DATA_FILE)
    grouped_df = df.groupby('company').size()
    print("Count per company:\n{}".format(grouped_df))
  except BaseException as ex:
    print("Error: {}".format(ex))


def company_max_price():
  try:
    df = pd.read_csv(DATA_FILE)
    grouped_df = df.groupby('company').agg({'price': 'max'})
    print("Company max price:\n{}".format(grouped_df))
  except BaseException as ex:
    print("Error: {}".format(ex))


def company_avg_mileage():
  try:
    df = pd.read_csv(DATA_FILE)
    grouped_df = df.groupby('company').agg({'average-mileage': 'mean'})
    print("Company average mileage:\n{}".format(grouped_df))
  except BaseException as ex:
    print("Error: {}".format(ex))


def sort_by_price():
  try:
    df = pd.read_csv(DATA_FILE)
    sorted_df = df.sort_values(by=['price'])

    print("Sorted by price:\n{}".format(sorted_df))
  except BaseException as ex:
    print("Error: {}".format(ex))


def concatenate_df():
  german_cars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925, 71400]}
  japanese_cars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500, 58900]}

  german_cars_df = pd.DataFrame(german_cars, index=german_cars["Company"])
  japanese_cars_df = pd.DataFrame(japanese_cars, index=japanese_cars["Company"])

  concat_df = pd.concat([german_cars_df, japanese_cars_df])

  print("Concat:\n{}".format(concat_df))


def merge_df():
  car_price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925, 71400]}
  car_horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182, 160]}

  car_price_df = pd.DataFrame(car_price, index=car_price["Company"])
  car_horsepower_df = pd.DataFrame(car_horsepower, index=car_horsepower["Company"])

  merge_df = pd.merge(car_price_df, car_horsepower_df, on='Company')

  print("Merge:\n{}".format(merge_df))


def main():
  head_tail()
  print_null_info()
  fill_na()
  most_expensive_car()
  all_toyotas()
  count_per_company()
  company_max_price()
  company_avg_mileage()
  sort_by_price()
  concatenate_df()
  merge_df()


if __name__ == "__main__":
  main()
