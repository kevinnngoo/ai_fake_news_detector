from app import create_app
from pymongo import MongoClient

def test_connections():
    # Test Flask
    try:
        app = create_app()
        print("✅ Flask initialized successfully")
    except Exception as e:
        print("❌ Flask initialization failed:", str(e))
        return

    # Test MongoDB
    try:
        client = MongoClient(app.config['MONGODB_URI'])
        # This command will trigger an actual connection attempt
        client.admin.command('ping')
        print("✅ MongoDB connected successfully")
        
        # Test database access
        db = client.get_default_database()
        collections = db.list_collection_names()
        print(f"📁 Available collections: {collections}")
    except Exception as e:
        print("❌ MongoDB connection failed:", str(e))

if __name__ == "__main__":
    test_connections()