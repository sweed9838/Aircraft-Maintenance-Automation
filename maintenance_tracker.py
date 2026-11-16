
# Aircraft Maintenance Discrepancy Tracker
# Sample data for educational purposes

maintenance_records = [
    {"aircraft": "2381", "issue": "Door roller bracket", "status": "Open"},
    {"aircraft": "2405", "issue": "Hydraulic leak", "status": "Open"},
    {"aircraft": "2250", "issue": "Generator failure", "status": "Closed"},
    {"aircraft": "2179", "issue": "Filter housing", "status": "Closed"}
]

print("================================")
print(" AIRCRAFT MAINTENANCE TRACKER")
print("================================")

open_count = 0
closed_count = 0

for record in maintenance_records:
    print(f"Aircraft: {record['aircraft']}")
    print(f"Issue: {record['issue']}")
    print(f"Status: {record['status']}")
    print("-----------------------------")

    if record["status"] == "Open":
        open_count += 1
    else:
        closed_count += 1

print("\nMAINTENANCE SUMMARY")
print(f"Total Records: {len(maintenance_records)}")
print(f"Open Discrepancies: {open_count}")
print(f"Closed Discrepancies: {closed_count}")


# Calculate maintenance completion percentage
total_records = len(maintenance_records)

if total_records > 0:
    completion_rate = (closed_count / total_records) * 100
else:
    completion_rate = 0

print(f"Maintenance Completion Rate: {completion_rate:.1f}%")

