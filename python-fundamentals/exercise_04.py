company = input("Enter company name: ")
files_per_day = int(input("Enter number of files per day: "))
file_size = float(input("Enter average file size (MB): "))
days = int(input("Enter number of days: "))
price_per_gb = float(input("Enter storage price per GB (EUR): "))


daily_storage = files_per_day * file_size
total_storage_mb = daily_storage * days
total_storage_gb = total_storage_mb / 1024
storage_cost = total_storage_gb * price_per_gb


print("\n======= DATA STORAGE REPORT =======")
print("Company:", company)
print("Files Per Day:", files_per_day)
print(f"Average File Size: {file_size:.2f} MB")
print("Days:", days)
print(f"\nDaily Storage: {daily_storage:.2f} MB")
print(f"Total Storage: {total_storage_mb:.2f} MB")
print(f"Total Storage: {total_storage_gb:.2f} GB")
print(f"\nStorage Cost: {storage_cost:.2f} EUR")
print("===================================")

