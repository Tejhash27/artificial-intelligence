from pyswip import Prolog

def run_prolog_db():
    # Initialize the Prolog engine
    prolog = Prolog()
    
    # Consult/load the Prolog database file
    # Ensure 'database.pl' is in the same directory as this script
    try:
        prolog.consult("database.pl")
    except Exception as e:
        print("Error loading database.pl. Make sure the file exists in the directory.")
        return

    print("=" * 60)
    print("      PROLOG DATABASE INTERFACE VIA PYTHON")
    print("=" * 60)

    # Query 1: Fetch the complete DOB for a specific individual (e.g., priya)
    print("Querying Priya's Date of Birth...")
    results1 = list(prolog.query("find_dob(priya, Day, Month, Year)"))
    for res in results1:
        # Decode bytes from Prolog atoms to readable strings
        month = res['Month'].decode('utf-8') if isinstance(res['Month'], bytes) else res['Month']
        print(f" -> Priya was born on: {res['Day']} {month.capitalize()} {res['Year']}\n")

    # Query 2: Find all individuals born in the year 1995
    target_year = 1995
    print(f"Finding everyone born in the year {target_year}...")
    results2 = list(prolog.query(f"born_in_year(Name, {target_year})"))
    if results2:
        for res in results2:
            name = res['Name'].decode('utf-8') if isinstance(res['Name'], bytes) else res['Name']
            print(f" -> {name.capitalize()}")
    else:
        print(" -> No records found.")
    print()

    # Query 3: Find all individuals born in the month of May
    target_month = "may"
    print(f"Finding everyone born in the month of {target_month.capitalize()}...")
    results3 = list(prolog.query(f"born_in_month(Name, {target_month})"))
    if results3:
        for res in results3:
            name = res['Name'].decode('utf-8') if isinstance(res['Name'], bytes) else res['Name']
            print(f" -> {name.capitalize()}")
    else:
        print(" -> No records found.")
        
    print("=" * 60)

if __name__ == "__main__":
    run_prolog_db()
