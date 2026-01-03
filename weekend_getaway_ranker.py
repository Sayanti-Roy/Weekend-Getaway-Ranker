import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time

# --- CONFIGURATION ---
SOURCE_CITIES = {
    'Delhi': (28.6139, 77.2090),
    'Mumbai': (19.0760, 72.8777),
    'Bangalore': (12.9716, 77.5946),
    'Chennai': (13.0827, 80.2707),
    'Kolkata': (22.5726, 88.3639),
    'Hyderabad': (17.3850, 78.4867)
}

# Fallback cache to ensure script works instantly for the demo cities
# (Fetching 200+ cities via API can be slow/flaky, so we preload common ones)
CACHE_COORDS = {
    'Agra': (27.1767, 78.0081), 'Jaipur': (26.9124, 75.7873), 
    'Rishikesh': (30.0869, 78.2676), 'Nainital': (29.3919, 79.4542), 
    'Chandigarh': (30.7333, 76.7794), 'Mussoorie': (30.4599, 78.0664),
    'Lonavala': (18.7515, 73.4056), 'Pune': (18.5204, 73.8567), 
    'Mahabaleshwar': (17.9235, 73.6586), 'Goa': (15.2993, 74.1240), 
    'Nashik': (19.9975, 73.7898), 'Mysore': (12.2958, 76.6394), 
    'Coorg': (12.3375, 75.8069), 'Ooty': (11.4102, 76.6950), 
    'Chikmagalur': (13.3153, 75.7754), 'Wayanad': (11.6854, 76.1320),
    'Shimla': (31.1048, 77.1734), 'Manali': (32.2432, 77.1892),
    'Udaipur': (24.5854, 73.7125), 'Amritsar': (31.6339, 74.8723)
}

def get_coordinates(city, geolocator):
    """Fetches coordinates for a city with caching."""
    # 1. Check Hardcoded Cache
    if city in CACHE_COORDS:
        return CACHE_COORDS[city]
    
    # 2. Try Geopy (Internet Required)
    try:
        location = geolocator.geocode(f"{city}, India", timeout=10)
        if location:
            return (location.latitude, location.longitude)
    except (GeocoderTimedOut, Exception):
        return None
    return None

def haversine(lat1, lon1, lat2, lon2):
    """Calculates distance (km) between two lat/lon points."""
    R = 6371  # Earth radius in km
    phi1, phi2 = np.radians(lat1), np.radians(lat2)
    dphi = np.radians(lat2 - lat1)
    dlambda = np.radians(lon2 - lon1)
    
    a = np.sin(dphi/2)**2 + np.cos(phi1)*np.cos(phi2)*np.sin(dlambda/2)**2
    c = 2*np.arctan2(np.sqrt(a), np.sqrt(1-a))
    return R * c

def recommend_weekend_getaways(source_city, file_path=r'D:\Projects\Intern-Assessment-2025\task-4-travel-ranker\visit.csv'):
    # 1. Load and Clean Data
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()  # Remove spaces from column names
    
    # 2. Setup Geocoder
    geolocator = Nominatim(user_agent="weekend_ranker_app")
    
    # 3. Get Source City Coordinates
    if source_city in SOURCE_CITIES:
        src_lat, src_lon = SOURCE_CITIES[source_city]
    else:
        # Try to find source city if not in config
        coords = get_coordinates(source_city, geolocator)
        if not coords:
            return f"❌ Could not find coordinates for source city: {source_city}"
        src_lat, src_lon = coords

    print(f"📍 Processing recommendations for: {source_city} ({src_lat}, {src_lon})...")

    # 4. Aggregate Data by City
    # The dataset has individual spots; we need to rank 'Cities'.
    # Logic: Rating = Average of spots, Popularity = Sum of review counts
    city_group = df.groupby('City').agg({
        'Google review rating': 'mean',
        'Number of google review in lakhs': 'sum',
        'Type': lambda x: ', '.join(x.unique()[:2])  # Just grab first 2 types for description
    }).reset_index()

    # 5. Enrich with Coordinates & Distance
    # Note: We filter for unique cities to minimize API calls
    city_group['Coordinates'] = city_group['City'].apply(lambda x: get_coordinates(x, geolocator))
    
    # Drop cities where coordinates weren't found
    city_group = city_group.dropna(subset=['Coordinates'])
    
    # Calculate Distances
    city_group['Distance_km'] = city_group.apply(
        lambda row: haversine(src_lat, src_lon, row['Coordinates'][0], row['Coordinates'][1]), axis=1
    )

    # 6. FILTER: Weekend Logic (Between 20km and 500km)
    weekend_destinations = city_group[
        (city_group['Distance_km'] > 20) & 
        (city_group['Distance_km'] <= 500)
    ].copy()

    if weekend_destinations.empty:
        return f"⚠️ No destinations found within 500km of {source_city}."

    # 7. RANKING ALGORITHM
    # Normalize metrics to 0-1 scale
    # Distance: Lower is better (1 - normalized)
    weekend_destinations['Norm_Dist'] = 1 - (weekend_destinations['Distance_km'] / 500)
    
    # Rating: Higher is better (0-5 scale)
    weekend_destinations['Norm_Rating'] = weekend_destinations['Google review rating'] / 5.0
    
    # Popularity: Higher is better (Log scale handles outliers like Taj Mahal better)
    weekend_destinations['Norm_Pop'] = np.log1p(weekend_destinations['Number of google review in lakhs'])
    weekend_destinations['Norm_Pop'] = weekend_destinations['Norm_Pop'] / weekend_destinations['Norm_Pop'].max()

    # Weighted Score
    # Distance (40%), Rating (40%), Popularity (20%)
    weekend_destinations['Score'] = (
        0.4 * weekend_destinations['Norm_Dist'] +
        0.4 * weekend_destinations['Norm_Rating'] +
        0.2 * weekend_destinations['Norm_Pop']
    )

    # 8. Format Output
    top_5 = weekend_destinations.sort_values(by='Score', ascending=False).head(5)
    
    result = top_5[['City', 'Type', 'Distance_km', 'Google review rating', 'Score']].copy()
    result['Distance_km'] = result['Distance_km'].round(1)
    result['Score'] = result['Score'].round(2)
    result['Google review rating'] = result['Google review rating'].round(1)
    
    return result

# --- EXECUTION ---
if __name__ == "__main__":
    while True:
        print("\n🔎 --- Weekend Getaway Recommender ---")
        source_city = input("Enter your source city (or type 'exit' to quit): ").strip()
        
        if source_city.lower() == 'exit':
            print("👋 Goodbye!")
            break
            
        print(f"\n🚗 Finding top weekend getaways from {source_city}...")
        try:
            recommendations = recommend_weekend_getaways(source_city)
            if isinstance(recommendations, str):
                print(recommendations) # Print error message if any
            else:
                print(recommendations.to_string(index=False))
        except Exception as e:
            print(f"❌ Error: {e}")