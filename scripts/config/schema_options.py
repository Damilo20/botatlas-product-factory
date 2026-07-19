"""
BotAtlas Schema Options

Single source of truth for every Airtable Single Select option.

Never hardcode option values anywhere else.
"""

# ==========================================================
# STATUS
# ==========================================================

STATUS = {

    "research": "Research",

    "queued": "Queued",

    "collecting": "Collecting Data",

    "processing": "AI Processing",

    "review": "Pending Review",

    "published": "Published",

    "archived": "Archived"

}

# ==========================================================
# PRODUCT CATEGORIES
# ==========================================================

CATEGORIES = {

    # Humanoids
    "humanoid robot": "Humanoid Robots",
    "humanoid robots": "Humanoid Robots",

    # Industrial
    "industrial robot": "Industrial Robots",
    "industrial robots": "Industrial Robots",
    "industrial": "Industrial Robots",

    # Educational
    "educational robot": "Educational Robots",
    "educational robots": "Educational Robots",
    "educational": "Educational Robots",

    # Pets
    "robot pet": "Robot Pets",
    "robot pets": "Robot Pets",

    # Companion
    "ai companion": "AI Companions",
    "ai companions": "AI Companions",
    "companion": "AI Companions",

    # Security
    "security robot": "Security Robots",
    "security robots": "Security Robots",
    "security": "Security Robots",

    # Home
    "home robot": "Home Robots",
    "home robots": "Home Robots",
    "home": "Home Robots",

    # Drone
    "drone": "Drones",
    "drones": "Drones",

    # Consumer electronics
    "tablet": "Tablets",
    "tablets": "Tablets",

    "smart display": "Smart Displays",
    "smart displays": "Smart Displays",

    "home appliance": "Home Appliances",
    "home appliances": "Home Appliances",

    "kitchen appliance": "Kitchen Appliances",
    "kitchen appliances": "Kitchen Appliances",

    "wearable": "Wearables",
    "wearables": "Wearables",

    "audio": "Audio",

    "camera": "Cameras",
    "cameras": "Cameras",

    "e-reader": "E-Readers",
    "ereader": "E-Readers",

    "smart home": "Smart Home",

    "smart lighting": "Smart Lighting",

    "computer accessory": "Computer Accessories",
    "computer accessories": "Computer Accessories",
}

# ==========================================================
# PRIMARY USES
# ==========================================================

PRIMARY_USES = {

    "personal_assistant": "Personal Assistant",

    "home_assistant": "Home Assistant",

    "hospitality": "Hospitality",

    "receptionist": "Receptionist",

    "companion": "Companion",

    "caregiver": "Caregiver",

    "retail": "Retail Assistant",

    "delivery": "Delivery",

    "entertainment": "Entertainment",

    "education": "Education",

    "research": "Research",

    "security": "Security",

    "industrial": "Industrial",

    "inspection": "Inspection",

    "cleaning": "Cleaning"

}

# ==========================================================
# INDUSTRIES
# ==========================================================

INDUSTRIES = {

    "consumer": "Consumer",

    "commercial": "Commercial",

    "industrial": "Industrial",

    "healthcare": "Healthcare",

    "education": "Education",

    "research": "Research",

    "military": "Military",

    "agriculture": "Agriculture",

    "construction": "Construction",

    "logistics": "Logistics",

    "hospitality": "Hospitality",

    "retail": "Retail",

    "public_safety": "Public Safety",

    "entertainment": "Entertainment",

    "multi": "Multi-Industry"

}

# ==========================================================
# ENVIRONMENTS
# ==========================================================

ENVIRONMENTS = {

    "indoor": "Indoor",

    "outdoor": "Outdoor",

    "indoor_outdoor": "Indoor/Outdoor",

    "warehouse": "Warehouse",

    "factory": "Factory",

    "office": "Office",

    "home": "Home",

    "hospital": "Hospital",

    "construction": "Construction Site",

    "agriculture": "Agricultural",

    "public": "Public Space",

    "laboratory": "Laboratory"

}

# ==========================================================
# TARGET USERS
# ==========================================================

TARGET_USERS = {

    "consumer": "Consumers",

    "business": "Businesses",

    "enterprise": "Enterprise",

    "developer": "Developers",

    "government": "Government",

    "military": "Military",

    "research": "Research Labs",

    "education": "Schools",

    "healthcare": "Hospitals",

    "warehouse": "Warehouses",

    "factory": "Factories",

    "retail": "Retail Stores"

}

# ==========================================================
# MOBILITY
# ==========================================================

MOBILITY = {

    "bipedal": "Bipedal",

    "quadruped": "Quadruped",

    "wheeled": "Wheeled",

    "tracked": "Tracked",

    "stationary": "Stationary",

    "flying": "Flying",

    "hybrid": "Hybrid"

}

# ==========================================================
# AUTONOMY
# ==========================================================

AUTONOMY = {

    "manual": "Manual",

    "remote": "Remote Controlled",

    "remote controlled": "Remote Controlled",

    "assisted": "Assisted",

    "semi": "Semi-Autonomous",

    "semi autonomous": "Semi-Autonomous",

    "semi-autonomous": "Semi-Autonomous",

    "full": "Fully Autonomous",

    "fully autonomous": "Fully Autonomous",
}