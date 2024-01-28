import os 
import warnings
import logging

from dotenv import load_dotenv
from supabase import create_client

def load_supabase_client():
    load_dotenv()
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    try: 
        client = create_client(supabase_url=url, supabase_key=key)
        logging.info("Successfully connected to supabase client")
        return client
    except:
        logging.error("Failed to connect to supabase client. Exiting.")

