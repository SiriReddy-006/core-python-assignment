patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]


def search_patient():
    d = input("Enter disease to search: ")
    result = []
    for p in patients:
        if p["Disease"].lower() == d.lower():
            result.append(p["Name"])

    if len(result) == 0:
        print("No patients found")
    else:
        print("Patients with", d, ":", result)

search_patient()


