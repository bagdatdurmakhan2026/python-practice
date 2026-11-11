def get_application():
    return{
        "application" : "Mlops learning API",
        "environment" : "development",
        "status" : "running"
    }
if __name__ == "__main__":
    app_status = get_application()
    print(app_status)