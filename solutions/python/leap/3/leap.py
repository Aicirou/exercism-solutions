from datetime import date, timedelta

def leap_year(year):
  """Determines if a given year is a leap year.

  Args:
    year: The year to check.

  Returns:
    True if the year is a leap year, False otherwise.
  """

  feb_28 = date(year, 2, 28)
  next_day = feb_28 + timedelta(days=1)
  return next_day.month != 3