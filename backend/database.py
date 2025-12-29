import os
import logging
from azure.cosmos import CosmosClient, PartitionKey, exceptions
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger("docgen.db")

# --- Cosmos DB Configuration ---
COSMOS_URI = os.getenv("COSMOS_DB_URI")
COSMOS_KEY = os.getenv("COSMOS_DB_KEY")
COSMOS_DB_NAME = os.getenv("COSMOS_DB_NAME", "docorator_db")

users_container = None
documents_container = None
init_error = None  # Capture initialization error

def init_cosmos():
    global users_container, documents_container, init_error
    if not COSMOS_URI or not COSMOS_KEY:
        logger.warning("COSMOS_DB_URI or COSMOS_DB_KEY not set. Database features will be disabled.")
        return

    try:
        client = CosmosClient(COSMOS_URI, credential=COSMOS_KEY)
        db = client.create_database_if_not_exists(id=COSMOS_DB_NAME)
        
        # Checking for Serverless compatibility: Remove offer_throughput
        # Also fix PartitionKey usage (must be an object)
        users_container = db.create_container_if_not_exists(
            id="users", 
            partition_key=PartitionKey(path="/email")
            # offer_throughput=400 # Removed to support Serverless
        )
        documents_container = db.create_container_if_not_exists(
            id="documents",
            partition_key=PartitionKey(path="/user_id")
            # offer_throughput=400 # Removed to support Serverless
        )
        logger.info(f"Connected to Cosmos DB: {COSMOS_DB_NAME}")
        init_error = None
    except Exception as e:
        logger.exception(f"Failed to initialize Cosmos DB: {str(e)}")
        init_error = str(e)
        users_container = None
        documents_container = None

# Initialize on import (or can be called by startup event)
init_cosmos()

def get_db():
    """Dependency for FastAPI routes"""
    # For Cosmos, we just return the containers or a wrapper
    # Since we are using global clients, we can just return a dict or similar
    if users_container is None:
        # Try to init again if failed previously
        init_cosmos()
        if users_container is None:
             error_msg = f"Database not initialized. Last Error: {init_error}" if init_error else "Database not initialized"
             raise Exception(error_msg)
    
    return {
        "users": users_container,
        "documents": documents_container
    }
