print("=" * 50, flush=True)
print("CONTAINER STARTED - Loading Python...", flush=True)
print("=" * 50, flush=True)

try:
    print("Importing modules...", flush=True)
    import app
except Exception as e:
    print(f"FATAL ERROR: {e}", flush=True)
    import traceback
    traceback.print_exc()
    # Keep container running so we can see logs
    import time
    time.sleep(3600)
