page_number = int(input())
pages_per_hour = int(input())
days_to_read = int(input())

total_time_to_read_book = page_number / pages_per_hour
hours_per_day = total_time_to_read_book / days_to_read

print(int(hours_per_day))