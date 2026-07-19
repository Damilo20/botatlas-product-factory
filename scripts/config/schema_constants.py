"""
BotAtlas Commercial Database Schema

This module centralizes every Airtable table name and field name.

Never hardcode Airtable names anywhere else.
"""

# ======================================================
# TABLES
# ======================================================

COMM_PRODUCTS = "COMM_Products"

COMM_REVENUE_EVENTS = "COMM_RevenueEvents"

COMM_PERFORMANCE_SNAPSHOTS = "COMM_PerformanceSnapshots"

COMM_OPTIMIZATION_OPPORTUNITIES = "COMM_OptimizationOpportunities"

COMM_OPTIMIZATION_STRATEGIES = "COMM_OptimizationStrategies"


# ======================================================
# COMM_PRODUCTS
# ======================================================

PRODUCT_NAME = "Product Name"

MANUFACTURER = "Manufacturer"

BRAND = "Brand"

MODEL = "Model"

CATEGORY = "Category"

PRIMARY_USE = "Primary Use"

INDUSTRY = "Industry"

ENVIRONMENT = "Environment"

TARGET_USER = "Target User"

MOBILITY = "Mobility"

AUTONOMY_LEVEL = "Autonomy Level"

DESCRIPTION = "Description"

AI_SUMMARY = "AI Executive Summary"

MSRP = "MSRP"

CURRENT_PRICE = "Current Price"

AFFILIATE_LINK = "Affiliate Links"

AI_VERSION = "AI Version"

LAST_AI_ANALYSIS = "Last AI Analysis"


# ======================================================
# COMM_REVENUE_EVENTS
# ======================================================

EVENT_ID = "event_id"

PRODUCT = "product"

EVENT_TYPE = "event_type"

SOURCE = "source"

GROSS_REVENUE = "gross_revenue"

CONFIRMED_REVENUE = "confirmed_revenue"

EVENT_COUNT = "event_count"

CONVERSION_COUNT = "conversion_count"

EVENT_DATE = "event_date"

CREATED_AT = "created_at"


# ======================================================
# COMM_PERFORMANCE_SNAPSHOTS
# ======================================================

SNAPSHOT_ID = "snapshot_id"

SNAPSHOT_DATE = "snapshot_date"

TOTAL_EVENT_COUNT = "total_event_count"

TOTAL_CONFIRMED_EVENTS = "confirmed_event_count"

CONVERSION_RATE = "conversion_rate"

REVENUE_PER_CONVERSION = "revenue_per_conversion"

CONFIDENCE_SCORE = "confidence_score"

PERFORMANCE_STATUS = "performance_status"

OPTIMIZATION_SCORE = "optimization_score"

UPDATED_AT = "updated_at"


# ======================================================
# COMM_OPTIMIZATION_OPPORTUNITIES
# ======================================================

OPPORTUNITY_ID = "opportunity_id"

OPPORTUNITY_TYPE = "opportunity_type"

PRIORITY = "priority"

TITLE = "title"

DESCRIPTION_FIELD = "description"

ESTIMATED_REVENUE = "estimated_revenue_gain"

STATUS = "status"

ASSIGNED_TO = "assigned_to"

DUE_DATE = "due_date"


# ======================================================
# COMM_OPTIMIZATION_STRATEGIES
# ======================================================

STRATEGY_ID = "strategy_id"

STRATEGY_NAME = "strategy_name"

STRATEGY_CATEGORY = "strategy_category"

EXECUTION_TYPE = "execution_type"

EXPECTED_REVENUE = "expected_revenue"

IMPLEMENTATION_COST = "implementation_cost"

ROI = "roi"

EFFORT = "effort"

OWNER = "owner"

PRIMARY_USE = "Primary Use"

INDUSTRY = "Industry"

ENVIRONMENT = "Environment"

TARGET_USER = "Target User"

MOBILITY = "Mobility"

AUTONOMY_LEVEL = "Autonomy Level"

STATUS = "Status"

RELEASE_DATE = "Release Date"