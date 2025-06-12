# location logic
import pandas as pd

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from geopy.extra.rate_limiter import RateLimiter
from geopy.distance import geodesic
from haversine import haversine, Unit
import sys


def create_location_lookup(df):
  lookup = {}
  clean_df = df.dropna(subset=['latitude', 'longitude']).copy()

  clean_df['latitude'] = pd.to_numeric(clean_df['latitude'], errors="coerce")
  clean_df['longitude'] = pd.to_numeric(clean_df['longitude'], errors="coerce")

  grouped = clean_df.groupby(clean_df['location'].str.lower())

  for loc, group in grouped:
    median_lat = group['latitude'].median()
    median_lon = group['longitude'].median()

    if pd.notnull(median_lat) and pd.notnull(median_lon):
      lookup[loc.strip()] = (median_lat, median_lon)
  return lookup

def get_profiles_within_radius(user_lat, user_lon, radius, df):
  def compute_distance(row):
    try:
      profile_location= (row['latitude'], row['longitude'])
      user_location = (user_lat, user_lon)
      return geodesic(user_location, profile_location).miles
    except Exception as e:
      print("Bad row:", row["latitude"], row["longitude"], "| Error:", e)
  
  df = df.copy()
  df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
  df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")
  df['distance_miles'] = df.apply(compute_distance, axis=1)
  return df[df['distance_miles'] <= radius]


