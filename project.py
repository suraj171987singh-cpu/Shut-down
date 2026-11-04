def shutdown():
    
    shutdown= input("Do you want to shutdown the system? (yes/no): ")
    if shutdown.lower() == "yes":
        print("Shutting down the system...")
        
    else:
      print("Aborting shut down.")

shutdown()